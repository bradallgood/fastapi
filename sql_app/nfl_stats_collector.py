import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import psycopg2
from sqlalchemy import create_engine

  
conn_string = 'postgresql://brada:Feasant1@172.28.176.1/nfl'
db = create_engine(conn_string)

week = 1
for year in [2021,2022]:
    while week <= 2:
        print(f'=========================== Week {week} =========================')
        for stats_cat in ['passing','rushing','receiving']:
            print(f'---------------------- Catagory {stats_cat} ----------------------')
            table_qb = pd.read_html(f'https://www.espn.com/nfl/weekly/leaders/_/week/{week}/seasontype/2/type/{stats_cat}')
            qb = table_qb[6]
            cols = qb.columns.tolist()
            new_cols = qb.loc[1].tolist()
            col_dict = dict(zip(cols, new_cols))
            qb.rename(columns=col_dict,inplace=True)
            qb.drop([0,1],inplace=True)
            qb.reset_index(inplace=True,drop=True)
            qb[['NAME','POSITION']]= qb['PLAYER'].str.split(",", expand = True)
            qb[['WIN_LOSS','SCORE','HOME_AWAY','OPPONENT']]= qb['RESULT'].str.split( expand = True)
            qb.loc[qb['HOME_AWAY'] == 'at', 'HOME_AWAY'] = 'AWAY'
            qb.loc[qb['HOME_AWAY'] == 'vs.', 'HOME_AWAY'] = 'HOME'
            qb[['WINNER_SCORE','LOSER_SCORE']]= qb['SCORE'].str.split("-", expand = True)
            qb[['WINNER_SCORE','LOSER_SCORE']] = qb[['WINNER_SCORE','LOSER_SCORE']].apply(pd.to_numeric)
            qb['SPREAD'] = qb['WINNER_SCORE'] - qb['LOSER_SCORE']
            qb.loc[qb['WIN_LOSS'] == 'L', 'SPREAD'] = qb['SPREAD'] * -1
            qb.drop(columns=['PLAYER', 'RESULT'],inplace=True)
            qb['YEAR'] = year
            qb[['YEAR']] = qb[['YEAR']].apply(pd.to_numeric)
            qb['WEEK'] = week
            qb[['YEAR']] = qb[['YEAR']].apply(pd.to_numeric) 
            qb["PKCOL"] = qb['YEAR'].astype(str) +"-"+ qb["WEEK"].astype(str)+"-"+ qb["NAME"].astype(str)
            if stats_cat in ['rushing','receiving']:
                qb = qb.loc[:, qb.columns.notna()]
            if stats_cat == 'passing':
                qb[['RK', 'COMP', 'ATT', 'YDS', 'TD', 'INT','SACK', 'FUM', 'RAT']] = qb[['RK', 'COMP', 'ATT', 'YDS', 'TD', 'INT',
                    'SACK', 'FUM', 'RAT']].apply(pd.to_numeric)
                qb['COMP_PER'] = qb['COMP'] / qb['ATT']
            elif stats_cat == 'rushing':
                qb[['RK', 'CAR', 'YDS', 'AVG', 'TD', 'LNG', 'FUM']] = qb[['RK', 'CAR', 'YDS', 'AVG', 'TD', 'LNG', 'FUM']].apply(pd.to_numeric)
            elif stats_cat == 'receiving':
                qb[['RK', 'REC', 'YDS', 'AVG', 'TD', 'LNG', 'FUM']] = qb[['RK', 'REC', 'YDS', 'AVG', 'TD', 'LNG', 'FUM']].apply(pd.to_numeric)
            print(qb.columns)
            print(qb.info())

            conn = db.connect()  
            qb.to_sql(stats_cat, con=conn, if_exists='append',index=True)
            conn = psycopg2.connect(conn_string)
            conn.autocommit = True
            cursor = conn.cursor()
  
            # conn.commit()
            conn.close()

        week += 1

with db.connect() as con:
    con.execute('ALTER TABLE "passing" ADD PRIMARY KEY ("PKCOL");')
    con.execute('ALTER TABLE "receiving" ADD PRIMARY KEY ("PKCOL");')
    con.execute('ALTER TABLE "rushing" ADD PRIMARY KEY ("PKCOL");')
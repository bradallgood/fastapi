from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Passing(Base):
    __tablename__ = "passing"

    RK = Column(Integer)
    TEAM = Column(String)
    COMP = Column(Integer)         
    ATT = Column(Integer)          
    YDS = Column(Integer)          
    TD = Column(Integer)           
    INT = Column(Integer)          
    SACK = Column(Integer)         
    FUM = Column(Integer)          
    RAT = Column(Float)          
    NAME = Column(String, primary_key=True)         
    POSITION = Column(String)     
    COMP_PER = Column(Float)     
    WIN_LOSS = Column(String)    
    SCORE = Column(String)        
    HOME_AWAY = Column(String)    
    OPPONENT = Column(String)     
    WINNER_SCORE = Column(Integer) 
    LOSER_SCORE = Column(Integer)  
    SPREAD = Column(Integer)       
    YEAR = Column(String, primary_key=True)
    WEEK = Column(String, primary_key=True) 
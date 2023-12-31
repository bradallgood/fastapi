from sqlalchemy.orm import Session
from sqlalchemy import select

import models, schemas


def get_passing(db: Session, skip: int = 0, limit: int = 100):
    passing_yds = select(models.Passing)
    stmt = select(models.Passing.NAME,models.Passing.YDS)
    print(stmt)
    for user in db.execute(stmt).all():
        print(user)
    return db.query(models.Passing).offset(skip).limit(limit).all()

def get_passing_yds(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(models.Passing.NAME,models.Passing.YDS)
    return db.execute(stmt).all()
    #return db.query(models.Passing.NAME).offset(skip).limit(limit).all()
 
def get_distinctName(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(models.Passing.NAME).distinct()
    print(stmt)
    for user in db.execute(stmt).all():
        print(user)
    return db.execute(stmt).all()

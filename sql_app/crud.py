from sqlalchemy.orm import Session
from sqlalchemy import select

import models, schemas


#def get_pass(db: Session, user_id: int):
#    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


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




#def create_user(db: Session, user: schemas.UserCreate):
#    fake_hashed_password = user.password + "notreallyhashed"
#    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#    db.add(db_user)
#    db.commit()
#    db.refresh(db_user)
#    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


#def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#    db_item = models.Item(**item.dict(), owner_id=user_id)
#    db.add(db_item)
#    db.commit()
#    db.refresh(db_item)
#    return db_item

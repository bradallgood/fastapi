from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine

from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#@app.post("/users/", response_model=schemas.User)
#def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    db_user = crud.get_user_by_email(db, email=user.email)
#    if db_user:
#        raise HTTPException(status_code=400, detail="Email already registered")
#    return crud.create_user(db=db, user=user)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/passing/", response_model=list[schemas.Passing])
def read_passing(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passing = crud.get_passing(db, skip=skip, limit=limit)
    return passing

@app.get("/passing_yds/", response_model=list[schemas.Passing_yds])
def read_passing_yds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passing = crud.get_passing_yds(db, skip=skip, limit=limit)
    return passing

@app.get("/distinct_name/", response_model=list[schemas.Passing_name])
def get_distinct_name(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passing = crud.get_distinctName(db, skip=skip, limit=limit)
    return passing

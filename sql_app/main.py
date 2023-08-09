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
    print('Hello World')
    passing = crud.get_passing(db, skip=skip, limit=limit)
    return passing

@app.get("/passing_yds/", response_model=list[schemas.Passing_yds])
def read_passing_yds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passing = crud.get_passing_yds(db, skip=skip, limit=limit)
    return passing

#@app.get("/passing_yds/", response_model=list[schemas.Passing])
#def read_passing_yds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    passing_yds = crud.get_passing_yds(db, skip=skip, limit=limit)
#    return passing_yds

@app.get("/test/")
async def test():
    return {"message": "This is test"}

#@app.get("/users/{user_id}", response_model=schemas.User)
#def read_user(user_id: int, db: Session = Depends(get_db)):
#    db_user = crud.get_user(db, user_id=user_id)
#    if db_user is None:
#        raise HTTPException(status_code=404, detail="User not found")
#    return db_user


#@app.post("/users/{user_id}/items/", response_model=schemas.Item)
#def create_item_for_user(
#    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
#):
#    return crud.create_user_item(db=db, item=item, user_id=user_id)


#@app.get("/items/", response_model=list[schemas.Item])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    items = crud.get_items(db, skip=skip, limit=limit)
#    return items

from pydantic import BaseModel


class PassingBase(BaseModel):
    pass


class Passing(PassingBase):
    RK: int
    TEAM: str
    COMP: int         
    ATT: int          
    YDS: int          
    TD: int           
    INT: int          
    SACK: int         
    FUM: int          
    RAT: float          
    NAME: str         
    POSITION: str     
    COMP_PER: float   
    WIN_LOSS: str    
    SCORE: str        
    HOME_AWAY: str    
    OPPONENT: str     
    WINNER_SCORE: int 
    LOSER_SCORE: int  
    SPREAD: int       
    YEAR: str
    WEEK: str 

    class Config:
        orm_mode = True

class Passing_yds(PassingBase):         
    YDS: int          
    NAME: str         

    class Config:
        orm_mode = True

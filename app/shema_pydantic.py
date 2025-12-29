from pydantic import BaseModel, EmailStr
from typing import List, Text
from datetime import datetime

class ProjetsResponse(BaseModel):
    title : str
    description : str
    outils : List
    lien : str
    
    class config:
        orm_mode = True # sérialisation des objets SQLAlchemy / ORM -> JSON
        
class CreateUser(BaseModel) :
    username : str
    password : str
    
class GetUser(BaseModel) :
    username : str
    is_active : str
    
class GetMessage(BaseModel):
    full_name : str
    email : EmailStr
    sujet : str
    message : Text
    created_at : datetime
from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session

from typing import List
from app.database import get_db
from app.shema_pydantic import ProjetsResponse, GetMessage
from app.models import Projet
from app.crud import get_message
from datetime import datetime

router = APIRouter()

@router.get("/projets/", response_model=List[ProjetsResponse])
def all_projets(db:Session = Depends(get_db)) :
    items = db.query(Projet).all()
    return items

@router.post("/message")
def message_get(
    request : Request,
    db : Session = Depends(get_db),
    full_name : str = Form(...),
    email : str = Form(...),
    sujet : str = Form(...),
    message : str = Form(...)
) :
    data = GetMessage(
        full_name = full_name,
        email = email,
        sujet = sujet,
        message = message,
        created_at = datetime.utcnow()
    )
    message = get_message(db, data)
    
    return {
            "status" : "success",
            "message" : message
        }
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
# from app.models import Message
from app.database import engine, Base, get_db
from app import api

from app.models import Projet, Text1, About1, About2, About3, Service, Skill, Langage, Contact

app = FastAPI(title="John Lion - Porte Folio")

# inclure les api routers
app.include_router(api.router, prefix="/api")

# table BD
Base.metadata.create_all(bind=engine)

# statique (css & js)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# templates, html
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request : Request, db=Depends(get_db)) :
    # objets
    projets = db.query(Projet).all()
    services = db.query(Service).all()
    skills = db.query(Skill).all()
    languages = db.query(Langage).all()
    contact = db.query(Contact).first()
    # texte
    home_text = db.query(Text1).first().text
    about_p1 = db.query(About1).first().text
    about_p2 = db.query(About2).first().text
    about_p3 = db.query(About3).first().text
    return templates.TemplateResponse(
        "folio.html", 
        {
            "request": request,
            "projets" : projets,
            "services" : services,
            "skills" : skills,
            "contact" : contact,
            "home_texte" : home_text,
            "about_p1" : about_p1,
            "about_p2" : about_p2,
            "about_p3" : about_p3,
            "languages" : languages,
        }
    )

if __name__ == "__main__" :
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
from app.database import Base
from sqlalchemy import Column, Integer, String, Text, JSON, Boolean, DateTime
from datetime import datetime

class AdminUser(Base) :
    __tablename__ = "Admin User"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(70), nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class Text1(Base):
    __tablename__ = "Texte home"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

class About1(Base):
    __tablename__ = "About p1"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

class About2(Base):
    __tablename__ = "About p2"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    
class About3(Base):
    __tablename__ = "About p3"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

class Projet(Base) :
    __tablename__ = "Projet"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    outils = Column(JSON, nullable=False)
    lien = Column(String)
    
class Service(Base):
    __tablename__ = "Service"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    outils = Column(JSON, nullable=False)
    lien = Column(String)    

class Message(Base) :
    __tablename__ = "Messages"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    sujet = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Skill(Base) :
    __tablename__ = "Domaine de Compétence"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    
class Langage(Base) :
    __tablename__ = "Language de programmation"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)

class Contact(Base):
    __tablename__ = "Contact Infos"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    github = Column(String, nullable=False)
    github_link = Column(String, nullable=False)
    linkedin = Column(String, nullable=False)
    linkedin_link = Column(String, nullable=False)

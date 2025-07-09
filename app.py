import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración DB (ajustá usuario, contraseña, host, bd)
engine = create_engine("mysql+pymysql://usuario:contraseña@localhost/tareas_db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de la tabla
class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    tarea = Column(Text)
    subtarea = Column(Text)
    hora_inicio = Column(DateTime)
    hora_final = Column(DateTime)
    comentarios = Column(Text)
    completado = Column(Boolean)

Base.metadata.create_all(engine)

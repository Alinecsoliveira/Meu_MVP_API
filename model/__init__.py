from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.pokemon import Pokemon

db_path = "database/"
if not os.path.exists(db_path):
     os.makedirs(db_path)

db_url = f"sqlite:///{db_path}/db.sqlite3"

engine = create_engine(
    db_url,
    echo=False,
    connect_args={"check_same_thread": False}, 
    pool_pre_ping=True,                         
    pool_size=5,                                
    max_overflow=10 
)                            

Session = sessionmaker(bind=engine)


if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

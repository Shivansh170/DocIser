from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.settings import settings


engine=create_engine(settings.DATABASE_URL)
sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()
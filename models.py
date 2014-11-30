from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import *


engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)



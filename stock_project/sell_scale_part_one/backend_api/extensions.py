''' The intention of this file is that the 
    project doesn't run into any circular 
    errors.'''
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import and_

db = SQLAlchemy()
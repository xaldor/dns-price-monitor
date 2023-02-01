from sqlalchemy.orm import declarative_base
from typing import Type


BaseSQLModel: Type = declarative_base()
""" Serves as a parent class for all other database model classes defined in application.
Every class inherited from `BaseSQLModel` will be mapped to actual database table."""

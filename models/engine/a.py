#!/usr/bin/python3
"""This module defines a class to manage the database storage fro hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes  = [Amenity, City, Place, Review, State, User]

class DBStorage:
    """saves, retireves, updates and deletes objects in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate objects of this class and 
        also creates the engine of the database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                 format(getenv("HBNB_MYSQL_USER"),
                     getenv("HBNB_MYSQL_PWD"),
                     getenv("HBNB_MYSQL_HOST"),
                     getenv("HBNB_MYSQL_DB")),
                 pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Returns all the objects of a certains class currently in the database"""
        all_objs = {}
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for c in classes:
                for obj in objs:
                    all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return all_objs
    
    def new(self, obj):
        """Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Committs all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the current database session"""
        if obj is not None:
            obj = self.__session.query(type(obj)).filter(type(obj).id == obj.id)
            self.__session.delete(ob)
    
    def reload(self):
        """Creates a session and creates the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                )
        Session = scoped_session(session_factory)
        self.session = Session()

    def close(self):
        """close a session"""
        self.__session.close()

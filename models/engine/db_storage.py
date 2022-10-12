#!/usr/bin/python3
"""This module defines a class to manage the database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = [Amenity, City, Place, Review, State, User]


class DBStorage:
    """Saves, updates, retrieves and deletes objects in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates objects of this class
        creates the engine for our database"""
        os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
        os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_ENV = os.getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB
        ), pool_pre_ping=True)
#        self.engine = create_engine('mysql+mysqldb://'+HBNB_MYSQL_USER+':'+HBNB_MYSQL_PWD+'@'+HBNB_MYSQL_HOST+'/'+HBNB_MYSQL_DB+"?charset=utf8")

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all the objects of a certain class
        currently in the database"""

        all_objs = {}
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for c in classes:
                objs = self.__session.query(c).all()
                for obj in objs:
                    all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return all_objs

    def new(self,  obj):
        """Adds a new object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """Committs all changes to the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the current database session"""

        if obj is not None:
            ob = self.__session.query(type(obj)).filter(type(obj).id == obj.id)
            self.__session.delete(ob)

    def reload(self):
        """creates a session and creates all tables in the database"""

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes a session"""
        self.__session.close()

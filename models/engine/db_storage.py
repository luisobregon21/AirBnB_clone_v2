#!/usr/bin/python3
''' STORAGE for when the Engine is based on SQL '''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


hbnb_classes = {
                'BaseModel': BaseModel, 'City': City,
                'User': User, 'Place': Place, 'State': State,
                'Amenity': Amenity, 'Review': Review
                }


class DBStorage:
    ''' Database storage class '''
    __engine = None
    __session = None

    def __init__(self):
        ''' DataBase Storage Constructor '''
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        '''
        query on the current database session
        all objects depending of the class name
        '''
        session_dic = {}

        ''' 
        NOTE: The all I think is working but it's mot saving
        the database
        '''

        if cls in hbnb_classes.values():
            for obj in self.__session.query(cls).all():
                session_dic[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for cls in hbnb_classes.values():
                for obj in self.__session.query(cls):
                    session_dic[obj.__class__.__name__ + "." + obj.id] = obj
        return session_dic

    def new(self, obj):
        ''' add the object to the current database session '''
        self.__session.add(obj)

    def delete(self, obj=None):
        ''' delete from the current database session obj if not None '''
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        '''  commit all changes of the current database session '''
        self.__session.commit()

    def reload(self):
        ''' create all tables in the database (feature of SQLAlchemy) '''
        Base.metadata.create_all(self.__engine)
        print("WHATS UP????\n\n")
        # creates a new session
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # creates a new object
        Session = scoped_session(s_factory)

        # Is an instanced of the session which can be used to talk to the DB
        self.__session = Session()

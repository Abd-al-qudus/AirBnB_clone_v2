"""
    A new storage engine for mysqldb
"""
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """mysql Database for the AirBnB project"""
    __engine = None
    __session = None
    __clsdict = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """init method for creating new engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(env['HBNB_MYSQL_USER'],
                                             env['HBNB_MYSQL_PWD'], env['HBNB_MYSQL_HOST'],
                                             env['HBNB_MYSQL_DB'],), pool_pre_ping=True)
        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query for objects depend on the class
                    """
        dict = {}
        cls = cls if not isinstance(cls, str) else self.__clsdict.get(cls)
        if cls:
            for obj in self.__session.query(cls):
                dict["{}.{}".format(
                    cls.__name__, obj.id
                )] = obj
            return dict
        for k, cls in self.__clsdict.items():
            for obj in self.__session.query(cls):
                dict["{}.{}".format(cls.__name__, obj.id)] = obj
        return dict

    def new(self, obj):
        """add the object to the session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit session on the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db is not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload the database"""
        """create all tables in the database
                """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=True)
        self.__session = scoped_session(factory)()

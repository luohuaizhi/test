# -*- encoding:utf-8-*-
import MySqlDB
from settings import database

db = MySqlDB.connect(host=database["host"], port=["port"], user=["username"], pwd=["password"])

class Entity(type):
    """docstring for Entity"""
    def __new__(cls, cls_name, cls_attrs):

        return 
        

class Model(Entity):

    def __init__()
        super(Entity, self).__init__()
        
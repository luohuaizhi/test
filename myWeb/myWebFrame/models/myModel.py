# -*- encoding:utf-8-*-
from models import Model

class User(Model):

    __table__ = "user"
    
    def __init__(self, name, pwd, phone=""):
        super(Model, self).__init__()
        self.name = name
        self.pwd = pwd
        self.phone = phone



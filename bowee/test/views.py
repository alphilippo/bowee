from bottle import run , debug , route
from bottle import request , response , redirect , template
import models
import peewee

#create your views

@route('/')
@route('/index')
def index():
    return "Hello World !!!"


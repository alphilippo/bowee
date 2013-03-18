from bottle import run , debug , route
from bottle import request , response , redirect , template
#import models
#import peewee

#create your views

@route('/')
@route('/hello/<name>')
def index(name):
    return template('test.tpl.html',montag=name)

run(host='localhost',port='8088',reloader=True,debug=True)


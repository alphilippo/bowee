#!/bin/python

import sys
import os.path
from subprocess import call
import pdb

import argparse

__PROJECT_DIR__ = os.getcwd()

__DIRS__ = ['templates','static_files']

__OPTIONS__ = ['project','syncdb','run']

def get_auto_model():
    auto = '''import peewee
#import db_driver
    
#Example with Sqlite database
#database = peewee.SqliteDatabase('sample.db',check_same_thread=False)
    
def create_tables():
    \'''code such as : ModelName.create_table()\'''
    
class BaseModel(peewee.Model):
    class Meta:
        database = database

if __name__ == '__main__':
    create_tables()
    
'''
    return auto

def get_auto_view():
    auto = '''from bottle import run , debug , route
from bottle import request , response , redirect , template
import models
import peewee

#create your views

@route('/')
@route('/index')
def index():
    return "Hello World !!!"

'''
    return auto

__PROJECT_FILES__ = [
    ('views.py',get_auto_view()),
    ('models.py',get_auto_model()),
    ('__init__.py',''),]

#PROJECT BUILDER
        
def create_project_dir(name):
    '''Create project directory
    '''
    os.mkdir(os.path.join(__PROJECT_DIR__,name))
    return os.path.join(__PROJECT_DIR__,name)

def generate_files(name):
    '''Generates project files
        -views.py
        -models.py
    '''
    print "Generating project files"
    for filename in __PROJECT_FILES__ :
        fname = os.path.join(name,filename[0])
        with open(fname,'w+') as f :
            f.write(filename[1])
            f.close()
    return True

def create_template_dir(name):
    '''Creates sub-directory
        -templates
        -static_files
    '''
    for directory in __DIRS__ :
        os.mkdir(os.path.join(name,directory))
    return True

#RUN SERVER

def run(name='views.py'):
    try :
        call(['python',name]) 
    except :
        pass
    
#ORM MANAGER
#Don't know if it is still working    
def syncdb(dbname=None):
    try :
        call(['python','models.py'])
        return "tables successfully created"
    except :
        pass
        
#ERROR HANDLER        

def args_error():
    print "Usage : "
    print "\t options : %s " %(__OPTIONS__,)
    return None

#MAIN
    
# def main(s=sys):

#     #print __PROJECT_DIR__
#     if len(s.argv) >= 2 and s.argv[1] =='project' :
#         try :
#             name = create_project_dir(s.argv[2])
#             project = generate_files(name)
#             template = create_template_dir(name)
#         except :
#             print "Usage : project projectname"
#     elif len(s.argv) == 2 and s.argv[1] == 'syncdb' :
#         print syncdb()
#     elif len(s.argv) >= 2 and s.argv[1] == 'run' :
#         if len(s.argv) == 2 :
#             run()
#         else:
#             run(s.argv[2])
#     else :
#         args_error()

def main():
    parser = argparse.ArgumentParser(description="Bottle project structure builder. Equivalent to django_admin.py")

    parser.add_argument('-p', '--project', action='store', help="Create project")
    parser.add_argument('-r', '--run', action='store', help="Launch server")
    parser.add_argument('-s', '--syncdb', action='store', help="Sync database")

    args = vars(parser.parse_args())

    print(args)

if __name__ == '__main__':
    main()


import sys
import os.path
from subprocess import call
import pdb

__PROJECT_DIR__ = os.getcwd()

__DIRS__ = [
    'templates',
    'static_files'
]

__OPTIONS__ = ['createproject','syncdb','run']

def get_auto_model():
    auto = '''import peewee
#import db_driver
    
#sample
#database = peewee.SqliteDatabase('sample.db',check_same_thread=False)
    
def create_tables():
    #code such as : ModelName.create_table()
    
class BaseModel(peewee.Model):
    class Meta:
        database = database
    
'''
    return auto

def get_auto_view():
    auto = '''from bottle import run , debug , route
from bottle import request , response , redirect , template
import peewee

#create your views 
'''
    return auto

__PROJECT_FILES__ = [
    ('views.py',get_auto_view()),
    ('models.py',get_auto_model()),
    ('__init__.py',''),]

#PROJECT BUILDER
        
def create_project_dir(name): 
    os.mkdir(os.path.join(__PROJECT_DIR__,name))
    return os.path.join(__PROJECT_DIR__,name)

    
def generate_files(name):
    print "Generating project files"
    for filename in __PROJECT_FILES__ :
        fname = os.path.join(name,filename[0])
        with open(fname,'w+') as f :
            f.write(filename[1])
            f.close()
    return True

def create_template_dir(name):
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
    
def syncdb(dbname=None):
    try :
        import models
        models.create_tables()
        return "tables successfully created"
    except ImportError :
        return "File models.py doesn't exist "

#ERROR HANDLER        

def args_error():
    print "Usage : "
    print "\t options : %s " %(__OPTIONS__,)
    print "\t python manage.py option [target]"
    return None

#MAIN
    
if __name__ == '__main__':
    #pdb.set_trace()
    if len(sys.argv) >= 2 and sys.argv[1] == 'createproject' :
        try :
            name = create_project_dir(sys.argv[2])
            project = generate_files(name)
            template = create_template_dir(name)
        except :
            print "Usage : createproject projectname"
    elif len(sys.argv) == 2 and sys.argv[1] == 'syncdb' :
        print syncdb()
    elif len(sys.argv) >= 2 and sys.argv[1] == 'run' :
        if len(sys.argv) == 2 :
            run()
        else:
            run(sys.argv[2])
    else :
        args_error()
        
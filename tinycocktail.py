import sys
import os.path

__PROJECT_DIR__ = os.getcwd()
__PROJECT_FILES__ = ['views.py','models.py']
__OPTIONS__ = ['createproject','syncdb']

def syncdb(dbname=None):
    try :
        import models
    
        models.create_tables()
        return "tables successfully created"
    except ImportError :
        return "File models.py doesn't exist "
        
def create_project_dir(name): 
    os.mkdir(os.path.join(__PROJECT_DIR__,name))
    return os.path.join(__PROJECT_DIR__,name)

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
    
def generate_files(name):
    print "Generating project files"
    for filename in __PROJECT_FILES__ :
        if filename == 'views.py' :
            filename = os.path.join(name,filename)
            f = open(filename,'w+')
            f.write(get_auto_view())
            f.close()
        else :
            filename = os.path.join(name,filename)
            f = open(filename,'w+')
            f.write(get_auto_model())
            f.close()
    return True

def create_template_dir(name):
    os.mkdir(os.path.join(name,'templates'))
    return os.path.join(name,'templates')
    
if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) > 2 :
        if sys.argv[1] == 'createproject':
            if sys.argv[1] :
                name = create_project_dir(sys.argv[2])
                #name = os.path.join(__PROJECT_DIR__,sys.argv[2])
                print name
                print __PROJECT_DIR__
                project = generate_files(name)
                template = create_template_dir(name)
            else :
                print "Usage : createproject projectname"
        else :
            print "Usage : "
            for opt in __OPTIONS__ :
                print "./manage.py %s " %(opt,)
    elif len(sys.argv) == 2 and sys.argv[1] == 'syncdb' :
        print syncdb()
    else :
        print "Usage : \n"
        for opt in __OPTIONS__ :
            print "./manage.py %s " %(opt,)

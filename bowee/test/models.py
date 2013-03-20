import peewee
#import db_driver
    
#Example with Sqlite database
#database = peewee.SqliteDatabase('sample.db',check_same_thread=False)
    
def create_tables():
    '''code such as : ModelName.create_table()'''
    
class BaseModel(peewee.Model):
    class Meta:
        database = database

if __name__ == '__main__'
    create_tables()
    

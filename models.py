from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os

database_name = "demodb"
username = "postgres"
password = 'skr123'
database_path = 'postgres://oumxopmevydvld:3387734dfedfb6ab1ccc9912db1f6f4089c80460bc8ca9ec7d91ac31052f5e16@ec2-52-71-55-81.compute-1.amazonaws.com:5432/deve3jnt51h5oi'

# database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)



'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(db.Integer, primary_key=True)
  name = Column(db.String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}
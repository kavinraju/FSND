import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgres://oumxopmevydvld:3387734dfedfb6ab1ccc9912db1f6f4089c80460bc8ca9ec7d91ac31052f5e16@ec2-52-71-55-81.compute-1.amazonaws.com:5432/deve3jnt51h5oi'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

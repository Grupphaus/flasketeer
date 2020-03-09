from flask import Flask

app = Flask(__name__)

''' Workaround for circular imports '''
''' The routes module needs to import the app variable defined in this script, 
    so putting one of the reciprocal imports at the bottom avoids the error that 
    results from the mutual references between these two files. '''
from app import routes
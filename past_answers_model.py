# the import section
from google.appengine.ext import ndb

class Answer_Tracker(ndb.Model):
    question =  ndb.StringProperty(required=True)
    answer =  ndb.StringProperty(required=True)

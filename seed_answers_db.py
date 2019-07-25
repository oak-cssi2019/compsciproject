# the import section
from past_answers_model import Answer_Tracker

def seed_data(q,a):
    track_key = Answer_Tracker(question=q, answer=a).put()

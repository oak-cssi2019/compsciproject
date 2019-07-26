
# the import section
import webapp2
import jinja2
import os
import random
from past_answers_model import Answer_Tracker
from seed_answers_db import seed_data

# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# the handler section
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/login.html')
        self.response.write(login_template.render())

class HomeHandler(webapp2.RequestHandler): #homepage "/"
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html') #pulls in "home.html" template
        self.response.write(home_template.render()) #serves home.html template back to front-end

    

class pastAnswersHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        # pastAnswers_template = the_jinja_env.get_template('templates/pastAnswers.html')
        # self.response.write(pastAnswers_template.render())


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        # below are the form results from the form on home.html
        results_Dict = {
          'name': self.request.get('user-first-name'), #stores form input named 'user-first-name' under key 'name' which is the same name as the placeholder on 'results.html'
          'feeling': self.request.get('user-feeling') #stores form input under 'user-feeling' under key 'feeling' which is the same name as the placeholder on 'results.html'
        }
        results_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(results_template.render(results_Dict)) #passes in results_Dict that will fill the placeholders on results.html

def errorMessage():

    errorArray = ["The database can't answer your question right now",
    "I must've been on break when I missed this",
    "error: 101",
    "Ask me a better question * yawn *",
    "Someone hasn't been treating their agent very well :/",
    "I think I lost your file on that"]
    randomError = random.choice(errorArray)
    return randomError

def ansPhrase():

    myPhrase = "FBI agent, check your records to answer us"
    testerString = "Cat and Dog"
    if "." in testerString:
        startIndexVal = testerString.find(".")
        endIndexVal = len(testerString) - 1
        savePortion = testerString[startIndexVal:endIndexVal]
        return savePortion

    else:
        return errorMessage()






# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/', LoginHandler),
  ('/home', HomeHandler),
  ('/about', AboutHandler),
  ('/pastAnswers',pastAnswersHandler)
  ], debug=True)

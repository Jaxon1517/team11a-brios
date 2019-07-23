# the import section
import webapp2
import jinja2
import os


Account = False
start = None
# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class Main(webapp2.RequestHandler):
  def get(self):  # for a get request
    self.response.write('I am sorry Jon')  # the response

if Account == True:
	start = 'Main'
# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ], debug=True)
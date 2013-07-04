import os
import webapp2
import jinja2

templates = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates),
    extensions=['jinja2.ext.autoescape'])



class BaseHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template(self.template)
        template_values = {
                'title': self.pageTitle,
                }
        self.response.write(template.render(template_values))
        return


class HomePage(BaseHandler):
    template = 'home.html'
    pageTitle = 'Phungsuk Jibabo'
    pageID = 'home'
    href = '/'
    navDisplay = 'Home'

def BuildGlobalRoutes():
    routes = [('/', HomePage)]
    return routes

GLOBAL_ROUTES = BuildGlobalRoutes()
application = webapp2.WSGIApplication(GLOBAL_ROUTES, debug=True)

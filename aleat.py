import webapp
import random

class aleatorio(webapp.app):
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hola(aleatorio)</h1><p><a href='/aleat/"+
                str(random.randint(0, 100000)) +"'>Dame Otra</a></p></body></html>")

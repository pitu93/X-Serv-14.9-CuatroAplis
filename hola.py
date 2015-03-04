import webapp

class hola(webapp.app):
    def parse(self, request, rest):
        opcion = request.split()[1][1:]
        return opcion

    def process(self, parsedRequest):
        if(parsedRequest=='hola'):
            return ("200 OK", "<html><body><h1>" +
                    "Hola" + "</h1></body></html>")
        elif(parsedRequest=='adios'):
            return ("200 OK", "<html><body><h1>" +
                    "Adios" + "</h1></body></html>")

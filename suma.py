import webapp

class suma(webapp.app):
    def parse(self, request, rest):
        sumandos = rest.split('/')[1:]
        return sumandos
    
    def process(self, parsedRequest):
        resultado= int(parsedRequest[0]) + int(parsedRequest[1])
        return ("200 OK", "<html><body><h1>" +
                str(resultado) + "</h1></body></html>")


import webapp
import suma
import hola
import aleat

if __name__ == "__main__":
    anApp = webapp.app()
    otherApp = webapp.app()
    hola = hola.hola()
    suma = suma.suma()
    aleatorio = aleat.aleatorio()
    testWebApp = webapp.webApp("localhost", 1234, {'/app': anApp,
                                            '/other': otherApp,
                                            '/hola': hola,
                                            '/adios': hola,
                                            '/suma':suma,
                                            '/aleat':aleatorio})

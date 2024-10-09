from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def health(request):
    return Response(status=200)


def hello_world(request):
    name = os.environ.get("NAME")
    if name == None or len(name) == 0:
        name = "different branch"
    message = "Good men, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = 8080
    with Configurator() as config:
        config.add_route('health', '/health')
        config.add_view(health, route_name='health')
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

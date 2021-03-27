from wsgiref.simple_server import make_server

def simple_application(environment, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
    ]

    start_response(status,headers)
    return ['<h1>Hello!</h1><p>This is WSGI application.</p>'.encode()]

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

with make_server(
    host=SERVER_HOST,
    port=SERVER_PORT,
    app=simple_application,
) as wsgi_server:
    print(f'Starting server on {SERVER_HOST}:{SERVER_PORT}.')
    wsgi_server.serve_forever()
    
##################

from wsgiref.simple_server import make_server


def simple_application(environ, start_response):
    status = '200 OK'
    response_body = '\n'.join([
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ])

    response_headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
    ]

    start_response(status, response_headers)
    return [response_body.encode()]

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

with make_server(
    host=SERVER_HOST,
    port=SERVER_PORT,
    app=simple_application
) as wsgi_server:
    print(f'Starting server on {SERVER_HOST}:{SERVER_PORT}.')
    wsgi_server.serve_forever()


##################

from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def simple_application(environ, start_response):

    query_string = environ["QUERY_STRING"]
    parameters = parse_qs(query_string)
    try:
        first_name = parameters["first_name"][0]
        last_name = parameters["last_name"][0]
        age = parameters["age"][0]
        response_content = f"<p>First Name:{first_name}</p><p>Last Name:{last_name}</p><p>Age:{age}</p>"
        status = "200 OK"
    except KeyError:
        response_content = f"<p> Invalid query string</p>"
        status = "400 Bad Request"

    response_headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
    ]

    start_response(status, response_headers)
    return [response_content.encode()]


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

with make_server(
    host=SERVER_HOST,
    port=SERVER_PORT,
    app=simple_application
) as wsgi_server:
    print(f'Starting server on {SERVER_HOST}:{SERVER_PORT}.')
    wsgi_server.serve_forever()


##################
##################

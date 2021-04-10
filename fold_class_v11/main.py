from urllib.parse import parse_qsl
from wsgiref.simple_server import make_server
import string
import student


# Template
def load_template(name):
    with open(name, 'r') as template:
        source = string.Template(template.read())
    return source


# Request/Reponse
class Request:
    def __init__(self, path, data):
        self.path = path
        self.data = data


class Response:
    def __init__(self, data):
        self.data = data

    def get_response_iter(self):
        yield self.data.encode()

    def __call__(self, start_response):
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        start_response(status, headers)
        return self.get_response_iter()


def read_request_body(environment):
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH',0))
    except ValueError:
        request_body_size = 0

    request_body = environment['wsgi.input'].read(request_body_size)
    return request_body.decode()


def parse_request_body(request_body):
    parsed = parse_qsl(request_body)
    return dict(parsed)


def load_request(environment):
    request_body = read_request_body(environment=environment)
    parsed_body = parse_request_body(request_body=request_body)
    request = Request(
        path=environment['PATH_INFO'],
        data=parsed_body,
    )
    return request


class Application:
    def __init__(self, routes):
        self.routes = routes
        self.request = None

    def __call__(self, environment, start_response):
        request = load_request(environment=environment)
        handler = self.routes[request.path]
        application_iterator = handler(request)
        return application_iterator(start_response)


# Routes
def index(request):
    #response = load_template('home.html')
    #return [response.substitute().encode()]
    return Response(data='<h1>Hello</h1>')


def latin(request):
    return Response(data='Lorem ipsum')

def student_grades(request):
    response = load_template('student.html')
    return Response(data=response.substitute())


def average(request):
    name = request.data['name']
    grades = [int(grade) for grade in request.data['grades'].split(',')]

    named_student = student.Student(
        name=name,
        grades=grades
    )
    student_average = named_student.average()

    return Response(
        data=named_student.generate_report(average=student_average),
    )


routes = {
    '/': index,
    '/student_grades': student_grades,
    '/average': average,
    '/favicon.ico': index,
}

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

application = Application(
    routes=routes
)

with make_server(
    host=SERVER_HOST,
    port=SERVER_PORT,
    app=application,
) as wsgi_server:
    print(f'Starting server on {SERVER_HOST}:{SERVER_PORT}.')
    wsgi_server.serve_forever()

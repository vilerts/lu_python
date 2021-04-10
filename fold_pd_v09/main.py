import string
from urllib.parse import parse_qsl
from wsgiref.simple_server import make_server


# Templates
def load_template(name):
    with open(name, 'r') as template:
        source = string.Template(template.read())

    return source


# Request/Response
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
        status_code = '200 OK'
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        start_response(status_code, headers)
        return self.get_response_iter()


def read_request_body(environment):
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH', 0))
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

    def __call__(self, environment, start_response):
        request = load_request(environment=environment)

        handler = self.routes[request.path]

        application_iterator = handler(request)

        return application_iterator(start_response)


def index(request):
    return Response(data='Empty, try /university')


def university(request):
    response = load_template('index.html')
    return Response(data=response.substitute())


def university_response(request):
    full_name = request.data['full_name']
    grade_math = int(request.data['grade_math'])
    grade_latvian = int(request.data['grade_latvian'])
    grade_foreign = int(request.data['grade_foreign'])

    # if cannot apply, will add "NOT" to text - otherwise (if can) empty
    can_apply_string = ''
    if grade_math < 80 or grade_latvian < 80 or grade_foreign < 80:
        can_apply_string = 'NOT '

    response_string = f'{full_name} can {can_apply_string} apply to university'

    return Response(
        data=response_string,
    )


routes = {
    '/': index,
    '/university': university,
    '/university_response': university_response,
    '/favicon.ico': index
}

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

application = Application(
    routes=routes,
)


with make_server(
    host=SERVER_HOST,
    port=SERVER_PORT,
    app=application,
) as wsgi_server:
    print(f'Starting server on {SERVER_HOST}:{SERVER_PORT}.')

    wsgi_server.serve_forever()
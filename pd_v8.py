from wsgiref.simple_server import make_server
import random


def get_random_quote():
    quotes = [
        "Love For All, Hatred For None.",
        "Change the world by being yourself.",
        "Every moment is a fresh beginning.",
        "Never regret anything that made you smile.",
        "Die with memories, not dreams.",
        "Aspire to inspire before we expire."
    ]
    return random.choice(quotes)


def simple_application(environ, start_response):
    status = "200 OK"
    response_content = f"<h1>{get_random_quote()}</h1>"
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

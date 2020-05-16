from http.server import BaseHTTPRequestHandler, HTTPServer
from host.application.http_request import HTTPRequest
from host.application.urls import urls
from host.application.settings import settings
from host.test.html_generator import HTMLGenerator
import json


class RouteHandler(BaseHTTPRequestHandler):
    def resolve_url(self):
        second_slash = self.path.find('/', 1)
        if second_slash == -1:
            app = self.path[1:]
        else:
            app = self.path[1: second_slash]
        for x in urls:
            if app == x:
                self.app = app
                response = urls[app](HTTPRequest(self))
                self.send(response)
                return
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            'error': 'Couldn\'t find path [{}]'.format(app),
        }).encode())

    def send(self, response):
        self.send_response(response.status)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        if response.headers['Content-type'] == 'application/json':
            self.wfile.write(json.dumps(response.data).encode())
        elif response.headers['Content-type'] == 'text/html':
            self.wfile.write(response.data)

    def do_GET(self):
        self.resolve_url()

    def do_POST(self):
        self.resolve_url()


def run():
    httpd = HTTPServer(('', settings['PORT']), RouteHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n')
        httpd.server_close()


if __name__ == '__main__':
    run()

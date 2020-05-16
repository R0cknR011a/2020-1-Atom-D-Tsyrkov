class HTTPRequest:
    def __init__(self, request):
        self.host, self.port = request.client_address
        self.method = request.command
        self.path = request.path
        self.version = request.request_version

        start = self.path.find('?', len(request.app))
        if '?' in request.path:
            data = request.path.split('?')[1]
            self.GET = self.parse_query_string(data)
        else:
            self.GET = {}

        length = request.headers['Content-Length']
        if not length is None:
            data = request.rfile.read(int(length)).decode()
            self.POST = self.parse_query_string(data)
        else:
            self.POST = {}


    def parse_query_string(self, string):
        result = {}
        for bundle in string.split('&'):
            tmp = bundle.split('=')
            key, value = tmp[0], tmp[1]
            result[key] = value
        return result

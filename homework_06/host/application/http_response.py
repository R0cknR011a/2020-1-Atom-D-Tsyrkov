class HTTPResponse:
    def __init__(self, data, error_code=None):
        self.data = data
        if error_code is None:
            self.status = 200
        else:
            self.status = error_code
        if isinstance(self.data, dict):
            self.headers = {'Content-type': 'application/json'}
        elif isinstance(self.data, str):
            self.data = self.data.encode()
            self.headers = {'Content-type': 'text/html'}

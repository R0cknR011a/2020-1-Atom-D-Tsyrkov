from host.application.http_response import HTTPResponse


def check_connection(request):
    return HTTPResponse({'status': 'OK'})

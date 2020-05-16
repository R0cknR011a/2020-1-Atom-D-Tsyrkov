from host.url_parser.view import parse_url
from host.application.view import check_connection


urls = {
    'check': check_connection,
    'parser': parse_url,
}

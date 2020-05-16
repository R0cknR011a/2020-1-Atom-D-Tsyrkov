import requests
from settings import settings


def start():
    try:
        PORT = settings['PORT']
        HOST = settings['HOST']
        path = settings['path']
        response = requests.get('http://{}:{}/check'.format(HOST, PORT)).json()
        print('Connection status: ' + response['status'])
        while True:
            request = input('Enter URL: ')
            response = requests.get('http://{}:{}/{}/?url={}&k=10'.format(HOST, PORT, path, request))
            data = response.json()
            if response.status_code == 200:
                for key, value in data['result'].items():
                    print('           {} : {}'.format(key, value))
            else:
                print('Server error: {}'.format(data['error']))
    except requests.exceptions.ConnectionError:
        print('Host isn\'t responding, please check your client settings')
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    start()

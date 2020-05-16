from host.application.http_response import HTTPResponse
import requests
import string
from bs4 import BeautifulSoup


def parse_url(request):
    if request.method == 'GET':
        try:
            if 'url' in request.GET and 'k' in request.GET:
                url = request.GET['url']
                k = request.GET['k']
                try:
                    k = int(k)
                except ValueError:
                    if k == 'all':
                        k = 'all'
                    else:
                        return HTTPResponse({'error': 'Input K parametr is NOT [int] instance'})
                response = requests.get(url).text
                soup = BeautifulSoup(response, features='html.parser')
                for script in soup(['script', 'style']):
                    script.extract()
                text = soup.get_text()
                result = get_most_frequent_words(text, k)
                return HTTPResponse({'result': result})
            else:
                return HTTPResponse({'error': 'Couldn\'t find URL or K parameter in request'}, error_code=400)
        except requests.exceptions.MissingSchema:
            return HTTPResponse({'error': 'Provided URL [{}] is invalid'.format(url)}, error_code=400)
        except requests.exceptions.ConnectionError:
            return HTTPResponse({'error': 'Couldn\'t connect to URL [{}]'.format(url)}, error_code=400)
    return HTTPResponse({'error': 'Method not allowed'}, error_code=403)


def get_most_frequent_words(text, k):
    hashmap = {}
    word = ''
    length = len(text)
    for i in range(length):
        if text[i] in string.ascii_letters:
            word += text[i]
            if i == length - 1:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 0
        elif word != '':
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 0
            word = ''

    if k == 'all':
        return hashmap

    length = 0
    for key in hashmap:
        if hashmap[key] > length:
            length = hashmap[key]
    sorted_map = [None] * (length + 1)
    for word, freq in hashmap.items():
        if sorted_map[freq] is None:
            sorted_map[freq] = [word]
        else:
            sorted_map[freq].append(word)

    result = {}
    for i in range(length, -1, -1):
        if sorted_map[i] is None:
            continue
        for j in range(len(sorted_map[i]) - 1, -1, -1):
            result[sorted_map[i][j]] = i
            if len(result) == k:
                return result

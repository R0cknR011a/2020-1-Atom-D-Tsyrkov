from homework_02.LFU_cache import LFUCache
import pytest
import string


def test_set_get():
    cache = LFUCache(5)
    cache.set('a', 'one')
    cache.set('b', 'two')
    cache.set('c', 'three')
    cache.set('d', 'four')
    cache.set('e', 'five')
    assert cache.get('a') == 'one'
    assert cache.get('e') == 'five'

    cache.set('a', 'one one')
    cache.set('a', 'one one one')
    cache.set('e', 'five five')
    assert cache.get('e') == 'five five'
    assert cache.get('a') == 'one one one'


def test_overload():
    cache = LFUCache()
    for x in string.ascii_lowercase[:10]:
        cache.set(x, x.upper())
    for x in range(10):
        for i in range(x):
            cache.get(string.ascii_lowercase[x])

    cache.set('k', 'K')
    with pytest.raises(KeyError):
        cache.get('a')
    for _ in range(3):
        cache.get('k')

    cache.set('l', 'L')
    with pytest.raises(KeyError):
        cache.get('b')
    for _ in range(3):
        cache.get('l')

    cache.set('m', 'M')
    with pytest.raises(KeyError):
        cache.get('c')
    for _ in range(3):
        cache.get('m')

    cache.set('n', 'N')
    with pytest.raises(KeyError):
        cache.get('d')
    for _ in range(3):
        cache.get('n')

    cache.set('k', 'smth')
    cache.set('o', 'O')
    assert cache.get('k') == 'smth'
    with pytest.raises(KeyError):
        cache.get('l')


def test_delete():
    cache = LFUCache()
    for x in string.ascii_lowercase[:10]:
        cache.set(x, x.upper())
    for x in range(10):
        for i in range(x):
            cache.get(string.ascii_lowercase[x])

    cache.delete('a')
    assert cache.get('a') == ''

    cache.set('b', 'X')
    cache.set('z', 'Z')
    with pytest.raises(KeyError):
        cache.get('a')

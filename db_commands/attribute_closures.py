
def trivials(attrs: str) -> None:
    for attr in attrs.split(', '):
        print('{' + attr + '}⁺ = {' + attr + '}')


def superkey(keys: str, attrs: str) -> None:
    if attrs:
        print('{' + keys + '}⁺ = {' + keys + ', ' + attrs + '}')
    else:
        print('{' + keys + '}⁺ = {' + keys + '}')


def attr_closure(name: str, keys: str, attrs: str) -> None:
    print(name)
    if attrs:
        trivials(keys + ', ' + attrs)
        superkey(keys, attrs)
    else:
        trivials(keys)
    if keys.find(',') != -1:
        print('superkey = (' + keys + ')')
    else:
        print('superkey = ' + keys)


if __name__ == '__main__':
    n = 'election'
    k = 'district, congress_number'
    a = 'votes_for, total_votes'
    attr_closure(n, k, a)

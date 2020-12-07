def recursive_search(dct, target, path=None):
    if path is None:
        path = []
    if target in dct.values():
        out = ' '.join(path) + ' ' + ' '.join(f'{key}:{value}' for key, value in dct.items())
        yield out
    else:
        for key, value in dct.items():
            if isinstance(value, dict):
                yield from recursive_search(value, target, path+[str(key)])

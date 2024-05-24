import orjson


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()

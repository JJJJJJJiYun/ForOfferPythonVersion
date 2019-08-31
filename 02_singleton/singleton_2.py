# -*- encoding: utf-8 -*-


# 使用装饰器
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class Singleton(object):
    val = 123

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    s = Singleton("hjy")
    t = Singleton("ljy")
    print s.val, t.val
    print s.name, t.name
    print s is t

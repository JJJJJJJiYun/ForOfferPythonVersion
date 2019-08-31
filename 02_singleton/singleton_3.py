# -*- encoding: utf-8 -*-

import threading


# 使用 __new__
# 类创建的过程是先调用 __new__ 方法创建实例，然后调用 __init__ 方法初始化参数
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

# -*- encoding: utf-8 -*-


# 使用模块，模块在第一次被导入时会生成 .pyc 文件，第二次导入会直接加载 .pyc 文件
class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()

# -*- encoding: utf-8 -*-


def replace_places(string=""):
    return string.replace(" ", "%20")


if __name__ == '__main__':
    print replace_places("i am a student")

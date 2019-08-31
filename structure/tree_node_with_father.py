# -*- encoding: utf-8 -*-


class TreeNodeWithFather(object):
    def __init__(self, val, left=None, right=None, father=None):
        self.val = val
        self.left = left
        self.right = right
        self.father = father

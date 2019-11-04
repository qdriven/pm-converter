# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     supplement
   Description :
   Author :        patrick
   date：          2019/11/1
-------------------------------------------------
   Change Activity:
                   2019/11/1:
-------------------------------------------------
"""
import re

from requests.structures import CaseInsensitiveDict

__author__ = 'patrick'


class QCaseInsensitiveDict(CaseInsensitiveDict):
    def __init__(self, data=None, **kwargs):
        super(QCaseInsensitiveDict, self).__init__(data, **kwargs)


def normalize_class_name(string: str) -> str:
    string = re.sub(r'[?!@#$%^&*()_\-+=,./\'\\\"|:;{}\[\]]', ' ', string)
    return string.title().replace(' ', '')


def normalize_func_name(string: str) -> str:
    string = re.sub(r'[?!@#$%^&*()_\-+=,./\'\\\"|:;{}\[\]]', ' ', string)
    return '_'.join(string.lower().split())

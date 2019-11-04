# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :        patrick
   date：          2019/11/1
-------------------------------------------------
   Change Activity:
                   2019/11/1:
-------------------------------------------------
"""
import json

__author__ = 'patrick'


def extract_dict_from_raw_mode_data(raw):
    try:
        return json.loads(raw)
    except json.decoder.JSONDecodeError:
        return {}


def extract_dict_from_raw_headers(raw):
    d = {}
    for header in raw.split('\n'):
        try:
            key, value = header.split(': ')
            d[key] = value
        except ValueError:
            continue

    return d


def format_object(o, key_values):
    if isinstance(o, str):
        try:
            return o.replace('{{', '{').replace('}}', '}').format(**key_values)
        except KeyError as e:
            raise KeyError(
                "Except value %s in PostPython environment variables.\n Environment variables are %s" % (e, key_values))
    elif isinstance(o, dict):
        return format_dict(o, key_values)
    elif isinstance(o, list):
        return [format_object(oo, key_values) for oo in o]


def format_dict(d, key_values):
    kwargs = {}
    for k, v in d.items():
        kwargs[k] = format_object(v, key_values)
    return kwargs

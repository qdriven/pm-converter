# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     core
   Description :
   Author :        patrick
   date：          2019/11/1
-------------------------------------------------
   Change Activity:
                   2019/11/1:
-------------------------------------------------
"""
import difflib
import json
from copy import copy
from string import Template

import requests

from postman import extract_dict_from_raw_mode_data, extract_dict_from_raw_headers, format_object
from util.supplement import QCaseInsensitiveDict, normalize_class_name

__author__ = 'patrick'


class PostmanCollections:
    """
    ToDo: Get Folder as TestSuite
    ToDo: Run Test Suite In a Row
    ToDo: PostMan Logging
    """

    def __init__(self, postman_collection_path):
        with open(postman_collection_path, encoding='utf-8') as postman_collection_file:
            self.__postman_collection = json.load(postman_collection_file)

        self.__folders = QCaseInsensitiveDict()
        self.env = QCaseInsensitiveDict()
        self.__postman_info = QCaseInsensitiveDict()
        self.__requests = QCaseInsensitiveDict()
        self.__load()

    def get_all_requests(self):
        return self.__requests

    def __load(self):
        self.__postman_info = self.__postman_collection["info"]
        self.__items = self.__postman_collection['item']
        for item in self.__items:
            if item.get('item', "") == "":
                self.__requests[normalize_class_name(item['name'])] = item['request']
            else:
                self.__parse_request(item["item"], self.__requests)

    def __parse_request(self, items, container):
        for item in items:
            if item.get("item", "") == "":
                container[normalize_class_name(item["name"])] = item["request"]
            else:
                self.__parse_request(item["item"], container)

    def __getattr__(self, item):
        if item in self.__requests:
            return self.__requests[item]
        else:
            all_reqs = list(self.__requests.keys())
            similar_names = difflib.get_close_matches(item, all_reqs)
            if len(similar_names) > 0:
                similar = similar_names[0]
                raise AttributeError('%s folder does not exist in Postman collection.\n'
                                     'Did you mean %s?' % (item, similar))
            else:
                raise AttributeError('%s folder does not exist in Postman collection.\n'
                                     'Your choices are: %s' % (item, ", ".join(similar_names)))

    def run(self, item, **kwargs):
        new_env = copy(self.env)
        new_env.update(kwargs)
        request_kwargs = dict()
        data = self.__getattr__(item)
        request_kwargs['url'] = data['url']
        if data['dataMode'] == 'raw' and 'rawModeData' in data:
            self.request_kwargs['json'] = extract_dict_from_raw_mode_data(data['rawModeData'])
        request_kwargs['headers'] = extract_dict_from_raw_headers(data['headers'])
        request_kwargs['method'] = data['method']
        formatted_kwargs = format_object(self.request_kwargs, new_env)
        return requests.request(**formatted_kwargs)

    def convert_to(self):
        runner_api_template = Template("""class $name(HttpClient):
                                    method = "$method"
                                    req_url = "$req_url"
                                    req_body= $req_body
                                    """)

        for name, request in self.__requests.items():
            req_body = ""
            if request.get("body", "") != "":
                req_body = request.get("body").get("raw")
            req_url = request.get("url")
            if isinstance(req_url, dict):
                req_url = "/".join(req_url["path"])

            context_data = {
                "name": name,
                "method": request['method'],
                "req_body": req_body,
                "req_url": req_url
            }
            sample_code = runner_api_template.substitute(context_data)
            print(sample_code)


class PostmanRequest:
    def __init__(self):
        pass

if __name__ == '__main__':
    loader = PostmanCollections("../OPERATING-SERVICE.json")
    print(loader)
    print(loader.convert_to())

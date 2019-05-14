#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
import json


class MwrClient:

    def __init__(self, endpoint='mwr', host='localhost', port=6495, is_https=False):
        scheme = 'https://' if is_https else 'http://'
        self.url = '{0}{1}:{2}/{3}/'.format(scheme, host, port, endpoint)

    def __getattr__(self, item):
        def f(*args):
            req = request.Request(self.url + item)
            req.add_header('MWR_VER', '0.1.0')
            req.add_header('CONTENT_TYPE', 'application/json')
            data = json.JSONEncoder().encode({'param': list(args)})
            with request.urlopen(req, data=data.encode('utf-8')) as rf:
                rep = rf.read().decode('utf-8')
                response = json.JSONDecoder().decode(rep)
                if 'result' in response:
                    return response['result']
                else:
                    print(response['err'])
                    return None

        return f


class MwrServer:

    def __init__(self, host='localhost', port=6495):
        self.__host__ = host
        self.__port__ = port
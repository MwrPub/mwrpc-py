#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import json
from wsgiref.simple_server import make_server


class MwrClient:

    def __init__(self, endpoint='mwr', host='localhost', port=6495):
        self.__host__ = host
        self.__port__ = port
        self.__endpoint__ = endpoint

    def __getattr__(self, item):
        def f(*args):
            conn = http.client.HTTPConnection(self.__host__, self.__port__)
            headers = {'Content-Type': "application/json", 'MWR_VER': "0.1.4"}
            data = json.JSONEncoder().encode({'param': list(args)})
            conn.request("POST", "/{0}/{1}".format(self.__endpoint__, item), data, headers)
            rep = conn.getresponse().read().decode('utf-8')
            response = json.JSONDecoder().decode(rep)
            if 'result' in response:
                return response['result']
            else:
                print(response['err'])
                return None

        return f


class MwrServer:
    __rules__ = []

    def __init__(self, host='localhost', port=6495):
        self.__host__ = host
        self.__port__ = port

    def func(self, endpoint='mwr', alias=None):
        def decorate(f):
            name = f.__name__ if alias is None else alias
            self.__rules__.append({'endpoint': endpoint, 'name': name, 'func': f})
            return f

        return decorate

    def run(self):
        h = make_server(self.__host__, self.__port__, self.handler)
        t = '''MWR 0.1.4
Serving MWR on {0}:{1}
(Press CTRL+C to quit)'''
        print(t.format(self.__host__, self.__port__))
        h.serve_forever()

    def handler(self, environ, start_response):
        url_array = environ['PATH_INFO'].split('/')
        start_response('200 OK', [('Content-Type', 'application/json')])
        for rule in self.__rules__:
            if rule['endpoint'] == url_array[1] and rule['name'] == url_array[2]:
                try:
                    content_length = int(environ['CONTENT_LENGTH'])
                except ValueError:
                    content_length = 0
                request_body = environ['wsgi.input'].read(content_length)
                request_info = json.JSONDecoder().decode(request_body.decode('utf-8'))
                args = request_info['param']
                result = rule['func'](*args)
                resp = json.JSONEncoder().encode({'result': result})
                return [resp.encode('utf-8')]
        return ['{"code":-1,"err":"method not exists"}'.encode('utf-8')]
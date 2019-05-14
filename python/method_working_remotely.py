#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import json
from wsgiref.simple_server import make_server


class MwrClient:
    __host__ = ''
    __port__ = 0
    __endpoint__ = ''

    def __init__(self, endpoint='mwr', host='localhost', port=6495):
        self.__host__ = host
        self.__port__ = port
        self.__endpoint__ = endpoint

    def __getattr__(self, item):
        def f(*args):
            conn = http.client.HTTPConnection(self.__host__, self.__port__)
            headers = {'Content-Type': "application/json", 'MWR_VER': "0.1.2"}
            data = json.JSONEncoder().encode({'param': list(args)})
            conn.request("POST", "/{0}/{1}".format(self.__endpoint__, item), data, headers)
            res = conn.getresponse()
            rep = res.read().decode('utf-8')
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
        httpd = make_server(self.__host__, self.__port__, self.handler)
        print("Method Working Remotely 0.1.2")
        print("Serving Mwr Server on port {0}...".format(self.__port__))
        print("Running on http://{0}:{1}/ (Press CTRL+C to quit)".format(self.__host__, self.__port__))
        httpd.serve_forever()

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

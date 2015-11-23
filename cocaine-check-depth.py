#!/usr/bin/env python

from tornado import gen
from tornado import ioloop

from cocaine.services import Service

ENDPOINTS = [("localhost", 10053)]

@gen.coroutine
def main():
    node = Service("node", endpoints=ENDPOINTS)
    chan = yield node.list()
    app_list = yield chan.rx.get()
    for name in app_list:    
        app = Service(name, endpoints=ENDPOINTS)
        chan = yield app.info()
        info = yield chan.rx.get()
        if info["queue"]["depth"] == info["queue"]["capacity"]:
            print name

ioloop.IOLoop.current().run_sync(main, timeout=30)


#!/usr/bin/env python

from tornado import gen
from tornado import ioloop

from cocaine.services import Service

ENDPOINTS = [("localhost", 10053)]

@gen.coroutine
def main():
    chrono = Service("chrono", endpoints=ENDPOINTS)
    chan = yield chrono.notify_after(0.1)
    try:
        id = yield chan.rx.get()
        try:
            yield chan.rx.get()
        except:
            print "2; error while read notify on notify_after method"
            exit(1)
    except:
        print "2; error while read id on notify_after method"
        exit(1)
    try:
        yield chrono.cancel(id)
    except:
        print "2; error while close id on notify_after method"
        exit(1)
    chan = yield chrono.notify_every(0.1)
    try:
        id = yield chan.rx.get()
        try:
            yield chan.rx.get()
        except:
            print "2; error while read notify on notify_every method"
            exit(1)
    except:
        print "2; error while read id on notify_every method"
        exit(1)
    try:
        yield chrono.restart(id)
    except:
        print "2; error while restart id on notify_every method"
        exit(1)
    try:
        yield chrono.cancel(id)
    except:
        print "2; error while close id on notify_every method"
        exit(1)
    print "0;Ok"

ioloop.IOLoop.current().run_sync(main, timeout=30)


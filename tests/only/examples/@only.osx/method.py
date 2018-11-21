#!/usr/bin/env python
import sys
import only


class CLS(object):

    @only.osx
    def method(self):
        print("hello world")

if "darwin" in sys.platform:  # linux,linux2,win32,cygwin,darwin
    CLS().method()  # no exception
else:
    try:
        CLS().method()
    except OSError as e:
        print("%s: %s" % (type(e), str(e)))

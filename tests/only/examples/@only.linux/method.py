#!/usr/bin/env python
import sys
import only


class CLS(object):

    @only.linux
    def method(self):
        print("hello world")

if "linux" in sys.platform:  # linux,linux2,win32,cygwin,darwin
    CLS().method()  # nothing
else:
    try:
        CLS().method()
    except OSError as e:
        print("%s: %s" % (type(e), str(e)))

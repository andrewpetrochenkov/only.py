#!/usr/bin/env python
import sys
import only


class CLS(object):

    @only.windows
    def method(self):
        print("hello world")

if "win" in sys.platform:  # linux,win32,cygwin,darwin
    CLS().method()  # no exception
else:
    try:
        CLS().method()
    except OSError:
        pass

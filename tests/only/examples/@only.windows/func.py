#!/usr/bin/env python
import sys
import only


@only.windows
def func():
    print("hello world")

if sys.platform == "win32":  # linux,win32,cygwin,darwin
    func()  # no exception
else:
    try:
        func()
    except OSError as e:
        print("%s: %s" % (type(e), str(e)))

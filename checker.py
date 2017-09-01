import pycurl
from StringIO import StringIO

for line in open('sites.txt').xreadlines():
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, line.rstrip())
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    print line + "    status code: %s" % c.getinfo(pycurl.HTTP_CODE)
    c.close()
   # Body is a string in some encoding.
   # In Python 2, we can print it without knowing what the encoding is.

import httplib
import pudb
pudb.set_trace()
conn = httplib.HTTPConnection("www.python.org")
conn.request("GET","/index.html")
res = conn.getresponse()
print res.getheaders()
print res.getheader('server')
print res.getheader('space','mine')

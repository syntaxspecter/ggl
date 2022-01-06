#!C:\Python27\python.exe

import urllib
import urllib2
user='BRIJESH'
key='8620e45a26XX'
senderid='SPILKO'
accusage='1'
def sendsms(mobile,message):
 data={'user':user,'key':key,'mobile':mobile,'message':message,'senderid':senderid,'accusage':accusage}
 url='http://sms.bulkssms.com/submitsms.jsp?'
 postdata=urllib.urlencode(data)
 request=urllib2.Request(url,postdata)
 response=urllib2.urlopen(request)
 output=response.read()
 
 
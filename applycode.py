#!C:\Python27\python.exe

import os
import Cookie
import MySQLdb
import cgi,cgitb
print "Content-type:text/html\n\n"
if 'HTTP_COOKIE' in os.environ:
 cookie_string=os.environ.get('HTTP_COOKIE')
 c=Cookie.SimpleCookie()
 c.load(cookie_string)
 try:
  name=c['userid'].value
 except KeyError:
  print "<h3>cookie is expired or not set</h3>"
data=cgi.FieldStorage()
refname=data.getvalue('refno')
tanname=data.getvalue('tanname')
cost=data.getvalue('cost')
proposaldoc=data.getvalue('filename')
username=name
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query="select compname,conperson from registration where username='"+username+"'"
cur.execute(query)
res=cur.fetchone()
compname=res[0]
conperson=res[1]
query1="insert into proposal values ('"+refname+"','"+tanname+"','"+cost+"','"+proposaldoc+"','"+conperson+"','"+compname+"')"
cur.execute(query1)
con.commit()
con.close()
if proposaldoc.filename:
 fn=os.path.basename(proposaldoc.filename)
 open('upload/'+fn,'wb').write(proposaldoc.fileread())
 print "proposal is uploaded"
else:
 print "proposal is not uploaded"
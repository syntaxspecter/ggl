#!C:\Python27\python.exe
import cgi
import MySQLdb
import os
import Cookie
print "Content-Type:text/html\n\n"
if 'HTTP_COOKIE' in os.environ:
 cookie_string=os.environ.get('HTTP_COOKIE')
 c=Cookie.SimpleCookie()
 c.load(cookie_string)
 try:
  name=c['userid'].value
 except KeyError:
  print "<h3>cookie is expired or not set</h3>"
data=cgi.FieldStorage()
feedback=data.getvalue('feedback')
uname=name
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query="select conperson,conpconno,conpemail from registration where username='"+uname+"'"
cur.execute(query)
res=cur.fetchone()
conperson=res[0]
conpconno=res[1]
conpemail=res[2]
query1="insert into feedback(name,contactno,emailadd,feedback)values('"+conperson+"','"+conpconno+"','"+conpemail+"','"+feedback+"')"
cur.execute(query1)
print "<script>alert('your feedback is submitted');window.location.href='feedback.py'</script>"
con.commit()
con.close()

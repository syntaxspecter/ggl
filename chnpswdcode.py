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
userid=name
password=data.getvalue('password')
oldpassword=data.getvalue('passwordold')
userid1=name
password1=data.getvalue('password')
oldpassword1=data.getvalue('passwordold')
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query2="update login set passwd ='"+password+"' where username='"+userid+"' and passwd='"+oldpassword+"'"
cur.execute(query2)
query1="update registration set passwd ='"+password1+"' where username='"+userid1+"' and passwd='"+oldpassword1+"'"
cur.execute(query1)
con.commit()
con.close()
print "<script>alert('your password has been changed');window.location.href='chnpswd.py'</script>"


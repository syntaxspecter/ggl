#!C:\Python27\python.exe

import MySQLdb
import cgi
print "Content-type:text/html\n\n"
data=cgi.FieldStorage()
name=data.getvalue('name')
password=data.getvalue('password')
class login:
 con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
 cur=con.cursor()
 def validuser(self,name,password):
  self.name=name
  self.password=password
  query="select * from login where username='"+name+"' and passwd='"+password+"'"
  login.cur.execute(query)
  result=login.cur.fetchone()
  login.con.commit()
  login.con.close()
  if result is None:
   print "<script>alert('Wrong password or username');window.location.href='login.py';</script>"
  else:
   print "<script>window.location.href='vendorzone/vendorhome.py?name="+name+"';</script>"
lg=login()
lg.validuser(name,password)

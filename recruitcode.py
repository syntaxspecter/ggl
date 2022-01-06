#!C:\Python27\python.exe
import MySQLdb
import cgi

print "Content-type:text/html\n\n"
data=cgi.FieldStorage()
name=data.getvalue('name')
emailaddress=data.getvalue('emailaddress')
gender=data.getvalue('gender')
keyskills=data.getvalue('keyskills')
address=data.getvalue('address')
qualification=data.getvalue('qualification')
experience=data.getvalue('experience')
contactno=data.getvalue('contactno')
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query="insert into recruitment values('"+name+"','"+gender+"','"+qualification+"','"+experience+"','"+keyskills+"','"+contactno+"','"+emailaddress+"','"+address+"')"
cur.execute(query)
con.commit()
con.close()
print "<script>alert('Your recruitment form is submitted');window.location.href='recruitment.py';</script>"

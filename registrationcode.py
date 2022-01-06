#!C:\Python27\python.exe
import MySQLdb
import cgi
print "Content-type:text/html\n\n"
data=cgi.FieldStorage()
companyname=data.getvalue('companyname')
concernpersonemailadd=data.getvalue('concernpersonemailadd')
tinno=data.getvalue('tinno')
companyemailadd=data.getvalue('companyemailadd')
panno=data.getvalue('panno')
companyurl=data.getvalue('companyurl')
comptype=data.getvalue('comptype')
sector=data.getvalue('sector') 
country=data.getvalue('country')
address=data.getvalue('address')
aboutcompany=data.getvalue('aboutcompany')
estyear=data.getvalue('estyear')
name=data.getvalue('name')
chairperson=data.getvalue('chairperson')
password=data.getvalue('password')
concernperson=data.getvalue('concernperson')
concernpersoncntno=data.getvalue('concernpersoncntno')
usertype='vendor'
status='no'
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query1="insert into registration values('"+companyname+"','"+comptype+"','"+sector+"','"+tinno+"','"+panno+"','"+address+"','"+country+"','"+estyear+"','"+chairperson+"','"+concernperson+"','"+concernpersoncntno+"','"+concernpersonemailadd+"','"+companyemailadd+"','"+companyurl+"','"+aboutcompany+"','"+name+"','"+password+"')"
query2="insert into login values('"+name+"','"+password+"','"+usertype+"','"+status+"')"
cur.execute(query1)
cur.execute(query2)
con.commit()
con.close()
print "<script>alert('Your registration is successfull');window.location.href='registration.py';</script>"

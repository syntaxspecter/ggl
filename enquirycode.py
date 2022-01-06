#!C:\Python27\python.exe
import cgi
import MySQLdb
import smssender
print "Content-type:text/html\n\n"
data=cgi.FieldStorage()
name=data.getvalue('name')
gender=data.getvalue('gender')
address=data.getvalue('address')
contactno=data.getvalue('contactno')
emailaddress=data.getvalue('emailaddress')
message=data.getvalue('message')
con=MySQLdb.connect("127.0.0.1","root","","ggldb",3306)
cur=con.cursor()
query="insert into enquiry(name,gender,address,contactno,emailaddress,message)values('"+name+"','"+gender+"','"+address+"','"+contactno+"','"+emailaddress+"','"+message+"')"
cur.execute(query)
con.commit()
con.close()
smssender.sendsms(contactno,'Thanks for enquiry.We will contact you soon-GGLCRM')
print "<script>alert('Your enquiry is submitted');window.location.href='enquiry.py';</script>"
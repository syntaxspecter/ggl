#!C:\Python27\python.exe

print "Content-Type:text/html\n\n"
print"""
<html>
<head>
<script>
function logOut()
{
window.location.href="http://localhost:70/ggl/login.py?passwd=''";
}
</script>
<link href="css/vendorstyle.css" rel="stylesheet">
<title>Vendor Zone</title>
</head>
<body>
<form action="applycode.py" method="post" form enctype="multipart/form-data">
<div id="wrapper">
 <div id="header">
 <img src="images/headernew1.jpg" height="150px" width="1000px" style="border-radius:20px 20px 0px 0px"/>
 </div>
 <div id="menu">
 <ul>
	  <a href="vendorhome.py"><li>Home</li></a>
	  <a href="review.py"><li>Review</li></a>
	  <a href="download.py"><li>Download</li></a>
	  <a href="apply.py"><li>Apply</li></a>
	  <a href="feedback.py"><li>Feedback</li></a>
	  <a href="complain.py"><li>Complain</li></a>
	  <li>More...
	    <ul class="submenu">
	    <a href="chnpswd.py"><li>Change password</li></a>
	    <a onclick="logOut()"><li>Logout</li></a>
	    </ul>
	  </li>
	</ul>
 </div>
 <div id="main">
 <h2 class="formh">Apply for tendor</h2>
 <table id="t1">
 <center>
         <tr>
		  <td>Referance No:</td>
		  <td><input type="text" name="refno" class="text" required="true"/></td>		  
		 </tr>
		 <tr>
		  <td>Tendor Name:</td>
		  <td><input type="text" name="tanname" class="text" required="true"/></td> 
		 </tr>
		 <tr>
		  <td>Proposed cost:</td>
		  <td><input type="number" name="cost" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td>Upload Proposal:</td>
		  <td><input type="file" name="filename" class="text"/></td>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
         <td colspan='2'><center><input type="submit" value="submit" class="button"/></center></td>
		 </tr> </center>
 </table>
 </div>
 <div id="footer">
  <div id="lfooter">
  </div>
  <div id="rfooter">
  </div>
 </div>
</div>
</form>
</body>
</html>
"""
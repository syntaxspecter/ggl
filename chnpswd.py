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
<form action="chnpswdcode.py" method="post">
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
 <h2 class="formh">Change Password</h2>
 <table id="t1" align="center">
		 <tr>
		  <td><b>Enter current password:</b></td>
		  <td><input type="password" class="text" name="passwordold" placeholder="enter current password " required="true"/></td>
		 </tr>
		 <tr>
		  <td><b>Enter new password:</b></td>
		  <td><input type="password" name="password" class="text" placeholder="enter new password" required="true"/></td>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
         <td colspan='2'><center><input type="submit" value="change password" class="button"/></center></td>
		 </tr>
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
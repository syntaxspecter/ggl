#!C:\Python27\python.exe

import cgi
print """
<html>
 <head>
  <link href="css/generalstyle.css" rel="stylesheet"/>
  <script src="js/slider.js"></script>
  <title>Green Gas Limited</title>
 </head>
 <body onload="moveSlider()">
  
   <div id="wrapper">
    <div id="header">
	<img src="images/headernew1.jpg" height="200px" width="1000px" style="border-radius:20px 20px 0px 0px"/>
	</div>
	<div id="menu">
	<ul>
	  <a href="index.py"><li>Home</li></a>
	  <a href="services.py"><li>Services</li></a>
	  <a href="registration.py"><li>Registration</li></a>
	  <a href="recruitment.py"><li>Recruitment</li></a>
	  <a href="login.py"><li>Login</li></a>
	  <a href="enquiry.py"><li>Enquiry</li></a>
	</ul>
	</div>
	<div id="container1">
	  <div id="slide1">
	    <img src="images/LKO_S2.jpg" width="300" height="300"/>
	  </div>
	  <div id="slide2">
	    <img id="slide" width="400" height="300"/>
	  </div>
	  <div id="slide3">
	   <img src="images/Agra_S2.jpg"width="300" height="300"/>
	  </div>
	</div>
	<div id="container2">
	  <form action="logincode.py" method="post">
		<h1 class="formh">Login Page</h1>
	    <table id="t1" align="center">
		 <tr>
		  <td><b>Enter user id:</b></td>
		  <td><input type="text" class="text" name="name" placeholder="enter your name " required="true"/></td>
		 </tr>
		 <tr>
		  <td><b>Enter Your Password:</b></td>
		  <td><input type="password" name="password" class="text" placeholder="enter your password" required="true"/></td>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
         <td colspan='2'><center><input type="submit" value="login" class="button"/></center></td>
		 </tr>
		</table>
		</form>
	</div>
	<div id="footer">
	 <div class="subfooter"></div>
	 <div class="subfooter"></div>
	</div>
   </div>   
 </body>
</html>
"""
#!C:\Python27\python.exe

print "Content-type:text/html\n\n"
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
	  <form action="enquirycode.py" method="post">
		<h2 class="formh">Enquiry Form</h2>
		<center>
	    <table id="t1"align="center">
		 <tr>
		  <td>Enter your name:</td>
		  <td><input type="text" class="text" name="name" required="true" placeholder="enter your name here"/></td>
		 </tr>
		 <tr>
		  <td>Select Gender:</td>
		  <td class="textg" style="margin-left:100px;"><input type="radio" name="gender" value="male"/>Male</td>
		  <td class="textg"><input type="radio" name="gender" value="female"/>Female</td>
		 </tr>
		 <tr>
		  <td>Enter Your Address:</td>
		  <td><textarea name="address" class="text" required="true" placeholder="enter your address here"></textarea></td>
		 </tr>
 		 <tr>
		  <td>Enter Contact No.:</td>
		  <td><input type="text" name="contactno" class="text" placeholder="enter your contact no. here"/></td>
		 </tr>
		 <tr>
		  <td>Enter Email Address:</td>
		  <td><input type="text" name="emailaddress" class="text" placeholder="enter your email address here"/></td>
		 </tr>
		 <tr>
		  <td>Enter Message:</td>
		  <td><textarea name="message" class="text" placeholder="enter your message here"></textarea></td>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
         <td colspan='2'><center><input type="submit" value="submit" class="button"/></center></td>
		 </tr>
		</table>
		</center>
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
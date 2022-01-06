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
  <form action="registrationcode.py" method="post">
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
	  
	   
		<h1 class="formh">Registration Form</h1>
	   <center>
	   <table id="t1"align="center">
		 <tr>
		  <td>Company Name:</td>
		  <td><input type="text" class="text" name="companyname" required="true"/></td>		 
		 </tr>
		 <tr>
		  <td>TIN No.:</td>
		  <td><input type="number" class="text"name="tinno" required="true"/>
		  </td>		  
		 </tr>
		 <tr>
		  <td>PAN No.:</td>
		  <td><input type="number" class="text"name="panno" required="true"/>
		  </td>		  
		 </tr>
		  <tr>
		  <td>Company Type.:</td>
		  <td>
		  <select name="comptype" class="text" required="true">
		  <option>select</option>
		  <option>production</option>
		  <option>services</option>
		  </select>
		  </td>
		  </tr>
		  <tr>
		  <td>Sector:</td>
		  <td><select name="sector" class="text" required="true">
		  <option>select</option>
		  <option>public</option>
		  <option>private</option>
		  <option>joint</option>
		  </select></td>
		 </tr>
		 <tr>
		 <td>Country:</td>
		  <td><select name="country" class="text" required="true">
		  <option>select</option>
		  <option>India</option>
		  <option>U.S.A.</option>
		  <option>Israel</option>
		  </select></td>
		 </tr>
 		 <tr>
		  <td>Company Address:</td>
		  <td><input type="text" name="address" class="text" required="true"/></td>
		 </tr>
		 <tr>
		  <td>Establishment year:</td>
		  <td><input type="number" class="text"name="estyear" required="true"/>
		  </td>		  
		 </tr>
		 <tr>
		  <td>Chair Person:</td>
		  <td><input type="text" name="chairperson" class="text" required="true"/></td>		  
		 </tr>
		 <tr>
		  <td>Concern Person:</td>
		  <td><input type="text" name="concernperson" class="text" required="true"/></td> 
		 </tr>
		 <tr>
		  <td>Concern Person Cont. No.:</td>
		  <td><input type="number" name="concernpersoncntno" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td>Concern Person Email Id:</td>
		  <td><input type="email" name="concernpersonemailadd" class="text"/></td>
		 </tr>
		 <tr>
		 <td>Company Email Address:</td>
		  <td><input type="email" name="companyemailadd" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td>Company URL:</td>
		  <td><input type="text" name="companyurl" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td>About Company:</td>
		  <td><textarea name="aboutcompany" class="text"></textarea></td>
		 </tr>
		 <tr>
		 <td>User Id:</td>
		  <td><input type="text" name="name" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td>Password:</td>
		  <td><input type="password" name="password" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 <td> Confirm Password:</td>
		  <td><input type="password" name="password1" class="text" required="true"/></td>
		 </tr>
		 <tr>
		 </tr>
		 <tr>
         <td colspan='2'><center><input type="submit" value="submit" class="button" /></center></td>
		 </tr>
		</table>
		</center>
	  
	</div>
	<div id="footer">
	 <div class="subfooter"></div>
	 <div class="subfooter"></div>
	</div>
   </div>   
  </form>
 </body>
</html>
"""
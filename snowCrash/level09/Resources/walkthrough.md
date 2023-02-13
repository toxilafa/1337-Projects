
in this level we got:
--------------------------------
level09@SnowCrash:~$ ls
level09  token
--------------------------------

let's execute level09i with the token:
--------------------------------
level09@SnowCrash:~$ ./level09 token
tpmhr
--------------------------------

let's use if for flag:
--------------------------------
level09@SnowCrash:~$ su flag09
Password:
su: Authentication failure
--------------------------------

ofcourse it's not that easy but worth the try
so now let's work a bit with level09 to understand the behaviour
as they ask to not reverse or try anything

let's try some tests:
--------------------------------
level09@SnowCrash:~$ ./level09 123
135
level09@SnowCrash:~$ ./level09 abc
ace
level09@SnowCrash:~$ ./level09 aaa
abc
--------------------------------

just from those simple examples we can deduct the following :
aaa became abc  -----> a + 0, a + 1 = b, a + 2 = c and so on. 

so we assume that the token has the same modification so we need
to reverse it using a script. By substracting n in place of adding it.

using the script in resources of level09 that we created:
--------------------------------
level09@SnowCrash:~$ python /tmp/script.py token
f3iji1ju5yuevaus41q1afiuq
--------------------------------

let's try the token on the program:
--------------------------------
level09@SnowCrash:~$ python /tmp/script.py token
f3iji1ju5yuevaus41q1afiuq
--------------------------------

let's try this on flag:
--------------------------------
level09@SnowCrash:~$ su flag09
Password:
Don't forget to launch getflag !
--------------------------------

Good! now let's get our finale flag:
--------------------------------
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
flag09@SnowCrash:~$ su level10
Password:
level10@SnowCrash:~$
--------------------------------


FINALLY!! THE END

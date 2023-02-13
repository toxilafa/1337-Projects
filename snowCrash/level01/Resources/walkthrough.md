
after many tries we checked the password file
knowing that linux sore the passwords in a file in etc/passwd:
--------------------------------
level01@SnowCrash:~$ cat /etc/passwd
.
.
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
flag02:x:3002:3002::/home/flag/flag02:/bin/bash
folag03:x:3003:3003::/home/flag/flag03:/bin/bash
.
.
--------------------------------

we see that the only one that has a kind off some password is flag01
which is "42hDRfypTqqnw"

let's try it on flag to check:
--------------------------------
level01@SnowCrash:~$ su flag01
Password:
su: Authentication failure
--------------------------------

we tried dcode but it seems not working for this one
so we used john the ripper so maybe we can find a way to our flag

firstly we create a file to put our password in it:
--------------------------------
echo "42hDRfypTqqnw" > file
--------------------------------

then we pass it to john:
--------------------------------
> ./john l --show
?:abcdefg

1 password hash cracked, 0 left
--------------------------------

we got this password "abcdefg"
let's try it on flag:
--------------------------------
level01@SnowCrash:~$ su flag01
Password:
Don't forget to launch getflag !
--------------------------------

Good! lett's get now our finale flag:
--------------------------------
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
flag01@SnowCrash:~$ su level02
Password:
level02@SnowCrash:~$
--------------------------------


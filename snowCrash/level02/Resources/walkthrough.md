
in level02 we find for the first time a file to work with
and it's a pcap file which means we need wireshark

> we first secure copied the file outside the vm so we work with it:
--------------------------------
 > scp -P 4242 level02@10.11.100.253:/home/user/level02/level02.pcap .
--------------------------------

> then we opened the file to get some banch of tcp requests data
we use the |Follow > TCP Steam| to see the data in strings and we got this:
--------------------------------
..%..%..&..... ..#..'..$..&..... ..#..'..$.. .....#.....'........... .38400,38400....#.SodaCan:0....'..DISPLAY.SodaCan:0......xterm.........."........!........"..".....b........b....	B.
..............................1.......!.."......"......!..........."........"..".............	..
.....................
Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

..wwwbugs login: l.le.ev.ve.el.lX.X
..
Password: ft_wandr...NDRel.L0L
.
..
Login incorrect
wwwbugs login:
--------------------------------

> we got this password passed "ft_wandr...NDRel.L0L"
so let's try t pass it to flag:
--------------------------------
level02@SnowCrash:~$ su flag02
Password:
su: Authentication failure
--------------------------------

> so it's not the case. we need to work with this password
to find out the exact one
after searching we got curious about the "." in the password
so we went to wireshark changed the text from ascii to Hex Dump:
--------------------------------
000000B9  66                                                 f
000000BA  74                                                 t
000000BB  5f                                                 _
000000BC  77                                                 w
000000BD  61                                                 a
000000BE  6e                                                 n
000000BF  64                                                 d
000000C0  72                                                 r
000000C1  7f                                                 .
000000C2  7f                                                 .
000000C3  7f                                                 .
000000C4  4e                                                 N
000000C5  44                                                 D
000000C6  52                                                 R
000000C7  65                                                 e
000000C8  6c                                                 l
000000C9  7f                                                 .
000000CA  4c                                                 L
000000CB  30                                                 0
000000CC  4c                                                 L
000000CD  0d                                                 .
--------------------------------

> "." was 7f. and 7f is DELETE in ascii table
so we deducted that the password "ft_wandr...NDRel.L0L" has 3 DELETES
at first to become "ft_waNDRel.L0L" and 1 DELETE at the end 
so the finale password is "ft_waNDReL0L"

> now let's try with the flag:
--------------------------------
level02@SnowCrash:~$ su flag02
Password:
Don't forget to launch getflag !
--------------------------------

> Good! now let's get our finale flag:
--------------------------------
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
flag02@SnowCrash:~$ su level03
Password:
level03@SnowCrash:~$
--------------------------------


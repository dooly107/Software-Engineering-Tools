#! /bin/bash

#---------------------------------------
# $Author: ee364c15 $
# $Date: 2017-08-27 21:27:54 -0400 (Sun, 27 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
read -p "Enter a command: " comValue

while [ "$comValue" != "quit" ]
do
    if [ "$comValue" == "hello" ]
    then
        echo "Hello $USER"
    elif  [ "$comValue" == "whereami" ]
    then
        echo "$PWD"
    elif [ "$comValue" == "compile" ]
    then
        for i in *.c
        do
            if gcc -Wall -Werror "$i" -o "${i%.c}.o"
            then    
                echo "Compilation succeeded for: "$i""
            else
                echo "Compilation failed for: "$i""
            fi
        done
    else
        echo "unrecognized input"
    fi
    echo
    read -p "Enter a command: " comValue
done
echo "Goodbye"

exit 0


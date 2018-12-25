#! /bin/bash

#---------------------------------------
# $Author: ee364c15 $
# $Date: 2017-09-03 17:57:43 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
curdir=$(echo $('pwd'))
changedir=$(echo $('pwd')"/c-files")
exec 2> /dev/null
cd $changedir
for i in *.c
do
    if gcc -Wall -Werror $i
    then
        ./a.out > ${i%.c}.out
        echo "Compiling file ${i%.c}.c... Compilation succeeded."
    else
        echo "Compiling file ${i%.c}.c... Error: Compilation failed."
    fi
done 

for j in *.out
do
    cp $j $changedir $curdir
    rm $j
done

exit 0

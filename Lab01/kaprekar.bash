#! /bin/bash

#---------------------------------------
# $Author: ee364c15 $
# $Date: 2017-08-29 17:20:21 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
Num_Of_Param=$#
Param_Values=$@
if (( $Num_Of_Param == 0 ))
then
    echo "Usage: kaprekar.bash <non-negative integer>"
else
    for i in {1..$1}
    do
        nonNegint=$1
        square=$(($nonNegint*$nonNegint))
        if [[ $square -lt 10 ]]
        then
            leftInt=0
            rightInt=$i
            echo $rightInt
            echo $leftInt
        else
            count=${#square}
            ((mod=$count%2))
            ((divide=$count/2))
            ((leftcut=$divide+$mod-1))
            ((rightcut=$divide+$mod))
            leftInt=$(echo $square | cut -c 1-$leftcut)
            rightInt=$(echo $square | cut -c $rightcut-$count)
        fi
        ((retain=$leftInt+$rightInt))
        if [[ $retain -eq $i ]]
        then
            echo "$i, square=$square, $leftint+$rightInt=$retain"
        fi
    done
fi


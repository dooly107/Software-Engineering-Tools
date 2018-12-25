#! /bin/bash

#---------------------------------------
# $Author: ee364c15 $
# $Date: 2017-08-29 17:16:52 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
Num_Of_Param=$#
Param_Values=$@
if (( $Num_Of_Param == 0 ))
then
    echo "Usage: ehcek_permission.bash <input file/directory>"
else
    stringWhole=$(ls -ld $1)
    dirorfile=$(echo $stringWhole | cut -c 1)
    if [[ $dirorfile = "-" ]]
    then
        echo "$1 is an ordinary file"
    fi
    if [[ $dirorfile = "d" ]]
    then
        echo "$1 is a directory"
    fi
    echo
    echo "Owner Permissions:"
    echo
    if [[ $(echo $stringWhole | cut -c 2) = "r" ]]
    then
        echo "$1 is readable"
    else
        echo "$1 is not readable"
    fi
    if [[ $(echo $stringWhole | cut -c 3) = "w" ]]
    then
        echo "$1 is writable"
    else
        echo "$1 is not writable"
    fi
    if [[ $(echo $stringWhole | cut -c 4) = "x" ]]
    then
        echo "$1 is executable"
    else
        echo "$1 is not executable"
    fi
    
    echo
    echo "Group Permissions:"
    echo
    if [[ $(echo $stringWhole | cut -c 5) = "r" ]]
    then
        echo "$1 is readable"
    else
        echo "$1 is not readable"
    fi
    if [[ $(echo $stringWhole | cut -c 6) = "w" ]]
    then
        echo "$1 is writable"
    else
        echo "$1 is not writable"
    fi
    if [[ $(echo $stringWhole | cut -c 7) = "x" ]]
    then
        echo "$1 is executable"
    else
        echo "$1 is not executable"
    fi

    echo
    echo "Others Permissions:"
    echo
    if [[ $(echo $stringWhole | cut -c 8) = "r" ]]
    then
        echo "$1 is readable"
    else
        echo "$1 is not readable"
    fi
    if [[ $(echo $stringWhole | cut -c 9) = "w" ]]
    then
        echo "$1 is writable"
    else
        echo "$1 is not writable"
    fi
    if [[ $(echo $stringWhole | cut -c 10) = "x" ]]
    then
        echo "$1 is executable"
    else
        echo "$1 is not executable"
    fi
fi

exit 0


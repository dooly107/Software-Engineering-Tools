#! /bin/bash

# $Author: ee364c15 $
# $Date: 2017-09-05 17:08:54 -0400 (Tue, 05 Sep 2017) $

function array 
{
    # Fill out your answer here.
    Arr=(a.txt b.txt c.txt d.txt e.txt)
    (( randomvr=$RANDOM%5 ))
    head -n 9 ${Arr[$randomvr]} | tail -n 3
    return

}


#
# To test your function, you can call it below like this:
#
array
#

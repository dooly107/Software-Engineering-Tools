#! /bin/bash

#---------------------------------------
# $Author: ee364c15 $
# $Date: 2017-09-03 17:57:43 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
Num_Of_Param=$#
Param_Values=$@
if [[ $Num_Of_Param != 1 ]]
then
    echo "Usage: sort_logs.bash <input file>"
    exit 1
else
    if rm -f ${1%.c}.unsorted ${1%.c}.sorted
    then
        echo "Note: Removing existing file ${1%.c}.unsorted"
        echo "Note: Removing existing file ${1%.c}.sorted"
    else
        echo "Note: Could not remove file ${1%.c}.unsorted"
        echo "Note: Could not remove file ${1%.c}.sorted"
        exit 3
    fi
    checkpermission=$(ls -ld $1)
    checkread=$(echo $checkpermission | cut -c 2)
    if [[ $checkread != "r" ]]
    then
        echo "Error: $1 is not a readable file."
        exit 2
    else
        exec 3< $1
        words=$(wc -w $1)
        lines=$(wc -l $1)
        wordsCount=$(echo $words | cut -d " " -f 1)
        linesCount=$(echo $lines | cut -d " " -f 1)
        cols=$(($wordsCount/$linesCount))

        for ((i = 2; i <= $linesCount; i++))
        do
            read line <&3
            read names <$1
            nline=$(head -n $i $1 | tail -n 1)
            for ((j = 2; j <= $cols; j++))
            do
                machine_name=$(echo $names | cut -d " " -f $j)
                machine_time=$(echo $nline | cut -d " " -f 1)
                temperature=$(echo $nline | cut -d " " -f $j)
                echo "$machine_name $machine_time $temperature"
            done
        done > "${1%.c}.unsorted"

        echo "\n" | sort -k3,3nr -k1,1 ${1%.c}.unsorted | tr -s " " "," > ${1%.c}.sorted

        for ((i = 2; i <= $linesCount; i++))
        do
            read line <&3
            read names <$1
            nline=$(head -n $i $1 | tail -n 1)
            for ((j = 2; j <= $cols; j++))
            do
                machine_name=$(echo $names | cut -d " " -f $j)
                machine_time=$(echo $nline | cut -d " " -f 1)
                temperature=$(echo $nline | cut -d " " -f $j)
                echo "$machine_name,$machine_time,$temperature"
            done
        done > "${1%.c}.unsorted"
    fi
fi



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
    echo "Usage: process_logs.bash <input file>"
    exit 1
else
    checkpermission=$(ls -ld $1)
    checkrOwner=$(echo $checkpermission | cut -c 2)
    checkrGroup=$(echo $checkpermission | cut -c 5)
    checkrOther=$(echo $checkpermission | cut -c 8)
    if [[ $checkrOwner != "r" ]]
    then
        echo "Error: $1 is not a readable file"
        exit 2
    else
        exec 3< $1
        words=$(wc -w $1)
        lines=$(wc -l $1)
        wordsCount=$(echo $words | cut -d " " -f 1)
        linesCount=$(echo $lines | cut -d " " -f 1)
        cols=$(($wordsCount/$linesCount))
        colswotime=$(($cols - 1))
        evenorodd=$(($colswotime % 2))
        rowwoname=$(($linesCount - 1))
        medcol=$(($linesCount / 2))
        remcol=$(($linesCount % 2))

        for (( i = 1; i <= $linesCount; i++))
        do
            read line <&3
            sum=0

            for (( j = 2; j <= $cols; j++))
            do
                values=$(echo $line | cut -d " " -f $j)
                sum=$(($sum + $values))
            done
            
            ti=$(echo $line | cut -d " " -f 1)
            if [[ i -ge 2 ]]
            then
                averagedec=$(echo "scale=2 ; $sum/$colswotime" | bc)
                echo "Average temperature for time $ti was $averagedec C." 
                arr=$(echo $line | cut -d " " -f 2-$cols)
                sortarr=$(echo $(printf "%s\n" $arr | sort -n))
                if [[ $evenorodd -eq 0 ]]
                then
                    half=$(($colswotime / 2))
                    uphalf=$(($half + 1))
                    lowbound=$(echo $sortarr | cut -d " " -f $half)
                    highbound=$(echo $sortarr | cut -d " " -f $uphalf)
                    median=$(echo "scale=2 ; (($lowbound+$highbound)/2)" | bc)
                    echo "Median temperature for time $ti was $median C."
                    echo
                elif [[ $evenorodd -eq 1 ]]
                then
                    half=$((($colswotime / 2) + 1))
                    medianval=$(echo $sortarr | cut -d " " -f $half)
                    mediandec=$(echo "scale=2 ; $medianval" | bc)
                    echo "Median temperature for time $ti was $mediandec C."
                    echo
                fi
            fi
        done
        
        read names <$1
        sumcol=0
        lowhalfcol=$(($medcol + 1))
        uphalfcol=$(($medcol + 2))
        halfmedcol=$(($medcol + 1))
        for (( v = 1; v <= $colswotime; v++ ))
        do
            nameplace=$(($v + 1))
            name=$(echo $names | cut -d " " -f $nameplace)
            sumcol=0
            while read -r -a value
            do
                col=${value[$v]}
                if [[ $col -eq $col ]]
                then
                    sumcol=$(($sumcol + $col))
                fi
            done < $1
            machine_average=$(echo "scale=2; (($sumcol/$rowwoname))" | bc)
            echo "Average temperature for $name was $machine_average C."
            
            while read -r -a value
            do
                if [[ ${value[$v]} -eq ${value[$v]} ]]
                then
                    column[$v]+="${value[$v]}"$'\n'
                fi
                sortcol[$v]=$(echo $(printf "%s\n" ${column[$v]} | sort -n))
                if [[ $remcol -eq 1 ]]
                then
                    lowboundmedcol=$(echo ${sortcol[$v]} | cut -d " " -f $lowhalfcol)
                    highboundmedcol=$(echo ${sortcol[$v]} | cut -d " " -f $uphalfcol)
                    machine_median=$(echo "scale=2 ; (($lowboundmedcol+$highboundmedcol)/2)" | bc)
                elif [[ $remcol -eq 0 ]]
                then
                    medcol=$(echo ${sortcol[$v]} | cut -d " " -f $halfmedcol)
                    machine_median=$(echo "scale=2 ; $medcol" | bc)
                    machine_median=$(printf "%0.2f\n" $machine_median)
                fi
                machine=$(echo ${sortcol[$v]} | cut -d " " -f 1)
            done < $1
            echo "Median temperature for $machine was $machine_median C."
            echo
        done
    fi
fi > "${1%.c}.out"
exit 0

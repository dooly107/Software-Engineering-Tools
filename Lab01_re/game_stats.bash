#! /bin/bash

#---------------------------------------
# $Author$
# $Date$
#---------------------------------------

# Do not modify above this line.
Num_Of_Param=$#
Param_Values=$@

if (( $Num_Of_Param != 2 ))
then
    echo "Usage: ./game_stats.bash <file> <game>"
    exit 1
elif [[ ! -f "$1" ]]
then
    echo "Error: \"$1\" does not exist"
    exit 2
else
    totalstudent=$(grep -c $2 $1)
    echo "Total Students: $totalstudent"

    totalHour=0
    highName=0
    highHour=0
    lowName=0
    lowHour=1
    gameName=$2
    while IFS= read -r line
    do
        col1=$(echo $line | cut -d',' -f1)

        col2=$(echo $line | cut -d',' -f2)

        col3=$(echo $line | cut -d',' -f3)
        if [[ $gameName == $col2 ]]
        then
            totalHour=$(( $totalHour+$col3 ))
            if [[ $highHour -lt $col3 ]]
            then
                highHour=$col3
                highName=$col1
            fi
            if [[ $lowHour -ge $col3 ]]
            then
                lowHour=$col3
                lowName=$col1
            fi
        fi        
    done < "$1"
    echo "Total hours spent in a day: $totalHour"
    echo "$highName spent the highest amount of time in a day: $highHour"
    echo "$lowName spent the least amount of time in a day: $lowHour"
fi

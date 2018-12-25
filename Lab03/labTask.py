#! /usr/bin/env python3.4

import sys

def getTotal(accounts):
    result = []
    for i in accounts:
        sum = 0;
        l = i.split()
        list = l[2:]
        lenlist = len(list)
        for j in range(lenlist):
            list[j] = list[j].replace("$","")
        for k in range(lenlist):
            val = float(list[k])
            sum += val
        roundsum = round(sum,2)
        result.append(roundsum)

    return result


def getDoublePalindromes():
    result = []
    for i in range(10,1000001):
        stri = list(str(i))
        binarystr = list(str(bin(i))[2:])
        reversestri = stri[:]
        reversestri.reverse()
        reversebinarystr = binarystr[:]
        reversebinarystr.reverse()

        if reversebinarystr == binarystr and stri == reversestri:
            result.append(i)


    return result





if __name__ == "__main__":


    accounts = ["George Teals:  $1.00   $2.00  $3.00 $4.01 ", "ABI AWSET: $10.51  $22.49  $12.00  $5.33  $100.00  "];
    print(getTotal(accounts));

    print(getDoublePalindromes())
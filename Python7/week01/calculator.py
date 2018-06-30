#!/usr/bin/env python3

import sys

def taxstart(tot):
    socins = [0.08, 0.02, 0.005, 0, 0, 0.06]
    lef = 1
    for a in socins:
        lef -= a
    if tot < 0:
        raise ValueError
    else:
        return tot * lef - 3500

def sep(str_):
    s = str_.strip().split(':')
    return s[0], int(float(s[1]))

def taxfin(taxstart):
    if taxstart < 0:
        return 0
    elif taxstart < 1500:
        return taxstart * 0.03
    elif taxstart < 4500:
        return taxstart * 0.1 - 105
    elif taxstart < 9000:
        return taxstart * 0.2 - 555
    elif taxstart < 35000:
        return taxstart * 0.25 - 1005
    elif taxstart < 55000:
        return taxstart * 0.3 - 2755
    elif taxstart < 80000:
        return taxstart * 0.35 - 5505
    else:
        return taxstart * 0.45 - 13505

if __name__ == '__main__':
    a = sys.argv
    num = len(a)
    if num == 1:
        raise ValueError
    try:
        for s in range(num - 1):
            m, n = sep(a[s+1])
            ns = taxstart(n)
            nt = taxfin(ns)
            ss = ns - nt + 3500
            print(m +":%.2f"%ss)
    except ValueError:
        print("Parameter Error")

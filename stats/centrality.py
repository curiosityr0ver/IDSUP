from typing import List

def mean(xs:List[float])->float:
    return sum(xs)/len(xs)

L=[2,8,8,9,2,3,4,1,112,13]
print(mean(L))

def median_odd(xs:List[float])->float:
    return sorted(xs)[len(xs)//2]

def median_even(xs:List[float])->float:
    sorted_xs=sorted(xs)
    hi_midpoint=len(xs)//2
    return (sorted_xs[hi_midpoint-1]+sorted_xs[hi_midpoint+1])/2

def median(v:List[float])->float:
    return median_even(v) if len(v)%2==0 else median_odd(v)

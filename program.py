import itertools
import enchant
s=input("enter word");
n=len(s)
i=0
for i in range(0,n-1):
    for word in itertools.permutations(s,n-i):
            a= "".join(word)
            d=enchant.Dict("en_UK")
            if d.check(a):
                print (a)
    n -1
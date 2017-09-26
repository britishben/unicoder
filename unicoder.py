#unicoder.py - encodes a number to unicode characters
#requires python 3, i think.

def numberToBase(n,b):
    """
    Takes two decimal ints, and returns an array of ints in the desired base
    >>> numberToBase(1500,2)
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
    """

    if n == 0:
        return [0]
    digits=[]
    while n:
        digits.append( int(n%b) )
        n //= b #"floor division"
    return digits [::-1] #returns array backwards (i.e. in the right order)

num=int( input("Enter the number?: ") or "0" )

base=int( input("Enter the desired number of possible characters (base)?: ") or 10 )

start=input("Enter the unicode start point (such as 0x1400)?: ") or "0x30"
start=int(start,16) #convert hex string to decimal int

myList=numberToBase(num,base)
for i in myList:
      print("{},".format(chr(start+i)),end='')

print() #print a newline at the end

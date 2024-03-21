inputRound = int(input())
maxStar = 2*inputRound - 1
middle = int(maxStar/2)

for i in range(inputRound):
    print(" "*(middle-i),"*"*(2*(i+1)-1))

#!/usr/bin/env python3

#This code returns the greatest possible score from a yahtzee roll

def yahtzee_upper(a):
    great = 0
   #Determines the maximum possible score of given roll
    a = list(map(int,a))
    for i in range(len(a)):
        if(a[i]>great):
            great = a[i]
        elif (a[i] == a[i-1]):
            great += a[i]
    return great





def main():
    print("Give me your yahtzee roll!")
    a = input()
    lis = a.split(" ")
    if(len(lis) != 5):
        print("Invalid yahtzee roll.")
        main()
    ret = yahtzee_upper(lis)
    print(ret)

main()

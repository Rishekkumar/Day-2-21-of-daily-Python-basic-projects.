# Snake, Water, Gun game: 

'''1 for sanke 
    -1 for water
    0 for gun 
'''
import random
computer=random.choise(1,0,-1)
yourstr= (input("enter your number: "))
yourdict= {"s":1,"w":-1,"g":0}
you=yourdict[yourstr]
computerdict={1:"snake", -1:"water" , 0:"gun"}
comp=computerdict[computer]
print(f'you choose:{computerdict[you]}\n computer choose:{computerdict[computer]}')
if(computer == you ):
    print("match draw")
else:
    if(computer== -1 and you ==1):
        print("you win ")
    elif(computer ==-1 and you ==0):
        print("you lose")
    elif(computer ==1 and you ==-1):
        print("you win ")
    elif(computer == 1 and you ==0):
        print("you lose")
    elif(computer==0 and you==-1):
        print("you lose ")
    elif(computer==0 and you ==1):
        print("you lose")
    else:
        print("something went wrong ")

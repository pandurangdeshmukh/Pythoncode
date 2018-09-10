import random
import string
print('..............WELLCOME TO LUCKY DRAW COMPETITION....................\n')

print('''instruction:
       1)choose Number in between 1 to 20
       2)if your guess is correct then you win prize\n''')
name=input("Enter Your Name:")
print("Welcome:",name)
def my_input():
    w=input('press 1 to start game press 0 to exit:')
    return int(w)

myinput=my_input()
num=0
while num<3:
    if myinput==1:
    
        test=random.randint(1,20)
        print (test)

        count=0
        while count<4:
            x=int(input('Guess your Number in between 1 to 20:\n'))

            if x==test:
                print ('Congratulations',name,'you are lucky winner\n')

                if count==0:
                    print ('you win fridge')
                elif count==1:
                    print ('you win tv')
                elif count==2:
                    print ('you win mobile')
                else:
                    print ('you win pendrive')
                break;
            else:
                print (name,'you are unlucky\t','please try again\n')
                if x<test:
                    print ('NOTE:Number is smaller than guess','Enter bigger number\n')
                else:
                    print ('NOTE:Number is larger than guess','Enter smaller number\n')
            count+=1
            if count==4:
                print ('hard luck')

        
        if count==4:
            print ('lucky num is:',test)
        break;
    elif myinput==0:
        exit()
    else:
        print ('Enter correct input')
        my_input()
    num+=1
    if num==3:
        print ('Max attempt over'',''you entered wrong input')



#name=input("enter your name : ")                                                #Input String
#age=int(input("How old are you, {0}? : ".format(name)))                         #String replacement
#address=input("enter your address please : ")
#print("The age of {0} is {1} who lives in {2} " .format(name,age,address))      #Multiple string replacement



month=("Jan:{2},\nFeb:{0},\nMar:{2},\nApril:{1},\nMay:{2},\nJune:{2},\nJuly:{1},\nAugust:{2}, \nSeptember:{1},\nOctober:{2},\nNovember:{1},\nDecember{2}".format(28,30,31))
print(month)



# String Formating:

 #for i in range(1,13):
    #print("No.{0} squared is {1} and cubed is {2}".format(i,i**2,i**3))
    #print("No.{0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    #print("No.{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    #print("No.{0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

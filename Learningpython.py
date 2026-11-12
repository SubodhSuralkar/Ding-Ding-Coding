text = input("Username: ")
try:
    number = int(text)
    print(number)
except:
    print("Invalid username")

print("eheheheheh just adding some comments to mess around aand \n show some progress in github btw i am doing another projects and \n its 3am in the morning or night what should i say i don't but one thing is sure \n i am enjoying this and i am in flow state")

"""
#modular programming is using import
import math
print(math.factorial(5))
import mymodule
#here i created mymodule to acces it using import
print(mymodule.calculator(5,5))
"""

"""
#this is how a to write a file
file = open('file.txt','w')

file.write('In python\n')
file.write("I am learning to write in a file")

file.close()

#this is how afile is read

file = open('file.txt','r')
f = file.readlines()
print(f)
print()
newlist = []

for word in f:
    #this is If else statement for removing \n
    '''
    if word[-1] == "\n":
        newlist.append(word[:-1])
    else:
        newlist.append(word)
    '''
    #this is better method than if else:
    newlist.append(word.strip())
print(newlist)
"""
# WAF to print the length of a list
'''
classs = ['c1' , 'c2' , 'c3' , 'c4' , 'c5' , 'c6']
things_not_in_my_life = ['love' , 'peace' , 'someone' , 'normal life']

def length(list):
    print(len(list))


length(things_not_in_my_life)

classs = ['c1' , 'c2' , 'c3' , 'c4' , 'c5' , 'c6']

def len_list(list):
    for i in list:
        print(list[i])

# len_list(classs)
'''



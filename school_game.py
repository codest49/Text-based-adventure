invontory= ''
def r0_1():
    print('')
def r0_3():
    print('') 
def r1_1():
    print('you found money on the ground. \nWhat do you do?: \npick it up \nburn it \nleave it')
    if input()=="pick it up":
        print()
print('welcome to my game!\nType start to begin') 
if input()=="start":
    print('make your choice on which way to go. \nLeft or right')
if input()=='left':
    r1_1()
if input()=='right':
    r0_1()
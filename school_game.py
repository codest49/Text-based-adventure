import random
def r0_1():
    print('you are hit over the head knocking you out')
    print("You wake up in a dark room. You look around and you can't see anything.\nWhat do you do?")
    print('check your pockets\nhit the wall\nscream')
    if input()=='check your pockets':
        print('you find nothing. your pockets are empty.\n what do you do?')
        print('check your pockets\nhit the wall\nscream')
    if input()=='hit the wall':
        print('you acc')
    if input()=='scream':
        print('nobody hears you and you wither away.\nGAME OVER!')
       # quit()
def r0_3():
    print('') 
def r1_1():
    print('you found money on the ground. \nWhat do you do?: \npick it up \nburn it \nleave it')
    if input()=="pick it up":
        print('you picked it up.')
        #invontory = '$200'
    #return invontory
def main():
    print('welcome to my game!\nType start to begin') 
if input()=="start":
    print('make your choice on which way to go. \nLeft or right')
if input()=='left':
    r1_1()
if input()=='right':
    r0_1()
main()
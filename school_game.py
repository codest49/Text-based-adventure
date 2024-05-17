import random
def r0_1():
    print('you are hit over the head knocking you out')
    print('You wake up in a dark room. You look around and you can\'t see anything.\nWhat do you do?')
    choice_1=input('check your pockets\nhit the wall\nscream\n').lower()
    if choice_1=='check your pockets':
        print('you find nothing. your pockets are empty.\n what do you do?')
        print('hit the wall\nscream')
        choice_1_1=input().lower()
        if choice_1_1=='hit the wall':
            print('You accidentally hit a secret panel and it opens letting you out.')
        elif choice_1_1=='scream':
            print('nobody hears you and you wither away.\nGAME OVER!')
    elif choice_1=='hit the wall':
        print('You accidentally hit a secret panel and it opens letting you out.')
    elif choice_1=='scream':
        print('nobody hears you and you wither away.\nGAME OVER!')
    else:
        print('Invalid choice.')
        return False
    print('You are immediately blinded by the light shining through the doorway.')
    print('You walk through the doorway and almost fall off a plane wing and you realize you are at on\nthe wing of a plane at the crusing altude of a jet liner.')
    print('You try to go back inside but the door closed behind you.')
    print('You here over an intercom "This is the captain speeking we are about to do a barrel roll."')
    print('You realize there is a parachute straped to the side of the plane.')
    print('You can\'t reach the parachute easily.')
    print('What do you do?\nCrawl to the parachute and put it on')
    print('Roll to the parachute and put it on')
    print('Try to hold on')
    choice_2=input().lower()
    if choice_2=='crawl to the parachute and put it on':
        print('You aren\'t fast enough and you fall off the plane without a parachute.')
        print('You hit the ground and go splat.\nYOU DIED')
        return False
    elif choice_2=='roll to the parachute and put it on':
        print('You grab the parachute right before you fall off.')
        print('While you are falling you put the parachute on and pull the ripcord.')
        print('You land successfully.')
    elif choice_2=='try to hold on':
        print('You manage to hold on until the pilot drops the drop tanks.')
        print('One of the the drop tanks hit you in the head knocking you off and unconscious.')
        print('You hit the ground and go splat.\nYOU DIED')
        return False
    else:
        print('Invalid choice.')
        return False
    return True
def r0_2():
    print('Your lucky you almost hit a tree but you landed safely.')
    print('You also almost landed on a landmine.')
def r1_1():
    #print('you found money on the ground. \nWhat do you do?: \npick it up \nburn it \nleave it')
    #if input()=="pick it up":
    #    print('you picked it up.')
    print('')
def main():
    while True:
        print('Welcome to my game!\nType "start" to begin.') 
        start_choice = input().lower()
        if start_choice == "start":
            print('Make your choice on which way to go.\nLeft or right?')
            direction = input().lower()
            if direction == 'left':
                r1_1()
            elif direction == 'right':
                if r0_1():
                    r0_2()
            end_choice=input('Would you like to keep playing?(y/n)').lower()
            if end_choice=='n':
                break
main()
print('Thanks for playing.')
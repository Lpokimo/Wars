from Extras import *

while True:
    ans = input('What year? 1775, 1861, 1917 or 1941 ')
    if ans in TRW:
        print('THE REVOLUTIONARY WAR')
        print('The Revolutionary war was the 13(14 Vermont) colonies escaping from englands control')
        print('The Revolutionary war started in 1775 but had tensions before that')
        print('The Commander George washington was Actually Disliked for most of the war')
        print('and in 1778 France joined the Revolutionary war With america.')
        print('and finally in september 3rd 1783 England Signed the treaty of paris')
        play_again = input("Would you like to restart ")
        if play_again.lower().strip() == 'yes':
            continue
        elif play_again.lower().strip() == "no":
            exit()

    if ans in TCW:
        print('THE CIVIL WAR (and Before)')
        print('The civil war started when the southern colonies were scared of losing their slaves.')
        print('Not because of lincoln its because of time, Slaves were becoming useless')
        print('the north and south were letting states become slave OR Non-slave')
        print("At this point The slave states couldn't have any states above THE line")
        print('Anyways The Civil war started in 1861 and ended in 1865')
        print('there were many generals on both side including,')
        print('Ulysses S. Grant,')
        print('Robert E. Lee,')
        print('and George B. McClellan')
        play_again = input("Would you like to restart ")
        if play_again.lower().strip() == 'yes':
            continue
        elif play_again.lower().strip() == "no":
            exit()
    if ans in TGW:
        print("THE GREAT WAR(The usa's story)")
        print('in 1917 Germany sent a message to mexico.')
        print('to declare war on america but the british intercepted the message')
        print('showed it to the usa so  the us join WW1')
        print('the us was great help stopping the Central powers ')
        print('But the us came nearing the end of the war.')
        play_again = input("Would you like to restart ")
        if play_again.lower().strip() == 'yes':
            continue
        elif play_again.lower().strip() == "no":
            exit()

    if ans in WW2:
        print("WW2")
        print('The only reason the us Even joined WW2 is Because of Pearl Harbor')
        print("when th japanesse bombed pearl harbor The us need a good reason to attack back")
        print("japan was on the axis(The bad guys) So the us joined the WW2")
        print("the Us Was a BIG Help Against the demoralized British soldiers")
        print("Yes only british. germany had set some stuff up to make france look like it was on the axis")
        play_again = input("Would you like to restart ")
        if play_again.lower().strip() == 'yes':
            continue
        elif play_again.lower().strip() == "no":
            exit()

# Russia

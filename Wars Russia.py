from Extras import *

while True:
    print('What Year(1904)?')
    ans = input('')
    if ans in RJW:
        print('The Russo-Japanese war')
        print('The RJW was right at the turn of the century during the 1890s-1900s\nRussia Was Just getting off of a Victory Against China During the boxers revolution\nThe reason the war started was because russia wanted a port for the navy and trade But Japan Refused Unless Russia let japan own korea.\nRussia Refused and Apperently was offended beacause they wanted the NORTH of Korea to be a buffer zone for russia and japan\nThe Japanese attacked at port arthur,China.And Russia Suffered several Defeats but Tsar Nicholas II Wanted to keep fighting\nand russia ended up losing and having to sign a treaty the treaty of Portsmouth')
        print('Do You want More Info')
        play_again = input('')
        if play_again in Ylist:
            continue
        elif play_again in Nlist:
            break

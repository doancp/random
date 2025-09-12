#! python3

import webbrowser, sys, pyperclip

sys.argv  # ['webbrowser lesson.py', '870', 'Valencia' 'St.']

# check if command line arguements were passed

if len(sys.argv) > 1: 
    # if the length of the argument is more than one. meaning if you added more to it.
    # ['webbrowser lesson.py', '870', 'Valencia' 'St.'] we want to this list to become one string -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:]) 
    # so here we slice it, because we only need the address and not the python file. starting at list INDEX 1 which would be '870' leaving the other side of the colon blank means it can grab anything above 1.
    # this basically joins the above address into one string, into the variable 'address'
else:
    address = pyperclip.paste()


# https://www.google.com/maps/place/ADDRESS
webbrowser.open('https://www.google.com/maps/place/' + address)
# this opens the browser to google and adds on the arguements you add in windows+R

# REMEMBER, there are two types of pyperclip and possibly other modules. ones that deal with your computer and ones that deal with your code. you still need to import it, but the copying and pasting is in your computer so you need to go to command line and install.
# since pyperclip is a 3rd party module and not from python, you need to install it on your computer
# also, pathing might be an issue and if path is too long, python cant find it.


# overall, all webbrowser does is open a webrowser page. but we enhanced it by providing some more details for this script

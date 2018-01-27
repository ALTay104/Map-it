import webbrowser, sys, pyperclip

sys.argv #this command line arg will be something like 'mapit.py' '600 Epic Way'

#check if command line arguments were passed
if len(sys.argv) > 1:
    # change it to '600', 'Epic', 'Way'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

import webbrowser, sys, pyperclip

sys.argv = 'mapit 870 Valencia St, San Francisco, CA 94110'
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print address
else:
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
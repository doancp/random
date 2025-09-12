import sys, pyperclip
from playwright.sync_api import sync_playwright

# starts playwright
start  = sync_playwright().start()
browser = start.firefox.launch(headless=False) # False so that browser is not running in background
context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US"
    ) # uses this header that are part of playwright. bypasses youtubes anti bot 

page = context.new_page() # opens new browser page using context variable
page.goto("https://www.youtube.com")

elem_selector = ".ytSearchboxComponentInput" # youtube search box
page.wait_for_selector(elem_selector) # waits for element above to be selectable.


# checks if any arguments are written in Windows Key+R
if len(sys.argv)> 1:
    search = ' '.join(sys.argv[1:]) # joins the arguments together by spaces
else:
    search = pyperclip.paste() # if text is copied and no arguments, paste 


page.fill(elem_selector, search) # takes search bar and fills it with what you copied/typed

page.press(elem_selector, 'Enter') # simulates an Enter key with the search bar


input('Press RETURN to finish') # this is so you can press return to end it. when a script ends, python will just end the program. and having a wait time might be too little time

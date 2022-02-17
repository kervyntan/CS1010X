import pyautogui

# variables
grab_login_link = 'https://bit.ly/3Bkam54'
grab_login_number = '90473599'

windows_logo = (37, 1044)
windows_search = (321, 990)
url = (540, 79)
grab_keyin = (941, 690)
# windows logo = Point(x=37, y=1044)
# search from windows = Point(x=88, y=876)
# url positionn = Point(x=540, y=79)
# grab key in number button = Point(x=985, y=572)
# grab next button = Point(x=1009, y=669)

def movement (x, y):
    pyautogui.moveTo(x, y, duration = 3)

def typing (str):
    pyautogui.write(str, interval = 0.25)
    
def mouse_left_click ():
    pyautogui.click()

def navigation_to_windows_logo(windows_x, windows_y):
    movement(windows_x, windows_y)
    pyautogui.click(button = 'right')
    movement(161, 870)
    mouse_left_click()

def navigation_to_open_browser (search_x, search_y):
    movement(search_x, search_y)
    mouse_left_click()
    typing('Chrome')
    movement(351, 225) # google chrome after searching
    mouse_left_click()
    
def navigation_to_url(x, y):
    movement(x, y)
    mouse_left_click()
    typing(grab_login_link)
    pyautogui.press('enter')

def navigate_grab_login(x, y):
    movement(x,y)
    mouse_left_click()
    typing('90473599')
    movement(984, 773)
    mouse_left_click()

navigation_to_windows_logo(windows_logo[0], windows_logo[1])
navigation_to_open_browser(windows_search[0], windows_search[1])
navigation_to_url(url[0], url[1])
navigate_grab_login(grab_keyin[0], grab_keyin[1])

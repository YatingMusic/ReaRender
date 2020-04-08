import os
import time
import pyautogui
import threading


PATH_TO_REAPER = '/Applications/REAPER64.app'


def click_window():
    '''
    function for click dialog window
    '''
    time.sleep(1.5)
    print('press enter')
    pyautogui.press('enter')


def open_project():
    '''
    open REAPER.app
    '''
    os.system('open ' + PATH_TO_REAPER)
    print('[*] opening...')
    time.sleep(10)
    print('press enter')
    pyautogui.press('enter')
    time.sleep(3)
    print('press enter')
    pyautogui.press('enter')
    time.sleep(3)
    print('press enter')
    pyautogui.press('enter')


def close_project(reopen=True):
    '''
    close REAPER.app
    '''
    print('[*] rclosing...')
    time.sleep(5)
    os.system('killall -9 REAPER')
    time.sleep(5)
    if reopen:
        t = threading.Thread(target=open_project)
        t.start()
        time.sleep(20)

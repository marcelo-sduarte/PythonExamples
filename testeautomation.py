import pyautogui as py
import pandas as pd

import scrapy 


from scrapy.mail import MailSender
mailer = MailSender()

py.PAUSE = 1
py.press('win')
py.write('chrome')
py.press('enter')
py.write('http://google.com/')
py.press('enter')

im1 = py.screenshot()
im2 = py.screenshot('my_screenshot.png')

open('my_screenshot.png')
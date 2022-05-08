from selenium import webdriver
import threading
import requests
import random
import time
import os
import ctypes
import sys
import string
import webbrowser
import subprocess
from time import sleep
import threading
import requests
from string import ascii_letters
import random
import time
import os
from os import system
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from os import system
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from colorama import Fore, Back, Style, init
init()
#{Fore.GREEN}[+] {Style.RESET_ALL}
opts = webdriver.ChromeOptions()
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--disable-extensions')
opts.add_argument('--profile-directory=Default')
opts.add_argument("--incognito")
opts.add_argument("--disable-plugins-discovery")
opts.add_argument("--headless")
opts.add_argument('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
opts.add_argument("--mute-audio")
driver = webdriver.Chrome('chromedriver.exe', options=opts)
webbrowser.open('https://www.youtube.com/channel/UCMitxi4f8XDUce2Whn1n4ig')
print(f'{Fore.MAGENTA} Credit To Node For Making Tool {Style.RESET_ALL}')
def main():
    for i in range(1):
        ctypes.windll.kernel32.SetConsoleTitleW(f'Node on youtube | NodeCodez on github | Made By Node')
        #ogvitality
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Username of streamer ')
        user = input()
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Your Account Username ') 
        username = input()
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Your Account Password ') 
        password = input()
        driver.get('https://www.twitch.tv/' + user)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div').click()
        time.sleep(0.7)
        driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(password + Keys.RETURN)
        time.sleep(0.3)
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}CHECK IF THERE IS A CAPATCHA!!! if there is fill it out')
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Email Verification Code (Check Account Email) ')
        code = input()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div[1]/div/input').send_keys(code)
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/button').click()
        print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Followed {user} +300 Points! (average)')
        while True:
            #here is where i love coding :(
            points = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/button/div/div/div/div[2]/span").text
            print(points)
            try:
                driver.find_element_by_xpath('//*[@id="2e4efbf0d8ecda7463839671e11e3e69"]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button').click()
            except:
                pass
main()
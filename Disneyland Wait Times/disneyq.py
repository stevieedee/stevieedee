from selenium import webdriver
from urllib.request import urlopen
import re
from selenium.webdriver.common.by import By
import time
import os
import smtplib
from emial.message import EmailMessage

#Create teh email message
msg = EmailMessage()
msg['Subject'] = 'Your Subject Here'
msg['From'] = 'your_email@example.com'
msg['To'] = 'recipient_email@example.com'
msg.set_content('This is the email body')

#Setup SMTP server and send email
with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp:
    smpt.login('your_email@example.com', 'your_password')
    smpt.send_message(msg)


# how do you continiously run this script and check every ride? and send an email if ride time is < 10 minutes?


#DCA
# 1 = Golden Zephyr
# 2 = Little Mermaid
# 3 = Inside Out
# 4 = Mater's Junkyard
# 5 = Luigi's
# 6 = Monster's Inc
# 7 Jessie's Critters
# 8 = Web Slingers

#Disneyland

# 9 = Small World
# 10 = Winnie the Pooh
# 11 = Pirate's of the Carribean
# 12 = Big Thunder Mountian
# 13 = Mickey's Runaway Railway
# 14 = Chip and Dale Coaster
# 15 = Mad Tea Party
# 16 = 


# Alphabeticalize this
# Future improvement, user can input any name instead of number


urls = {
    '1': 'https://www.laughingplace.com/w/p/golden-zephyr-disney-california-adventure/',
    '2': 'https://www.laughingplace.com/w/p/the-little-mermaid-ariels-undersea-adventure-disney-california-adventure/',
    '3': 'https://www.laughingplace.com/w/p/inside-out-emotional-whirlwind-disney-california-adventure/',
    '4': 'https://www.laughingplace.com/w/p/maters-junkyard-jamboree-disney-california-adventure/',
    '5': 'https://www.laughingplace.com/w/p/luigis-rollickin-roadsters-disney-california-adventure/',
    '6': 'https://www.laughingplace.com/w/p/monsters-inc-mike-sulley-to-the-rescue-disney-california-adventure/',
    '7': 'https://www.laughingplace.com/w/p/jessies-critter-carousel-disney-california-adventure/',
    '8': 'https://www.laughingplace.com/w/p/web-slingers-a-spider-man-adventure-disney-california-adventure/'
}

rides = {
    '1': 'Golden Zephyr',
    '2': 'Little Mermaid',
    '3': 'Inside Out',
    '4': 'Mater\'s Junkyard Jamboree',
    '5': 'Luigi\'s\n',
    '6': 'Monster\'s Inc',
    '7': 'Jessie\'s Critter Carousel',
    '8': 'Web Slingers'
}

inp = input('\033[1;32;40m\033 Please select a ride to see wait time: \n'
'1: Golden Zephyr\n'
'2: Little Mermaid\n'
'3: Inside Out\n'
'4: Mater\'s Junkyard Jamboree\n'
'5: Luigi\'s\n'
'6: Monster\'s Inc \n'
'7: Jessie\'s Critter Carousel\n'
'8: Web Slingers\n'
'\n'
'Selection: ')

browser=webdriver.Firefox()
url = urls[inp]
new_lis=[]
browser.get(url)
text = browser.find_element(By.CLASS_NAME, "waittimeinfo1").text
time.sleep(3)
browser.close()

for i in text.split():
    if i.isdigit():
        new_lis.append(int(i))
    else:
        new_lis.append(i)

print(new_lis)


for m in new_lis:
    if m.isdigit():
        if m <= 13: #13 because of Haunted Mansion:
            print(f'wait time is 10 minutes and under.')
    else:
        if new_lis[0] == 'Closed':
            print('Ride is Closed')
        else:
            print('Ride wait time is:{}'.format({new_lis}))



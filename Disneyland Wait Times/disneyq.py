from selenium import webdriver
from urllib.request import urlopen
import re
from selenium.webdriver.common.by import By
import time
import os
#from twilio.rest import Client

################################################################
# This takes Disney wait times from The Laughing Place website #
# There was an option to text wait times to user, but it's a   #
# paid subscription.                                           #
################################################################

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']


#DCA
# 1 = Golden Zephyr
# 2 = Little Mermaid
# 3 = Inside Out
# 4 = Mater's Junkyard
# 5 = Luigi's
# 6 = Monster's Inc
# 7 = Jessie's Critters
# 8 = Web Slingers
# 9 = what other rides do you want?

#Disneyland
# 9 = Small World
# 10 = Winnie the Pooh
# 11 = Pirates
# 12 = Mad Tea Party
# 13 = Haunted Mansion


urls = {
    '1': 'https://www.laughingplace.com/w/p/golden-zephyr-disney-california-adventure/',
    '2': 'https://www.laughingplace.com/w/p/the-little-mermaid-ariels-undersea-adventure-disney-california-adventure/',
    '3': 'https://www.laughingplace.com/w/p/inside-out-emotional-whirlwind-disney-california-adventure/',
    '4':'https://www.laughingplace.com/w/p/maters-junkyard-jamboree-disney-california-adventure/',
    '5': 'https://www.laughingplace.com/w/p/luigis-rollickin-roadsters-disney-california-adventure/',
    '6': 'https://www.laughingplace.com/w/p/monsters-inc-mike-sulley-to-the-rescue-disney-california-adventure/',
    '7': 'https://www.laughingplace.com/w/p/jessies-critter-carousel-disney-california-adventure/',
    '8': 'https://www.laughingplace.com/w/p/web-slingers-a-spider-man-adventure-disney-california-adventure/',
    '10': 'https://www.laughingplace.com/w/p/the-many-adventures-of-winnie-the-pooh-disneyland/',
    '11': 'https://www.laughingplace.com/w/p/pirates-of-the-caribbean-disneyland/',
    '12': 'https://www.laughingplace.com/w/p/mad-tea-party-disneyland/',
    '13': 'https://www.laughingplace.com/w/p/haunted-mansion-disneyland/'
}

#Rides chosen based off of kid's height restriction
rides = {
    '1': 'Golden Zephyr',
    '2': 'Little Mermaid',
    '3': 'Inside Out',
    '4': 'Mater\'s Junkyard Jamboree',
    '5': 'Luigi\'s\n',
    '6': 'Monster\'s Inc',
    '7': 'Jessie\'s Critter Carousel',
    '8': 'Web Slingers',
    '10': 'Winnie the Pooh',
    '11': 'Pirates',
    '12': 'Mad Tea Party',
    '13': 'Haunted Mansion'
}

user_input = input('\033[1;32;40m\033 Please sinput ride number to see wait time: \n'
'1: Golden Zephyr\n'
'2: Little Mermaid\n'
'3: Inside Out\n'
'4: Mater\'s Junkyard Jamboree\n'
'5: Luigi\'s\n'
'6: Monster\'s Inc \n'
'7: Jessie\'s Critter Carousel\n'
'8: Web Slingers\n'
'10: Winnie the Pooh\n'
'11: Pirates\n'
'12: Mad Tea Party\n'
'13: Haunted Mansion\n'
'\n'
'Selection: '
)

browser=webdriver.Safari()
url = urls[user_input]
new_lis=[]
browser.get(url)
text = browser.find_element(By.CLASS_NAME, "waittimeinfo1").text
time.sleep(3)
browser.close()

for i in text.split():
    if i.isdigit():
        new_lis.append(int(i))

for m in new_lis:
    if m <= 13: #13 because of Haunted Mansion
        #client = Client(account_sid,auth_token)
        #client.messages.create(
            #to=os.environ["MY_PHONE_NUMBER"],
            #from_="19784875784",
            #body= rides[inp] + " has a wait time of under 10 minutes! HURRY AND GET OVER THERE!!!"
    #)
        print(f'wait time is 10 minutes and under. {new_lis}')
    else:
         print('wait time over 10 min')
         print (f'Actual wait time is: \033[1;31;40m {new_lis} minutes')




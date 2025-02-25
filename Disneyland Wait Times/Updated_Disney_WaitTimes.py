import os
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from rides import rides

def send_email(ride_name, wait_time):
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    msg = EmailMessage()
    msg['Subject'] = f'Low Wait Time Alert: {ride_name}'
    msg['From'] = email_user
    msg['To'] = email_user
    
    if wait_time == 'Closed':
        msg.set_content(f'{ride_name} is Closed! Check back later.')
    else:
        msg.set_content(f'The wait time for {ride_name} is now {wait_time} minutes!')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('useremailhere', 'passwordhere')
        smtp.send_message(msg)

def get_ride_wait_time(url):
    with webdriver.Firefox() as browser:
        browser.get(url)
        
        try:
            time.sleep(5) 
            wait_time_element = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gauge-desc-box"))
            )
            text = wait_time_element.text
        except Exception as e:
            print(f"Error: {e}")
            text = None
        
    if text:
        for word in text.split():
            if word.isdigit():
                return int(word)
        if "No Data Collected Yet!" in text:
            return "Closed"
    
    return None

def monitor_rides():
    while True:
        for ride, url in rides.items():
            wait_time = get_ride_wait_time(url)
            if wait_time is not None:
                if wait_time == "Closed":
                    print(f'Alert: {ride} is currently closed.')
                elif isinstance(wait_time, int) and wait_time <= 20:
                    print(f'Alert: {ride} wait time is {wait_time} minutes!')
                    send_email(ride, wait_time)
        time.sleep(600)

def get_current_location():
    try:
        response = requests.get("[YOUR IP HERE]:5000/location")
        data = response.json()
        if "latitude" in data and "longitude" in data:
            return float(data["latitude"]), float(data["longitude"])
    except requests.exceptions.RequestException as e:
        print("Error retrieving location from server:", e)
    return None, None

def is_at_disneyland(latitude, longitude):
    try:
        response = requests.post(
            "[YOUR IP HERE]/location",
            json={"latitude": latitude, "longitude": longitude}
        )
        data = response.json()
        return data.get("status") == "inside Disneyland"
    except requests.exceptions.RequestException as e:
        print("Error checking location (request):", e)
        return False
    except (ValueError, KeyError, TypeError) as e:
        print("Error decoding JSON or accessing data:", e)
        return False
    except Exception as e:
        print("Error checking location (other):", e)
        return False

if __name__ == "__main__":
    while True:
        latitude, longitude = get_current_location()
        if latitude is not None and longitude is not None:
            if is_at_disneyland(latitude, longitude):
                print("You're at Disneyland! Checking wait times for rides...")
                monitor_rides()
            else:
                print("You're not at Disneyland. Waiting...")
        else:
            print("Unable to retrieve location. Retrying...")
        time.sleep(2)
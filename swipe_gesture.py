from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Pixel9API34'  
options.udid = 'emulator-5554'
options.automation_name = 'UiAutomator2'
options.no_reset = True  

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

def swipe_right(driver, duration=800):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] * 0.1  
    end_x = screen_size['width'] * 0.9    
    start_y = screen_size['height'] * 0.5  
    end_y = start_y  
 
    driver.swipe(start_x, start_y, end_x, end_y, duration)

try:
    time.sleep(5)
    swipe_right(driver)
    time.sleep(3)  
    print("Swipe right action performed successfully!")

finally:
    driver.quit()
i = int(1) #defines i. idk why i put this here

from selenium import webdriver  # imports everything 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "E:/chromedriver/chromedriver"  # path for the chrome driver (note to keep this updated)
driver = webdriver.Chrome(Path)  # discribes the instance of a driver
driver.get("https://clickspeedtest.com/10-seconds.html") # open's the webpage
 
time.sleep(10) #sleep cuz my internet and the website and also my computer take 3 light years 
               #and i didnt use implicit wait
Click_Area = WebDriverWait(driver , 10 ).until #web driver waits
(EC.presence_of_element_located((By.ID , "clicker")))


while i < 500:  # the while loop to click 
   Click_Area.click()
   i += 1 
time.sleep(10) 



    
        




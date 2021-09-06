# to make a new selenium console
# importing selenium releated modules
i = int(1)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "E:/chromedriver/chromedriver"
driver = webdriver.Chrome(Path)
driver.get("https://clickspeedtest.com/10-seconds.html")

time.sleep(10)
Click_Area = WebDriverWait(driver , 10 ).until
(EC.presence_of_element_located((By.ID , "clicker")))


while i < 500:
   Click_Area.click()
   i += 1 
time.sleep(10) 



    
        




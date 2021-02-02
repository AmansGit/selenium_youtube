from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://youtu.be/4cLa1c7Zzg8")

user_data = driver.find_element_by_xpath('//*[@id="video-title"]')
link = []
print("user::",user_data)

for i in user_data:
    link.append(i.get_attribute('href'))

print("Link::",len(link))

df = pd.DataFrame(column = ['link', 'title', 'description', 'category'])
wait = WebDriverWait(driver, 10)
v_category = "CATEGORY_NAME"
for x in links:
    driver.get(x)
    v_id = x.strip('https://www.youtube.com/watch?v=')
    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    v_description =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#descriptio  yt-formatted-string"))).text

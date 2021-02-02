# from selenium import webdriver
# import pandas as pd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/watch?v=4cLa1c7Zzg8&feature=youtu.be")

# user_data = driver.find_element_by_xpath('//*[@id="video-title"]')
# urls_links = []
# descriptions = []
# vid_title = []


# print("user::",user_data)


# for i in user_data:
#     links.append(i.get_attribute('innerHTML'))

# print("Link::",len(links))

# # df = pd.DataFrame(column = ['link', 'title', 'description', 'category'])
# # wait = WebDriverWait(driver, 10)
# # v_category = "CATEGORY_NAME"
# #for x in links:
# #    driver.get(x)
# #    v_id = x.strip('https://www.youtube.com/watch?v=')
# #    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
# #    v_description =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#descriptio  yt-formatted-string"))).text

from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://www.youtube.com/watch?v=m00F8gAJJJo'
driver.get(url)
xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string'

e = driver.find_element_by_xpath(xpath)
print(e.get_attribute('innerHTML'))
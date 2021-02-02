from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

import json
driver = webdriver.Chrome()
channelURL = "https://www.youtube.com/channel/UCO5QSoES5yn2Dw7YixDYT5Q"


def getChannelDetals(links):
	details = []
	# for li in links:
	driver.get(f"{links}/about")
	channel_name = driver.find_element_by_xpath("//*[@id='text']").text
	discC = driver.find_element_by_css_selector("#description-container").text
	subs = driver.find_element_by_xpath("//*[@id='subscriber-count']").text
	descriptions = driver.find_element_by_xpath("//*[@id='description-container']").text
	# channel_link = li
	other_linksobj = driver.find_element_by_xpath("//*[@id='links-container']").text
	# other_links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"), other_linksobj)))
	
	obj = {
		"name": channel_name,
		"descriptions": descriptions,
		# "URL": channel_link,
		"Social Links": other_linksobj,
		"Subscriber": subs,
		"discription": discC
	}
	details.append(obj)
	return details



if __name__ == '__main__':
	channelDetails = getChannelDetals(channelURL)
	print(json.dumps(channelDetails, indent=4))
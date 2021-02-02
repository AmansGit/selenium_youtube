from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

import json
driver = webdriver.Chrome()

def getVideoDetails(uTube_url, channelName):
	# base_url = uTube_url + "/c/" + channelName + "/videos"
	base_url = f"{uTube_url}/c/{channelName}/videos"
	driver.get(base_url)
	videos_list = []

	allVideos = driver.find_elements_by_tag_name("ytd-grid-video-renderer")
	print(allVideos)
	for i in allVideos:
		# play_video = driver.find_element_by_xpath("//*[@id='video-title']").text
		# print(play_video)
		time.sleep(2)
		
		i.click()
		# play_video = driver.find_element_by_xpath("//*[@id='video-title']").click()
		# time.sleep(2)
		# video_name = driver.find_element_by_css_selector("#container > h1 > yt-formatted-string").text
		# vid_url = driver.current_url
		# time.sleep(5)
		# show_more_click = driver.find_element_by_xpath("//*[@id='more']/yt-formatted-string").click()
		# descriptions = driver.find_element_by_css_selector("#description").text

		# obj = {
		# 	"Name": video_name,
		# 	"Video URL": vid_url,
		# 	"Description": descriptions
		# }
		# videos_list.append(obj)
		# print(json.dumps(obj))
	# return videos_list


# def getChannelDetals(uTube_url, channelName):
# 	details = []
# 	# for li in links:
# 	driver.get(f"{uTube_url}/c/{channelName}/about")
# 	channel_name = driver.find_element_by_css_selector("#text").text
# 	discC = driver.find_element_by_css_selector("#description-container").text
# 	subs = driver.find_element_by_xpath("//*[@id='subscriber-count']").text
# 	# descriptions = driver.find_element_by_xpath("//*[@id='description-container']").text
# 	# channel_link = li
# 	# other_linksobj = driver.find_element_by_css_selector("//*[@id='link-list-container']/a[1]/yt-formatted-string]").text
# 	# other_links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"), other_linksobj)))
# 	print(channel_name)
# 	obj = {
# 		"name": channel_name,
# 		# "descriptions": descriptions,
# 		# "URL": channel_link,
# 		# "Social Links": other_linksobj,
# 		"Subscriber": subs,
# 		"discription": discC
# 	}
# 	details.append(obj)
# 	return details

if __name__ == '__main__':
	uTube_url = "https://www.youtube.com/"
	username = input()	#this line will replace by excel link imported

	all_videos = getVideoDetails(uTube_url, username)
	# channelDetails = getChannelDetals(uTube_url, username)
	# print(json.dumps(channelDetails, indent=4))
	print(json.dumps(all_videos, indent=4))
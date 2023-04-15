import requests
import os
import re
from bs4 import BeautifulSoup
import dateutil.parser

class Podcast:
	def __init__(self, name, rss_feed_url):
		self.name = name
		self.rss_feed_url = rss_feed_url
		
        # Create a folder to keep all mp3 file
		self.download_directory = f'./downloads/{name}'
		if not os.path.exists(self.download_directory):
			os.makedirs(self.download_directory)

        # Create a folder to keep all the transcript file (.txt)
		self.transcription_directory = f'./transcripts/{name}'
		if not os.path.exists(self.transcription_directory):
			os.makedirs(self.transcription_directory)

	def get_items(self, limit=None):
        # limit: how many podcast you want download and transcript
		page = requests.get(self.rss_feed_url)
		soup = BeautifulSoup(page.text, 'xml')
		return soup.find_all('item')[:limit]

    # The function will search the key word you want into the description in each podcasts
	def search_items(self, search, limit=None):
		matched_podcasts = []
		items = self.get_items()
		for podcast in items:
			if re.search(search, podcast.find('description').text, re.I):
				matched_podcasts.append(podcast)

		return matched_podcasts[:limit]
"""

Inspired by code created by Diego De Lazzari
Modified for Python 3 by Aungshuman Zaman
Adapted for obtaining data using ELK by Stephen Paladines & Muhammed Fallah

"""

from selenium import webdriver 			# From bs4 import BeautifulSoup # For HTML parsing
from time import sleep 					# To prevent overwhelming the server between connections
from collections import Counter 		# Keep track of our term counts
import nltk 							# Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd 					# For converting results to a dataframe and bar chart plots
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import NoSuchElementException
from nltk.corpus import stopwords
import numpy as np
import sys
import re
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
nltk.download('stopwords')
# call the helper

from helper import load_obj, get_csv, save_obj_json, init_driver, searchJobs, text_cleaner, get_pause, \
string_from_text

# 1 - Load existing dictionary. Check for initial dictionary.
# If empty, initialize

try:
	jobDict = load_obj('glassDoorDict')
	link =    load_obj('glassDoorlink')
except:
	save_obj_json([], 'glassDoorlink')
	save_obj_json({}, 'glassDoorDict')

	jobDict = load_obj('glassDoorDict')
	link =    load_obj('glassDoorlink')

print('len(jobDict) = '+str(len(jobDict))+ ', len(link) = '+str(len(link)))

# 2 - Choose what you want to do:
# get_link => Scraping for links and brief data,
# get_data => Scraping for detailed data.


get_link = True 
get_data = True 

if get_link or get_data:

# 3- initialize website

	website = "https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK"

	# Initialize the automatic webdriver

	browser = init_driver()
	browser.get(website)
	emailUser = browser.find_element_by_id("userEmail")
	emailUser.send_keys("vuxizu@virtual-email.com")
	passwordUser = browser.find_element_by_id("userPassword")
	passwordUser.send_keys("GatorCrawler")
	button = browser.find_element_by_xpath("//*[@id='InlineLoginModule']/div/div/div[1]/div[4]/form/div[3]/div[1]/button")
	button.click()


# 4- Scrape for links and brief data
#	 List will be used to grab information (get_data) from each individiual link

if get_link :
	iter_num = 0		 #	Variable counter for loop
	while iter_num < 1:	 #	Iterate until complete
		print('Starting iteration number {}'.format(iter_num))
		sleep(get_pause())				# Pause added to slow down process in order to avoid being blacklisted

		# Initialize cities and jobs
		jobName_lst = ['Data Scientist', 'Data Analyst','Data Engineer', 'Junior Developer', 'Software Developer']	#	List of predetermined jobs (update to ask the user)
		jobName = np.random.choice(jobName_lst)		#	jobName = 'Data Scientist' (Will chose a random position from array -> update by user preference)

		city_lst = ['San Jose','New York','San Francisco','Detroit','Washington','Austin','Boston','Seattle','Chicago','Los Angeles',' ']#	List of predetermined cities (update to ask the user)
		city = np.random.choice(city_lst)			#	city = 'Miami'  (Will chose a random position from array -> update by user preference)

		print('jobName = '+ jobName + ', city = '+ city)	# Confirm website input

		# search for jobs (short description)
		try:
			# jobDict structure {'job_id':['rating','position','company','salary']}
			update_jobDict, update_link = searchJobs(browser, jobName, city, jobDict, link)
			sleep(get_pause())
		except Exception as e:
			print(type(e),e)
			sys.exit("Error message")

		print('len(update_jobDict) = '+ str(len(update_jobDict)) + ', len(update_link) = '+ str(len(update_link)))

		# save dictionary and link

		save_obj_json(update_jobDict, 'glassDoorDict')
		save_obj_json(update_link, 'glassDoorlink')

		iter_num += 1

	#browser.close()
 # 5- Scrape the job description for every link

if get_data:
	print('len(link) = ' + str(len(link)))
	while len(link) > 0: # Originally 0, a hard coded solution for when only bad links are left.
		try:
			rnd_job = np.random.choice(range(len(link)))
			ids = link[rnd_job][0]
			page = link[rnd_job][1]
			browser.get(page)
			sleep(5)
			
			# Extract text (Not necessary for ELK solution)
			desc_list = browser.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[1]').text
			print('desc_list '+ str(type(desc_list)))
			description = text_cleaner(desc_list)
			#print(desc_list)
			#description = desc_list
			#print('description '+ str(type(description)))

			# jobDict structure {'job_id':['rating','position','company','salary','descr']}
			jobDict[ids].append(description)

			# Additional information about company (size, revenue, industry)
			sleep(5)
			try:
				browser.find_element_by_xpath('//*[@id="JobDetailsInfo"]/div/header/div/div/div[2]/span').click()
				tmp_txt = browser.find_element_by_id('EmpBasicInfo').text
				headQuarter = string_from_text('Headquarters', tmp_txt)
				#print(tmp_txt)
				#headQuarter = headQuarter.replace(',','')
				print(headQuarter)
				hq_city = headQuarter.split(',')[0]
				#print('hq_city = ',hq_city)
				jobDict[ids].append(hq_city)
				print(' 1 = ',)
				hq_state_code = headQuarter.split(',')[1]
				#print('hq_state_code = ',hq_state_code)
				jobDict[ids].append(hq_state_code)
				print(' 2 = ',)
				#size_low = int(re.findall('\d+',string_from_text('Size',tmp_txt))[0])
				#size = string_from_text('Size',tmp_txt)
				#print('size = ', size)
				#size_high = int(re.findall('\d+',string_from_text('Size',tmp_txt))[1])
				#print(' = ',)
				#jobDict[ids].append(size)
				#print(' 3 = ',)
				#jobDict[ids].append(size_low)
				#jobDict[ids].append(size_high)
				industry = string_from_text('Industry',tmp_txt)
				print('industry = ',industry)

				jobDict[ids].append(industry)
				print(' 4 = ',)
				#jobDict[ids].append(revenue)


			except Exception as e:
				print(type(e),e)

			# Remove links already used

			dummy = link.pop(rnd_job)

			# If everything is fine, save
			print("Saving data......")
			save_obj(jobDict, 'glassDoorDict')
			save_obj(link, 'glassDoorlink')
			
			print('Scraped successfully ' + ids)

			sleep(get_pause())
		except:
			print( ids + ' is not working! Sleep for 6 seconds and retry')
			print( 'Still missing ' + str(len(link)) + ' links' )
			sleep(6)
	print('Done for now!! len(link) = ' + str(len(link)))
	browser.close()

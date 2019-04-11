"""

Inspired by code created by Diego De Lazzari
Modified for Python 3 by Aungshuman Zaman
Adapted for obtaining data using ELK by Stephen Paladines & Muhammed Fallah

"""
from selenium import webdriver           # From bs4 import BeautifulSoup # For HTML parsing
from time import sleep                   # To prevent overwhelming the server between connections
from collections import Counter          # Keep track of our term counts
import nltk                              # Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd                      # For converting results to a dataframe and bar chart plots
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nltk.corpus import stopwords
import numpy as np
import pickle
import re
import csv
import os.path
import json
#from collections import OrderedDict
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
nltk.download('stopwords')

def init_driver():
    ''' Initialize chrome driver'''

    chrome_options = webdriver.ChromeOptions()

    #chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--account-consistency")
    #chrome_options.add_argument("--disable-plugins-discovery")
    #chrome_options.add_argument("--start-maximized")
    #browser = webdriver.Chrome(driver, chrome_options=chrome_options)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    #browser = webdriver.Chrome()

    return browser

##############################################################################

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

###############################################################################

def save_obj_json(obj, name):
    with open(name + '.json', 'wb') as f:
        json.dump(obj,f)

###############################################################################

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

###############################################################################

def load_obj_json(name):
    with open(name + '.json', 'rb') as f:
        return json.load(f)
        
###############################################################################
# Alternating pauses to avoid being blacklisted
def get_pause():
    return np.random.choice(range(4,6))

###############################################################################
# Utility function to get csv file from pickle.
def get_csv(pickle_obj):  ####&&&& Don' use it for new files
    my_dict = load_obj(pickle_obj)
    csv_filename = 'mycsvfile.csv'
    if os.path.isfile(csv_filename):
        print('File already exists! Please rename it.')
        return
    with open(csv_filename, 'w') as f:  # Just use 'w' mode in 3.x
        writer = csv.writer(f)

        for k,v in my_dict.items():
            if len(v) == 6:
                new_dict = {}
                new_dict['job_id'] = k
                new_dict['rating'] = v[0]
                new_dict['position'] = v[1]
                new_dict['company_name'] = v[2]
                new_dict['salary'] = v[3]
                new_dict['link'] = v[4]
                new_dict['description'] = v[5]  #[x.decode('ascii') for x in v[5]]
                writer.writerow(new_dict.values())

###############################################################################

def get_csv2(pickle_obj): ####&&&& Don' use it for new files
    my_dict = load_obj(pickle_obj)
    csv_filename = 'mycsvfile2.csv'
    if os.path.isfile(csv_filename):
        print('File already exists! Please rename it.')
        return
    with open(csv_filename, 'w') as f:  # Just use 'w' mode in 3.x
        writer = csv.writer(f)
        fieldnames = ['job_id','rating','position','company_name','salary','link',\
        'description','hq_city','hq_state_code','size','industry']

        for k,v in my_dict.items():
            if len(v) == 10:
                new_dict = {}
                new_dict['job_id'] = k
                new_dict['rating'] = v[0]
                new_dict['position'] = v[1]
                new_dict['company_name'] = v[2]
                new_dict['salary'] = v[3]
                new_dict['link'] = v[4]
                new_dict['description'] = v[5]  #[x.decode('ascii') for x in v[5]]
                new_dict['hq_city'] = v[6]
                new_dict['hq_state_code'] = v[7]
                new_dict['size'] = v[8]
                new_dict['industry'] = v[9]

                #writer.writerow(new_dict.values())
                writer.writerow([new_dict[i] for i in fieldnames]) #order preserved

##############################################################################

def get_csv3(pickle_obj): ####&&&&
    my_dict = load_obj(pickle_obj)
    csv_filename = 'mycsvfile3.csv'
    if os.path.isfile(csv_filename):
        print('File already exists! Please rename it.')
        return

    with open(csv_filename, 'w') as f:  # Just use 'w' mode in 3.x
        writer = csv.writer(f)
        fieldnames = ['job_id','rating', 'position', 'company', 'job_city', 'job_state_code',\
         'sal_low', 'sal_high', 'link','description','hq_city','hq_state_code','size','industry']

        for k,v in my_dict.items():
            if len(v) == 13:
                new_dict = {}
                new_dict['job_id'] = k
                new_dict['rating'] = v[0]
                new_dict['position'] = v[1]
                new_dict['company'] = v[2]
                new_dict['job_city'] = v[3]
                new_dict['job_state_code'] = v[4]
                new_dict['sal_low'] = v[5]
                new_dict['sal_high'] = v[6]
                new_dict['link'] = v[7]
                new_dict['description'] = [x.decode('ascii') for x in v[8]]
                #print(type(v[8]))
                new_dict['hq_city'] = v[9]
                new_dict['hq_state_code'] = v[10]
                new_dict['size'] = v[11]
                new_dict['industry'] = v[12]

                #writer.writerow(new_dict.values())
                writer.writerow([new_dict[i] for i in fieldnames]) #order preserved

##############################################################################

def searchJobs(browser, jobName, city = None, jobDict = None, link = None):
    '''Scrape for job listing'''
    if True:
        job = browser.find_element_by_id("sc.keyword")              # Job title, keywords, or company
        location = browser.find_element_by_id("sc.location")        # Location search
        sleep(3)

        job.send_keys(jobName)                                      # Type in job name in search
        sleep(2)

        location.clear()                                            # Location form must be cleared since it's already populated.
        location.send_keys(city)                                    # Type in location name in search
        sleep(2)

        browser.find_element_by_class_name('gd-btn-mkt').click()    # Seach job button
        sleep(5)
        

        # Find brief description
        for i in range(1): #20  ####&&&&
            try:
                # Extract useful classes
                jobPosting = browser.find_elements_by_class_name('jl')
                sleep(10)

                # Create a job Dictionary based on a unique  (job) data-id as key for the dictionary
                # Map will consist of a 2-tuple(data-id and selenium webElement (job listing)).
                jobTuple = map(lambda a: (a.get_attribute('data-id'), a), jobPosting)

                # Filter out the job, data-ids that are not present in the Dictionary (jobDict.keys())
                # Variable will be used to update the job dictionary and job list
                newPost = list(filter(lambda b: b[0] not in jobDict.keys(), jobTuple) ) #list of 2-tuple

                # If there are new posts, update job dict and link list
                if newPost != []:
                    # Process the tuple
                    # Example of a[1].text ->
                    # "3.7\nData Scientist, Analytics\nEtsy – Brooklyn, NY\n$114k-$167k  (Glassdoor Est.)\nWe're Hiring"
                    # Tuple structure ('job_id',['rating','position','company','salary'])
                    # JobData = list(map(lambda a: (a[0],a[1].text.encode("utf8")./
                    # split('\n')[0:4]),newPost))
                    # JobData = list(map(lambda a: (a[0],a[1].text.split('\n')[0:4]),newPost))
                    # JobData = list(map(do_stuff, newPost)) ####&&&&
                    # do_stuff returns many misplaced entries.
                    # do_new_stuff uses regex to minimize bad data, it also splits up entries into more columns
                    # new tuple structure ('job_id',[rating, position, company, job_city, job_state_code, sal_low, sal_high])
                    print('starting do_new_stuff')
                    jobData = list(map(do_new_stuff, newPost))
                    print("I'm out of do_new_stuff.")

                    # Update job dictionary;
                    # Convert tuple to dictionary. structure ('job_id',['rating',...]) -> {'job_id':['rating',...]}
                    print('updating jobDict')
                    tmp = dict((a[0],a[1]) for a in jobData)
                    print('tmp created')
                    jobDict.update(tmp) # Add a new entry with unique key job_id
                    # Finally find the links:
                    link_lst = list(map(lambda c: (c[0],c[1].find_element_by_tag_name('a').\
                        get_attribute('href')), newPost))
                    # Add the link to job dict
                    print('Adding to link')
                    tmp = [jobDict[c[0]].append(c[1]) for c in link_lst]
                    # Update link list. This will be used in get_data part.
                    link += link_lst
                browser.find_element_by_class_name('next').click() # Next page
                try:
                    browser.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/div').click() # Pop up
                except:
                    pass

            except Exception as e:
                # Pass
                print(type(e),e)

    return jobDict, link

###############################################################################

def text_cleaner(text):
    '''
    This function just cleans up the raw html so that I can look at it.
    Inputs: a URL to investigate
    Outputs: Cleaned text only
    '''
    print('starting text_cleaner')
    stopws = set(stopwords.words('english'))
    #print('initialized stopws')
    
    lines = (line.strip() for line in text.splitlines()) # break into lines
    #lines = [line.strip() for line in text.splitlines()]
    
    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each
    #chunks = [phrase.strip() for line in lines for phrase in line.split("  ")]
    
    def chunk_space(chunk):
        chunk_out = chunk + ' ' # Need to fix spacing issue
        return chunk_out

    #print('Going for text!')
    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') 
    # Get rid of all blank lines and ends of line
    # Now clean out all of the unicode junk (this line works great!!!)
    #print('cleaning out unicode junc from text!')
    try:
        text = text.decode('unicode_escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted
    except:                                                            # in a way that this works, can occasionally throw
        return                                                         # an exception

    #print('getting rid of non-words from text!')
    text = re.sub(b"[^a-zA-Z.+3]",b" ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                                # Also include + for C++
    #print('make text lower case!')
    text = text.lower()  # Go to lower case
    #print('split text!')
    text = text.split()  #  and split them apart
    #print('removing stop words!')
    text = [w for w in text if not w in stopws]
    #print('set of text')
    text = list(set(text)) # Last, just get the set of these. Ignore counts
                           # we are just looking at whether a term existed or not on the website

    #print("We are done! Let's return it!")
    return text


##############################################################################

def string_from_text(pattern, tmp_txt):
    lst  = tmp_txt.split('\n')
    hq = [''.join(x.split()[0:]) for x in lst if x.find(pattern) !=-1][0]
    #hq will have the pattern attached to the headquarter location
    print( hq )
    return(hq[len(pattern):]) #returns a substring starting from where the last index of pattern ends

##############################################################################

def do_stuff(a):
    return (a[0],a[1].text.split('\n')[0:4])

##############################################################################

def do_new_stuff(a):
    print("I'm in do_new_stuff")
    if len(a) ==0:
        print('object is empty')

    tmp = a[1].text
    raw_rating = re.findall('\d\.\d',tmp )
    print('raw_rating = ',raw_rating)
    if len(raw_rating)==1:
        rating =raw_rating[0]
    else:
        rating = ''
    raw_sal_range = re.findall('\d+k',tmp )
    print('raw_sal_range = ',raw_sal_range)
    if len(raw_sal_range)==2:
        sal_low = int(raw_sal_range[0].replace('k',''))
        sal_high = int(raw_sal_range[1].replace('k',''))
    else:
        sal_low = np.nan
        sal_high = np.nan
    raw_company = re.findall('.+–.+,.+',tmp)
    print('raw_company = ',raw_company)
    if len(raw_company)==1:
        tt = raw_company[0].split('–')
        company = tt[0].strip()
        job_city = tt[1].split(',')[0].strip()
        job_state_code = tt[1].split(',')[1].strip()
    else:
        company = ''
        job_city = ''
        job_state_code = ''
    raw_position = re.findall('(.+sci.+|.+ana.+|.+eng.+)',tmp.lower())
    print('raw_position = ',raw_position)
    if len(raw_position)==1:
        position = raw_position[0]
    else:
        position = tmp.split('\n')[1].lower()
    #return (a[0],tmp[0:4])
    print('Will go out of do_new_stuff.')
    return (a[0],[rating, position, company, job_city, job_state_code, sal_low, sal_high])

##############################################################################

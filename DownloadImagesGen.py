from bs4 import BeautifulSoup
import re
import requests

from datetime import datetime

# the imageUrl from where the images are to be 
# downloaded.
imageUrl = 'https://sports.ndtv.com/cricket/vinod-rai-says-incorrect-to-think-nobody-held-virat-kohli-responsible-for-world-cup-2019-loss-2105227'

# get the response from the url
response =  requests.get(imageUrl)

# beautifulSoup used to parse the html 
# file i.e. to extract data from the html file
soup = BeautifulSoup(response.text,'html.parser')

# just to check the HTML code
# print(soup)

# As we are concered with the img file we
# extract all the tags which contains img
imgTags = soup.find_all('img')

# getting the url of the img and storing 
# it in a list.
urls = [img['src'] for img in imgTags]

fObj = open('Logs/Logs.txt','a')

# for each URL
for url in urls:
    # w --> word character i.e. alphanumeric or underscore
    # should end with jpg gif o png
    # a list of filename which matches the given pattern 
    # in url
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)

    # if any such filname exits
    if filename:

        # open the file which matches
        with open('Images/' + filename.group(1), 'wb') as f:

            # if the image is in sub folder it will not 
            # contain the complete link so we need to 
            # append it with the url
            if 'http' not in url:

                # complete link to the image
                url = '{}{}'.format(imageUrl, url)
            # get response from the actual image Url
            response = requests.get(url)
            # writing content our image file
            f.write(response.content)
            
            # to create log file

            # current date and time
            dateTimeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            myLog = dateTimeNow + " : " + filename.group(1) + " downloaded.\n"

            # writing logs
            fObj.write(myLog)
            print(myLog)
fObj.close()
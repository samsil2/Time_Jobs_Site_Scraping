import time
import requests
from bs4 import BeautifulSoup

unSkills = input("Put unfamiliar skills: ")
print(f'filtering out unfamiliar skills: {unSkills}')

def findJob():
    #url
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').content

    #html parsing
    soup = BeautifulSoup(html_text,'html.parser')

    #jobs finds
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        date = job.find('span', class_="sim-posted").span.text
        if '2' or '3' or '4' in date:
            #company name fetching
            companyName = job.find('h3', class_='joblist-comp-name').text.strip()
            #skills fetching
            skills = job.find('span', class_="srp-skills").text.strip()
            #url
            moreInfo = job.header.h2.a['href']

            #filtering, print info & save info on files
            if unSkills not in skills:
                with open(f'files/{index}.txt', 'w') as f:
                    f.write(f'company name: {companyName} \n')
                    f.write(f'Required Skills: {skills} \n')
                    f.write(f'more info: {moreInfo} \n')
                print(f"File created...: {index}")

#main driver
if __name__== '__main__':
    while True:
        findJob()
        print(f'wating time: 5 min...')
        time.sleep(300)

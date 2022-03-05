
import requests
from bs4 import BeautifulSoup
from time import sleep
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
query = "uet lahore"
search = query.replace(' ', '+')
results = 10
url = (f"https://www.google.com/search?q={search}&num={results}")

driver = webdriver.Chrome()
driver.get("http://www.google.com")
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys(query)
# Clears the entered text
requests_results=driver.get(url)
# time.sleep(2);
print(requests_results)
# requests_results = requests.get(url)
# soup_link = BeautifulSoup(requests_results.content, "html.parser")
# links = soup_link.find_all("a")
# results=list()
# for link in links:
#     link_href = link.get('href')
#     if "url?q=" in link_href and not "webcache" in link_href:
#       title = link.find_all('h3')
#       if len(title) > 0 :
#          testlink = link.get('href').split("?q=")[1].split("&sa=U")[0]
#          test_list = ['youtube.com', 'wikipedia.org','investopedia.com','facebook.com','linkedin.com','.pdf','maps.google']
#          test_result = [ele for ele in test_list if(ele in testlink)]
#          if bool(test_result)==False:
#           mainlink=link.get('href').split("?q=")[1].split("&sa=U")[0]
#           maintitile=title[0].getText()
#           r={
#              "link":mainlink,
#              "title":maintitile}
#           results.append(r)

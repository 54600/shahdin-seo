
import rewrite_article
import requests
from bs4 import BeautifulSoup
from time import sleep
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def search_results(q):
    query = q
    search = query.replace(' ', '+')
    results = 10
    # url = (f"https://www.google.com/search?q={search}&num={results}")
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    SearchInput = driver.find_element(By.NAME, "q")
    SearchInput.send_keys(query+ Keys.ENTER)
    result = driver.find_element_by_id('res')
    elements=result.find_elements_by_css_selector(".yuRUbf a")
    results=list()
    for element in elements:
        link = element.get_attribute('href')
        try:
         title = element.find_element(By.TAG_NAME,"h3").text        
         test_list = ['google.com','youtube.com', 'wikipedia.org','investopedia.com','facebook.com','linkedin.com','.pdf','maps.google','github.com']
         test_result = [ele for ele in test_list if(ele in link)]
         if bool(test_result)==False and title!='':
          r={"link":link,"title":title}
          results.append(r)
        except:
            title=''
         
    driver.close();
    return results

def search_paragraph(url):
    brand="Brand"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    paragraph=list();
    paragraphtext=""
    t=soup.find("title").text
    for i in soup.find_all("p"):
        if len(i.text.split())> 20:
         paragraph.append(i.text)
         paragraphtext=paragraphtext+i.text
    content=paragraphtext.lower()
    url_split = url.split(".")
    content = content.replace(url,brand)
    content = content.replace(url_split[1],brand)
    content = content.replace('&','and')
    
    # spincontent=rewrite_article.plagiarism_removal(content)
    result={
        "link":url,
        "title":t,
        "paragraph":content,
        # "spin_paragraph":content,
    }
    return result
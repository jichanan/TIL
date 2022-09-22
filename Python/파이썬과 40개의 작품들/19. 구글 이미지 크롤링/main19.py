#!/usr/bin/env python
# coding: utf-8

# In[17]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp?hl=ko&ogbl'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[18]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[19]:


import time
elem = driver.find_element(By.TAG_NAME, "body")
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    driver.find_element(By.CSS_SELECTOR, "#islmp > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input").click()

    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[21]:


links = []
images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")
for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print('찾은 이미지 개수: ', len(links))


# In[23]:


import urllib.request

for k,i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "C:\\Users\\user\\Desktop\\작업\\TIL\\Python\\파이썬과 40개의 작품들\\19. 구글 이미지 크롤링\\사진다운로드"+str(k)+".jpg")

print("다운로드 완료하였습니다.")


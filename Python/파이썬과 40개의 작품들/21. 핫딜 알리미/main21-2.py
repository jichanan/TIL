from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

send_message_list = []

while True:
    try:
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
        message = ""
        for i in range(len(titles)):
            if "두유" in titles[i].text:
                message = titles[i].text + urls[i].get_attribute('href')
                print(message)
                token = '봇 api 토큰 입력' 
                id = '채팅방 고유 id 입력'
                bot = telegram.Bot(token)
                bot.sendMessage(chat_id=id, text=message)
        time.sleep(60.0 * 5)
    except KeyboardInterrupt:
        break
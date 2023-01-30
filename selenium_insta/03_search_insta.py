from selenium import webdriver
import chromedriver_autoinstaller # 크롬 오토 드라이버
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)  # 로딩 기달리는 시간 3초 빠르면 주석 처리 해도 됨

url = 'https://www.instagram.com/'
driver.get(url=url)

# 로그인
xpath = '//*[@id=”loginForm”]/div/div[1]/div/label/input'

id = os.getenv('INSTA_ID')
passwd = os.getenv('PW')

input_id = driver.find_element(By.XPATH, '//*[@id=”loginForm”]/div/div[1]/div/label/input') # 위치
input_id.send_keys(id) # 입력

driver.find_element(By.XPATH,'//*[@id=”loginForm”]/div/div[2]/div/label/input').send_keys(passwd) # 한줄 표현

driver.find_element(By.XPATH,'//*[@id="mount_0_0_Va"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/div/div[1]/button').click() # 한줄 표현
driver.find_element(By.XPATH,'//*[@id="mount_0_0_Va"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/div/div[1]/button').send_keys(Keys.ENTER) # 한줄 표현

# Search
hashtag = str(input())
url = f'https://www.instagram.com/explore/tags/{hashtag}/' # url로 검색
driver.get(url=url)
print(driver.page_source) # 페이지 소스 보기

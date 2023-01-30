from selenium import webdriver
import chromedriver_autoinstaller # 크롬 오토 드라이버
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)  # 로딩 기달리는 시간 3초 빠르면 주석 처리 해도 됨

url = 'https://www.instagram.com/'
driver.get(url=url)
time.sleep(20)  # 20초 잠듬 유지
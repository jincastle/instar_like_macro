from selenium import webdriver
import chromedriver_autoinstaller  # 크롬 오토 드라이버
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
def login(id, password):
    input_id = driver.find_element(By.XPATH, '//*[@id=”loginForm”]/div/div[1]/div/label/input')  # 위치
    input_id.send_keys(id)  # 입력

    driver.find_element(By.XPATH, '//*[@id=”loginForm”]/div/div[2]/div/label/input').send_keys(password)  # 한줄 표현

    # driver.find_element(By.XPATH,'//*[@id="mount_0_0_Va"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/div/div[1]/button').click() # 한줄 표현
    driver.find_element(By.XPATH,
                        '//*[@id="mount_0_0_Va"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/div/div[1]/button').send_keys(
        Keys.ENTER)  # 한줄 표현


# Search
def search(hashtag, scroll_times):
    url = f'https://www.instagram.com/explore/tags/{hashtag}/'  # url로 검색
    driver.get(url=url)
    # print(driver.page_source) # 페이지 소스 보기
    # scroll
    for _ in range(2):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)


# 좋아요 댓글 달기
def like_comment(nth, comment, repeat=3):
    # 게시판 클릭
    row = (nth - 1) // 3 + 1  # 인스타 원하는 걸 찾는 로직
    col = (nth - 1) % 3 + 1  # 인스타 원하는 걸 찾는 로직
    xpath = f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[5]/div[1]/a/div[{row}]/div[{col}]'
    driver.find_element(By.XPATH, xpath).click()
    for _ in range(repeat):
        # 좋아요 클릭
        like_xpath = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[1]/div[3]/div[1]/div/article[1]/div/div[3]/div/div/section[1]/span[1]/button/div[2]/span/svg'
        driver.find_element(By.XPATH, like_xpath).click()

        # 댓글 입력
        comment_xpath = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[1]/div[3]/div[1]/div/article[1]/div/div[3]/div/div/section[3]/div/form/textarea'
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)
        # 엔터
        # driver.find_element(By.XPATH, comment_xpath).end_keys(Keys.ENTER)
        # 클릭
        comment_button_xpath = ''
        driver.find_element(By.XPATH, comment_button_xpath).click()

        # 다음 게시물
        next_button_xpath = '/html/body/다음버튼'
        driver.find_element(By.XPATH, next_button_xpath).click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    id = os.getenv('INSTA_ID')
    passwd = os.getenv('PW')

    hashtag = str(input('검색할 해쉬태그 입력좀'))
    scroll_times = int(input('스크롤 몇번 내릴꺼야'))


    nth = int(input('몇번째 게시물?'))
    comment = str(input('댓글내용'))
    repeat = int(input('반복 횟수'))

    login(id,passwd)
    time.sleep(5)

    search(hashtag, scroll_times)
    time.sleep(5)

    like_comment(nth, comment, repeat)






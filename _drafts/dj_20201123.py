from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import numpy as np
import os

import pandas as pd
from bs4 import BeautifulSoup
import time
import re
# =COUNTIF(E:E,"판매중")
input = '조커'
selection = 2
"""selection = {'선택없음': 1, '매장명': 2, '매장번호': 3, 
'업주ID': 4, '업주번호': 5, '담당MD': 6 , '대행업체': 7}"""

driver = webdriver.Chrome()
url = 'https://auth.wmpo.co.kr/signin?redirectUrl=https://admin.wmpo.co.kr/manager/signin&clientID=hniaizj2uvfl13rpsahvsfdov6rkpulx'
# driver.maximize_window()
driver.get(url)
action = ActionChains(driver)

action.send_keys('2020050014').perform()  # 아이디 입력
driver.find_element_by_css_selector('.input-group').click()
driver.find_element_by_id('password').send_keys('wemakeprice123!')
driver.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-block').click()  # sign in 버튼 클릭
driver.implicitly_wait(1)

wait = WebDriverWait(driver, 25)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menuTree"]/div/div/ul/li[2]/ul/li[3]').click()  # 왼쪽패널 배달매장조회 클릭

wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.Spinner_visible__wyc4m')))
time.sleep(1)
driver.find_element_by_id('keywordKey').click()  # 키워드 선택없음


driver.find_element_by_xpath(f'//*[@id="keywordKey"]/option[' + str(selection) + ']').click()  # 오른쪽 패널 검색 툴

driver.find_element_by_id('keywordValue').click()
driver.find_element_by_id('keywordValue').send_keys(input)
driver.find_element_by_id('keywordValue').send_keys(Keys.ENTER)
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.Spinner_visible__wyc4m')))
time.sleep(1)
"""
위에까지 로그인하고, 
왼쪽 패널에 '배달 매장 조회'버튼 클릭하고 
오른쪽 키워드에 md이름을 넣고엔터까지
"""

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

rts = []
rt_ids = []
rt_numbers = [] #업주번호
statuses = [] #상태
enrollment_statuses = [] #매장등록상태

while True:
    try:
        for i in range(1,21):
            rt = driver.find_element_by_xpath(f'//*[@id="mArticle"]/div/div[2]/div/table/tbody/tr[{i}]/td[2]').text
            rt_id = driver.find_element_by_xpath(f'//*[@id="mArticle"]/div/div[2]/div/table/tbody/tr[{i}]/td[4]').text
            rt_number = rt_id[-6:-1]
            rt_number = "".join(re.findall("\d", rt_number))
            rt_id = rt_id[:-8]

            status = driver.find_element_by_xpath(f'//*[@id="mArticle"]/div/div[2]/div/table/tbody/tr[{i}]/td[8]').text
            enrollment_status = driver.find_element_by_xpath(f'//*[@id="mArticle"]/div/div[2]/div/table/tbody/tr[{i}]/td[9]').text
            print(rt, rt_id, rt_number, status, enrollment_status)

            rts.append(rt)
            rt_ids.append(rt_id)
            rt_numbers.append(rt_number)
            statuses.append(status)
            enrollment_statuses.append(enrollment_status)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[ng-click='detail(data.companyID)']"))).click()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.Spinner_visible__wyc4m')))


        continue
    except NoSuchElementException:
        print("""\n
        추가매장없음
        """)
        break

print(len(rts))

results = [rts, rt_ids, rt_numbers, statuses, enrollment_statuses]
data = pd.DataFrame(results)
tran = pd.DataFrame(results) #편의상 data 변수를 tran 변수로 바꾸려고 생성한 문자열
tran = tran.transpose()
tran.columns = ['매장명', 'ID', '업주번호', '상태', '등록상태']
tran.to_excel('DJlist.xlsx')

driver.close()
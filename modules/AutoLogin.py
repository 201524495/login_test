from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

from Run import *


def autoLogin(game_name, game_numbers, game_leader, game_start,
              game_end, game_year, game_month, game_day, first_number, second_number):
    try:
        import sys, os.path, time

        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            driver = webdriver.Chrome(chromedriver_path)
        else:
            driver = webdriver.Chrome()
        # driver = webdriver.Chrome('chromedriver.exe')
        delay_time = 3
        driver.implicitly_wait(delay_time)

        url = 'https://lend.pusan.ac.kr/grand/login.asp'
        driver.get(url)

        id = "pnucse1"
        pw = "0513116"

        # ID and PW INPUT
        driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
        driver.execute_script("document.getElementsByName('password')[0].value=\'" + pw + "\'")

        # Click the "SEND" button
        driver.find_element_by_xpath(
            '/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[14]/td/input').click()

        # Click the "입력하기" button
        driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/a/img').click()

        # Check the "OK_Check_Box"
        driver.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input').click()

        # Click the "SEND" button
        driver.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/div/input').click()

        #  "사용일자" INPUT
        #  Select statement
        # Year = "2021"
        Year = game_year
        # Month = "7"
        Month = str(int(game_month))
        print(Month)
        # Day = "30"
        Day = str(int(game_day))

        ddelement = Select(driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/select[2]'))
        ddelement.select_by_value(Month)

        if int(Month) < 10:
            Month = "0" + Month

        if int(Day) < 10:
            Day = "0" + Day

        day = Year + "-" + Month + "-" + Day

        ddelement = Select(driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/select[3]'))
        ddelement.select_by_value(day)

        #  "사용시간" INPUT
        # start_time = "13"
        start_time = game_start
        # end_time = "15"
        end_time = game_end
        ddelement = Select(driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select[1]'))
        ddelement.select_by_value(start_time)

        running_time = int(end_time) - int(start_time)
        ddelement = Select(driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select[2]'))
        ddelement.select_by_index(running_time)

        #  "행사명" INPUT
        # Name = "친선경기"
        Name = game_name
        driver.execute_script("document.getElementsByName('strtitle')[0].value=\'" + Name + "\'")

        #  "인원수" INPUT
        # Number = "22"
        Number = game_numbers
        driver.execute_script("document.getElementsByName('intNum')[0].value=\'" + Number + "\'")

        #  "책임자" INPUT
        # leader = "페가수스"
        leader = game_leader
        driver.execute_script("document.getElementsByName('strname')[0].value=\'" + leader + "\'")

        #  "휴대전화번호" INPUT
        # first_phone_number = "1234"
        first_phone_number = first_number
        driver.execute_script("document.getElementsByName('strPhone1_2')[0].value=\'" + first_phone_number + "\'")

        # second_phone_number = "5678"
        second_phone_number = second_number
        driver.execute_script("document.getElementsByName('strPhone1_3')[0].value=\'" + second_phone_number + "\'")

        # print(game_month)

        # Click the "입력하기" button
        # finish stage
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td/input').click()

    except Exception as e:
        print(e)
        pass

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('D:\chromedriver.exe')
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
driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[14]/td/input').click()

# Click the "입력하기" button
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/a/img').click()

# Check the "OK_Check_Box"
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input').click()

# Click the "SEND" button
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/div/input').click()


#  "사용일자" INPUT
#  Select statement
Year = "2021"
Month = "7"
Day = "30"
day = Year + "-0" + Month + "-" + Day

ddelement= Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/select[2]'))
ddelement.select_by_value(Month)


ddelement= Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/select[3]'))
ddelement.select_by_value(day)

#  "사용시간" INPUT
start_time = 13
ddelement= Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select[1]'))
ddelement.select_by_value(str(start_time))

ddelement= Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select[2]'))
ddelement.select_by_index(1)

#  "행사명" INPUT
Name = "친선경기"
driver.execute_script("document.getElementsByName('strtitle')[0].value=\'" + Name + "\'")

#  "인원수" INPUT
Number = "22"
driver.execute_script("document.getElementsByName('intNum')[0].value=\'" + Number + "\'")

#  "책임자" INPUT
leader = "페가수스"
driver.execute_script("document.getElementsByName('strname')[0].value=\'" + leader + "\'")

#  "휴대전화번호" INPUT
first_phone_number = "1234"
driver.execute_script("document.getElementsByName('strPhone1_2')[0].value=\'" + first_phone_number + "\'")

second_phone_number = "5678"
driver.execute_script("document.getElementsByName('strPhone1_3')[0].value=\'" + second_phone_number + "\'")


# Click the "입력하기" button
# finish stage
##driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td/input').click()
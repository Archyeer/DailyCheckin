# .由杨辰逸版权所属，请勿照抄，多多思索。
# import time
# import option

# from selenium import webdriver

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# 5
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

driver = Chrome(options=opt)

# driver = webserver.Chrome()
driver.get('http://yqfk.xjau.edu.cn/SPCP/Web')


# 无头浏览器
# option.add_argument('--headless')
# option.add_experimental_option("detach", True)


# 登录 进入
driver.find_element_by_xpath('//*[@id="StudentId"]').send_keys('720180188')
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="Name"]').send_keys('181613')
# time.sleep(1)
text = driver.find_element_by_id('code-box').text
driver.find_element_by_xpath('//*[@id="codeInput"]').send_keys(text)
driver.find_element_by_xpath('//*[@id="Submit"]').click()
driver.find_element_by_xpath('//*[@id="platfrom1"]/a/img').click()



# 选择体温
# driver.find_element_by_xpath('//*[@id="Temper1"]')
driver.find_element_by_xpath('//*[@id="Temper1"]/option[4]').click()
# driver.find_element_by_xpath('//*[@id="Temper2"]')
driver.find_element_by_xpath('//*[@id="Temper2"]/option[6]').click()


# 提交
driver.find_element_by_xpath('//*[@id="SaveBtnDiv"]/div/button').click()

# driver.close()
driver.quit()
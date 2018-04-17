from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')
link = 'https://www.lazada.vn/'
browser.get(link)
register = browser.find_element_by_xpath("//a[@class='grey'")
print('...',register)
email = browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-email mod-input-email']//input").send_keys('pignobig2@gmail.com')
password = browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-password mod-input-password']//input").send_keys('123@HuyOCLCT')
rePassword = browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-re-password mod-input-re-password']//input").send_keys('123@HuyOCLCT')
name = browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-name mod-input-name']//input").send_keys('Huy OC')
register = browser.find_element_by_css_selector('.next-btn .next-btn-primary .next-btn-large')
register.click()
# print('...', email.text)
# browser.quit()
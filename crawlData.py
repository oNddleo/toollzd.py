from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
from openpyxl import load_workbook
from openpyxl import Workbook
import datetime


def readFile(fileName):
    f = open(fileName)
    links = []
    line = f.readline()
    # append line to links
    links.append(line)
    while line:
        line = f.readline()
        # append line to links
        links.append(line)
    f.close()
    return links


def writeFile(data):
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    # print('data=',data)
    wb = Workbook()
    ws = wb.active
    ws.append(['Tên', 'Giá cũ',  'Giá mới',
               'Giảm %', 'Khuyến mãi', 'Tình trạng', 'Link sản phẩm'])
    for row in data:
        ws.append(row)
    wb.save(date + '-products.xlsx')


def run():
    linkFile = readFile('links2.txt')
    for element in linkFile:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-infobars')
        display = Display(visible=0, size=(800, 600))
        display.start()

        browser = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        browser.get(element)
        elms = browser.find_elements_by_xpath("//a[@href]")
        links = []
        products = []
        for elm in elms:
            if elm.get_attribute("href").startswith(
                    'https://www.lazada.vn/products/'):
                links.append(elm.get_attribute("href"))
        print(len(links), ' links')
        # for link in links:
        link = 'https://www.lazada.vn/products/smart-tv-samsung-55-inch-full-hd-model-ua55m5520ak-den-hang-phan-phoi-chinh-thuc-i150505216-s158177525.html?mp=1'
        product = []
        browser.get(link)
        name = browser.find_element_by_xpath(
            "//div[@id='module_product_title_1']//h1[@class='pdp-product-title']").text
        try:
            oldPrice = browser.find_element_by_xpath(
                "//div[@class='origin-block']//span[@class=' pdp-price pdp-price_type_deleted pdp-price_color_lightgray pdp-price_size_xs']").text
        except NoSuchElementException:
            oldPrice = ' '

        price = browser.find_element_by_xpath(
            "//div[@class='pdp-product-price']//span[@class=' pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl']").text
        try:
            discount = browser.find_element_by_xpath(
                "//div[@class='origin-block']//span[@class='pdp-product-price__discount']").text
        except NoSuchElementException:
            discount = ' '

        try:
            promo = browser.find_element_by_xpath(
                "//div[@class='promotion-tag-item voucher has-arrow']//span[@class='tag-name']").text
        except NoSuchElementException:
            promo = 'Không có'
        try:
            out_of_stock = browser.find_element_by_xpath(
                "//div[@id='module_quantity-input']//div[@class='pdp-mod-product-info-section sku-quantity-selection']//div[@class='section-content']").text
        except NoSuchElementException:
            out_of_stock = ' '
        product.append(name)
        product.extend([oldPrice, price, discount,
                        promo, out_of_stock, link])

        products.append(product)
        writeFile(products)
    browser.quit()


run()

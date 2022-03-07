import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome("c:\\utils\\chromedriver.exe")
query = "오렌지쥬스"

# 로켓배송 상품만 가져오기
driver.get("https://www.coupang.com/np/search?rocketAll=true&q=" + query + "&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=364335&component=&rating=0&sorter=scoreDesc&listSize=72")

# 스크롤 위에서부터 아래까지 쭉 내려오기

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_xpath("//dt[@class='image']/img") # 상품 이미지 url
imgNames = driver.find_elements_by_xpath("//div[@class='descriptions-inner']/div[@class='name']") # 상품 제목 가져오기
imgPrice = driver.find_elements_by_xpath("//del[@class='base-price']") # 상품 가격 가져오기

count = 0

for image in images:
  try:
    imgUrl = image.get_attribute("src")
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgUrl, "cimages\\" + imgNames[count].get_attribute('innerText') + " - " + imgPrice[count].get_attribute('innerText') + "원.jpg")
    count = count + 1
  except:
    pass

driver.close()



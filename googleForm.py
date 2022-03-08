import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import urllib.request

driver = webdriver.Chrome("c:\\utils\\chromedriver.exe")
driver.get("https://forms.gle/Nsb1JyGsf7iQBPht8")

itemList = driver.find_elements_by_class_name("Qr7Oae")

# Use the following snippets to get elements by their class names
# textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
# radiobuttons = driver.find_elements_by_class_name("docssharedWizToggleLabeledContainer")
# checkboxes = driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")



textArea = "KHxj8b"

def answerForRadioButtons(questionItem, answer):
  radioOrCheckButtons = "docssharedWizToggleLabeledContainer"
  findedQuestion = questionItem.find_elements_by_class_name(radioOrCheckButtons)
  answer = answer - 1
  findedQuestion[answer].click()

def answerForCheckboxButtons(questionItem, answers):
  radioOrCheckButtons = "docssharedWizToggleLabeledContainer"
  findedQuestion = questionItem.find_elements_by_class_name(radioOrCheckButtons)
  for answer in answers:
    answer = answer - 1
    findedQuestion[answer].click()


def answerForInputText(questionItem, answer):
  inputText = "whsOnd"
  findedQuestion = questionItem.find_element_by_class_name(inputText)
  findedQuestion.send_keys(answer)


submitbutton = driver.find_element_by_xpath("//div[@class='lRwqcd']/div[@role='button']/span/span") # 제출 버튼 가져오기

time.sleep(0.5)

# 1번
answerForRadioButtons(itemList[0], 2)

# 2번
answerForInputText(itemList[1], "안뇽안뇽~66")

# 3번
answerForInputText(itemList[2], "안뇽안뇽~77")

# 4번
answerForInputText(itemList[3], "안뇽안뇽~88")

# 5번
answerForCheckboxButtons(itemList[4], [1,2,4])

# 제출
submitbutton.click()

driver.close()
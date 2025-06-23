import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


URL = "https://www.linkedin.com/jobs/search/?currentJobId=4251877298&f_AL=true&keywords=devops%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
EMAIL = "yupeng.100daysofcode@gmail.com"
PASSWORD = "Wyp5618256@"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
time.sleep(3)
sign_in_google = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_google.click()

time.sleep(3)
email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(PASSWORD)

sign_in = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in.click()
time.sleep(3)

save = driver.find_element(By.XPATH, value='//*[@id="jobs-apply-button-id"]')
save.click()
time.sleep(1)

mobel = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4251877298-21438008524-phoneNumber-nationalNumber"]')
mobel.send_keys("0635314494")

next =driver.find_element(By.XPATH, value='//*[@id="ember379"]')
next.click()
time.sleep(1)

next_2 =driver.find_element(By.XPATH, value='//*[@id="ember379"]')
next_2.click()
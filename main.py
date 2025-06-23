import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4251877298&f_AL=true&keywords=devops%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
EMAIL = "yupeng.100daysofcode@gmail.com"
PASSWORD = os.getenv("PASSWORD")

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

index = 0
while True:
    jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    if index >= len(jobs):
        print("No more jobs found.")
    for job in jobs:
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", job)
        time.sleep(1.5)
        job.click()
        time.sleep(2)
        try:
            save = driver.find_element(By.CSS_SELECTOR, value='.jobs-save-button__text')
            if save.text != "Saved":
                save.click()
                print("job saved")
        except NoSuchElementException:
            print("No save button, skipped")
            continue

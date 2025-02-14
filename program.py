import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Program:
   def __init__(self, crn):
       self.personalInfo = {
           'username': '<ITU PORTAL USERNAME>',
           'password': '<ITU PORTAL PASSWORD>',
       }
       self.crn = crn
       self.main()


   def main(self):
       driver = webdriver.Chrome(service=Service(webdriver_path='chromedriver.exe'))
       driver.get("https://girisv3.itu.edu.tr/Login.aspx")
       driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$tbUserName').send_keys(self.personalInfo['username'])
       driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$tbPassword').send_keys(self.personalInfo['password'])
       driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnLogin').click()
       driver.get('https://obs.itu.edu.tr/ogrenci/')
       WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div[2]/div[1]/ul/li[5]"))
       )
       driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div[1]/ul/li[5]").click()

       WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]"))
       )
       driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]").click()
       WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div/div[4]/div/form/div[1]/div/div[1]/div/input"))
       )
       driver.execute_script('javascript: !function(){var e=[' + f"'{self.crn}'" + '];let t=document.querySelectorAll("input[type=\'number\']"),n=0;t.forEach(t=>{(function e(t){let n=window.getComputedStyle(t);if("none"===n.display||"hidden"===n.visibility)return!1;let l=t.parentElement;for(;l;){let i=window.getComputedStyle(l);if("none"===i.display||"hidden"===i.visibility)return!1;l=l.parentElement}return!0})(t)&&n<e.length&&(t.value=e[n],t.dispatchEvent(new Event("input",{bubbles:!0})),n++)}),setTimeout(function(){let e=document.querySelector(\'button[type="submit"]:not([disabled])\');e&&e.click(),setTimeout(function(){let e=document.querySelector(".card-footer.d-flex.justify-content-end");if(e){let t=e.getElementsByTagName("button");t.length>1&&t[1].click()}},50)},50)}();')
       time.sleep(5)
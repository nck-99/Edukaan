from selenium import webdriver
from selenium.webdriver.common.by import By
import time

password = input("Enter password to be set::")
driver = webdriver.Chrome()
driver.get("https://ibpodev.home.tatamotors/edukaan_ui/#/")
driver.maximize_window()

class set_password:
    def set(self):
        driver.implicitly_wait(10)
        profile = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]/img")
        profile.click()
        time.sleep(5)
        if driver.title == "E-Dukaan | Login":
            print("customer login")
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[1]/input").send_keys("9145462369")
            send_otp_buttn = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/button")
            send_otp_buttn.click()
            driver.implicitly_wait(5)
            otp = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]")
            otp.send_keys("123456")
            driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[2]/button[1]").click()
            time.sleep(5)
            if driver.title == "E-Dukaan":
                time.sleep(10)
                driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[1]/div/ul/li[2]/img").click()
                set_pw = driver.find_element(By.CSS_SELECTOR, "#header-password")
                set_pw.click()
                time.sleep(5)
                if driver.title == "E-Dukaan | Set Password":
                    pw = driver.find_element(By.CSS_SELECTOR, "#checkout-Shop-name")
                    pw.click()
                    pw.send_keys(password)
                    pw_confirm = driver.find_element(By.CSS_SELECTOR, "#checkout-address")
                    pw_confirm.send_keys(password)
                    pw_confirm.click()
                    save = driver.find_element(By.CSS_SELECTOR, "#nav-Items > div > form > div > button")
                    save.click()
                    time.sleep(10)
                    confirm = driver.find_element(By.CSS_SELECTOR, "#toast-container")
                    if bool(confirm) == 1:
                        print("Password set successfully")

if __name__ == "__main__":
    pw = set_password()
    pw.set()
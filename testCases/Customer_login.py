import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

choice = input("do you wand to select random obj?::y/n-->")
Guest = input("are you a guest user?:y/n-->>")
#phno = int(input("Enter phone no."))
#addr1 = str(input("Enter address 1--->"))
#addr2 = str(input("Enter address 2--->"))
#pincode = int(input("Enter pincode--->"))
order = input("Do you want to order something?::y/n-->")
logout = input("Do you want to logout?::y/n-->")

driver = webdriver.Chrome()


driver.get("https://ibpodev.home.tatamotors/edukaan_ui/#/")
driver.maximize_window()
driver.implicitly_wait(3)
login = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]/img")
login.click()
driver.implicitly_wait(3)
if Guest == "n":
    if driver.title == "E-Dukaan | Login":
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[1]/input").send_keys("9145462369")
        send_otp_buttn = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/button")
        send_otp_buttn.click()
        driver.implicitly_wait(5)
        otp = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]")
        otp.send_keys("123456")
        driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[2]/button[1]").click()
        time.sleep(5)
        if choice == "y":
            product = driver.find_elements(By.CLASS_NAME, "ng-star-inserted")
            list(product)
            for p in product:
                print(p)
            pr = random.choice(product)
            action = webdriver.common.action_chains.ActionChains(driver)
            action.context_click(pr)
            print("random value is :", str(pr))
            time.sleep(10)

        if driver.title == "E-Dukaan":
            print("LOGIN Successful")
        else:
            assert False
else:
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/p[1]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[1]/input").send_keys(phno)
    submit = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[2]/button")
    submit.click()
    driver.implicitly_wait(6)
    driver.find_element(By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[1]/mat-form-field/div/div[1]/div/input").send_keys(name)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[3]/mat-form-field/div/div[1]/div/input").send_keys(addr1)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[4]/mat-form-field/div/div[1]/div/input").send_keys(addr2)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[5]/mat-form-field/div/div[1]/div[1]/input").send_keys(pincode)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[5]/mat-form-field/div/div[1]/div[2]/mat-icon").click()
    send_otp = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[2]/button")
    send_otp.click()
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]").send_keys("123456")
    password = "VSS@1234"
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div[1]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[3]/mat-form-field/div/div[1]/div[1]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[4]/button[1]").click()
    time.sleep(10)
if order == "y":
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/input").send_keys("wheel")
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/button/img").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[1]").click()
    #driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a"))
    add_cart = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
    action = ActionChains(driver)
    action.scroll_to_element(add_cart).click()
    #driver.execute_script("arguments[0].scrollIntoView();", add_cart)
    #driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#cart-details").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#view-all-items").click()
    driver.implicitly_wait(10)
    place_order = driver.find_element(By.CSS_SELECTOR, "#next_id > button")
    action = ActionChains(driver)
    action.scroll_to_element(place_order).click()
    time.sleep(10)

if logout == "y":
    driver.find_element(By.CSS_SELECTOR, "#user-details").click()
    out = driver.find_element(By.CSS_SELECTOR, "#header-logout")
    out.click()
    driver.implicitly_wait(6)
    driver.find_element(By.CSS_SELECTOR, "body > modal-container > div > div > app-logout > div.modal-footer.ng-star-inserted > button:nth-child(1)").click()
    time.sleep(5)
    print("LOGOUT Successful")



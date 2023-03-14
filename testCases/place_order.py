from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import random

#choice = input("Do you want to place order?::y/n-->")
order_name = input("Enter your order:")
driver = webdriver.Chrome()


driver.get("https://ibpodev.home.tatamotors/edukaan_ui/#/")
driver.maximize_window()
driver.implicitly_wait(10)
login = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]/img")
login.click()
driver.implicitly_wait(3)
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


    if driver.title == "E-Dukaan":
         print("LOGIN Successful")
    else:
         assert False

if bool(driver) == 1:
    driver.implicitly_wait(3)
    driver.find_element(By.NAME, "search").send_keys(order_name)
    search = driver.find_element(By.CLASS_NAME, "btn-search")
    search.click()
    product = driver.find_elements(By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div[2]/div[1]")
    product[0].click()
    print(len(product))
    driver.implicitly_wait(6)
    try:
        add = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
        action = ActionChains(driver)
        action.scroll_to_element(add).click()
        confirm = driver.find_element(By.ID, "toast-container")
    except NoSuchElementException:
        print("Order Incomplete")
        pass

    if bool(confirm) == 1:
        print("Order added to cart")
        driver.implicitly_wait(3)
        cart = driver.find_element(By.ID, "cart-details")
        cart.click()
        driver.implicitly_wait(6)
        driver.find_element(By.ID, "view-all-items").click()
        time.sleep(10)
        next_bttn = driver.find_element(By.CSS_SELECTOR, "#next_id > button")
        print("next element:", next_bttn)

        action = ActionChains(driver)
        action.scroll_to_element(next_bttn).click()
        time.sleep(10)
        try:
            offer = driver.find_element(By.ID, "swal2-html-container")
            if bool(offer) == 1:
                driver.find_element(By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline").click()
                driver.find_element(By.CSS_SELECTOR, "#edukaan-offer-section > div.card.h-100.shadow.mt-2.show-for-desktop.ng-star-inserted > div > div.col-3.col-sm-5.ng-star-inserted > button").click()
                driver.find_element(By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline")
        except NoSuchElementException:
             print("No offer available")
             pass
        payment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary text-uppercase mat-action-btn mat-next mat-p-to-p")))
        print("payment values:", payment)
        action.scroll_to_element(payment).click()
        time.sleep(10)
    else:
        print("Failed to add Order")


time.sleep(10)
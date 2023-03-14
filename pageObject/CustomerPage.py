from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://edukaan.home.tatamotors/#/")

driver.implicitly_wait(5)

user_proile = driver.find_element(By.XPATH, "")
menu = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[1]/div/div[1]/a")
popular_models = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[1]/a/span")
durafit = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[2]/a/span")
prolife = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[2]/a/span")
oil_grese = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[4]/a/span")
fast_consumables = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[5]/a/span")
service_kit = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[6]/a/span")
offers = driver.find_element(By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/app-menu/div/div[2]/ul/li[7]/a/span")




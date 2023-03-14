import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
class UserRegistration:
        User_option = driver.find_element(By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/ul/li[4]")
        Registration = driver.find_element(By.XPATH, "/html/body/app-root/app-adminlayout/app-user-registration/section/div/button")
        Contractor_radio_butn = driver.find_element(By.CLASS_NAME, "form-chk-list")
        Status_bar = driver.find_element(By.CLASS_NAME, "mat-slide-toggle-thumb")
        Type_dropdwn = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[3]/ng-select/div")
        Role_dropdwn = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[4]/ng-select/div/div/div[2]/input")
        Fname_txtbx = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[5]/input")
        Lname_txtbx = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[6]/input")
        Phnum_txtbx = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[8]/input")
        Email_txtbx = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[9]/input")

        def __int__(self, driver):
                driver=self.driver

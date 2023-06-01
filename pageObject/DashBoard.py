import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage


class Dashboard(BasePage):

    DashBoard = (By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/ul/li[1]/a")
    Refresh = (By.XPATH, "/html/body/app-root/app-adminlayout/app-home/section/div/div[1]/div[1]/ul/div/ul/span")
    Filter = (By.ID, "filterPopup")
    Today_Filter = (By.ID, "kk")
    Filter_7days = (By.ID, "mm")
    Filter_30days = (By.ID, "xx")
    Filter_90days = (By.ID, "zz")
    Filter_LastYear = (By.ID, "aa")
    Filter_Quater  = (By.ID, "bb")
    Filter_Custom = (By.ID, "uu")
    From_date = (By.XPATH, "/html/body/app-root/app-adminlayout/app-home/section/div/div[1]/div[1]/ul/div/div/div/form/div/div/div[1]/div/li[8]/div/div[1]/div/div/div/button")
    To_date = (By.XPATH, "/html/body/app-root/app-adminlayout/app-home/section/div/div[1]/div[1]/ul/div/div/div/form/div/div/div[1]/div/li[8]/div/div[2]/div/div/div/button")


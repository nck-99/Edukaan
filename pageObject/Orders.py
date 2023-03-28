import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class OrdersPage(BasePage):

    User_Details = (By.ID, "user-details")
    Order_History = (By.ID, "header-order-history")
    Search_OTC = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/ecom-orders/div/nav/div/div/div[1]/input")
    Part_Search = (By.ID, "header-paste-search")

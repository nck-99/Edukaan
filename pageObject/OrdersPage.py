import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pageObject import WhishList
class Orders(BasePage):
    Part_Search = (By.ID, "header-paste-search")
    User_Details = (By.ID, "user-details")
    Add_Cart = (By.XPATH, "/html/body/div/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
    Cart = (By.ID, "cart-details")
    View_Cart = (By.ID, "view-all-items")
    Order_History = (By.ID, "header-order-history")
    Search_OTC = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/ecom-orders/div/nav/div/div/div[1]/input")

    def add_to_cart(self, setup):
        wl = WhishList.Whish_List(setup)
        wl.search_part()
        wl.select_part()
        self.find_element(self.Add_Cart).click()

    def verify_add_cart(self, setup):
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        print(msg)



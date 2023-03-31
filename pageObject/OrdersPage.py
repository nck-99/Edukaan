import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from pageObject import WhishList
from pageObject import SETPassword
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Orders(BasePage):
    Part_Search = (By.ID, "header-paste-search")
    User_Details = (By.ID, "user-details")
    Add_Cart = (By.XPATH, "/html/body/div/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
    Cart = (By.ID, "cart-details")
    Clear  = (By.CLASS_NAME, "clear")
    Clear_All = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/div[2]/div/p[3]/span")
    Confirm_Clear = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    View_Cart = (By.ID, "view-all-items")
    Order_History = (By.ID, "header-order-history")
    Search_OTC = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/ecom-orders/div/nav/div/div/div[1]/input")
    Verify_empty_cart = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div")
    Next_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[4]/mat-card/div[3]/button")
    Proceed_to_payment = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-address/div/form/fieldset/div/div[2]/mat-card/div[5]/button[2]")
    Apply_cupon = (By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
    GST_popup = (By.XPATH, "/html/body/modal-container/div/div/gst-permmission/div/div/div[2]/button[2]")
    Terms_Conditions = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-payment/div/form/fieldset/div/div[2]/mat-card/div[5]/mat-checkbox/label/div")
    Place_Order = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-payment/div/form/fieldset/div/div[2]/mat-card/div[6]/button[2]")
    Wallet_payment = (By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div[3]/form/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div/button[4]/div")
    def add_to_cart(self, setup, item):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part(item)
        wl.select_part()
        self.find_element(self.Add_Cart).click()

    def verify_add_cart(self, setup):
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        print("########", msg)
        a = "added to cart"
        b = "Product already exist."
        if a in msg:
            return True
        elif b in msg:
            return True
        else:
            return False

    def remove_from_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        time.sleep(5)
        self.find_element(self.Cart).click()
        time.sleep(5)
        clr = self.find_all_elements(self.Clear)
        for c in clr:
            c.click()
            time.sleep(5)

    def verify_remove_cart(self):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        time.sleep(3)
        msg = self.find_element(self.Verify_empty_cart).text
        print(msg)
        check = "shopping cart is empty"
        if check in msg:
            return  True
        else:
            return False
    def empty_cart(self, setup):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        time.sleep(3)
        self.find_element(self.Clear_All).click()
        self.find_element(self.Confirm_Clear).click()
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        if "Cleared all cart successfully" in msg:
            return True
        else:
            return False

    def place_order(self):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.find_element(self.Next_button).click()

    def apply_cupon(self):
        try:
            cupon = self.find_element(self.Apply_cupon)
            cupon.click()
        except NoSuchElementException:
            pass

    def move_to_payment(self, setup):
        self.find_element(self.Proceed_to_payment).click()
        self.find_element(self.GST_popup).click()
        self.driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        self.find_element(self.Terms_Conditions).click()
        self.find_element(self.Proceed_to_payment).click()
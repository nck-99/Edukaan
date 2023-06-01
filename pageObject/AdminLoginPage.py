import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage

class LoginPage(BasePage):

    User_Name_txt = (By.NAME, "name")
    Password_txt = (By.NAME, "psw")
    Sign_In_button = (By.XPATH, "/html/body/app-root/app-auth-layout/div/app-login/div/div[2]/div/form/button")
    Log_Out_button = (By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/div/a/span")
    Confirm_logout = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[3]/button[2]")
    Container_Msg = (By.XPATH, "/html/body/div[2]/div/div[2]")
    PopUp = (By.XPATH, "/html/body/div[4]/div/div[6]/button[1]")
    PopUpMsg = (By.ID, "swal2-html-container")
    LoginID = (By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div")

    def enter_user_name(self, uname):
        self.find_element(self.User_Name_txt).send_keys(uname)

    def enter_password(self, pwd):
        self.find_element(self.Password_txt).send_keys(pwd)

    def click_sign_in(self):
        self.find_element(self.Sign_In_button).click()

    def logout(self):
        self.find_element(self.Log_Out_button).click()
        self.wait(10)
        self.find_element(self.Confirm_logout).click()

    def pop_up_msg(self):
        msg = self.find_element(self.PopUpMsg)
        print(msg.text)
        return msg


    def pop_up_ok(self):
        self.find_element(self.PopUp).click()

    def verify_login(self):
        ID = self.find_element(self.LoginID)
        id_txt = ID.text
        print("User_ID : ", id_txt[:28])
        if "(TML)" or "(Distributor)" in id_txt[:28]:
            return True
        else:
            return False

    def TML_login(self):
        self.enter_user_name("SSV533008")
        self.enter_password("Tml@062323")
        self.click_sign_in()
        time .sleep(5)
        assert self.verify_login() == True

    def Distributor_login(self):
        self.enter_user_name("ZWANI_2080120")
        self.enter_password("Sapr#2023")
        self.click_sign_in()
        time.sleep(5)
        assert self.verify_login() == True
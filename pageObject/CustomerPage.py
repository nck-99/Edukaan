import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures()
class BasePage():
    def __init__(self, setup):
        self.driver = setup

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find (self, locator):
        return self.driver.find_element(locator)

    def locate_by_invisibility(self, locator):
        return EC.invisibility_of_element_located(locator)

    def wait (self, time):
        return self.driver.implicitly_wait(time)

    def current_url(self):
        return self.driver.current_url


class LoginPage(BasePage):
    LOGIN = (By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]/img")
    OTP_radio = (By.ID, "OTP")
    PASSWORD_radio = (By.ID, "Password")
    MOBILE_NO_txtbox = (By.ID, "mat-input-0")
    OTP_txtbox = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]")
    Send_OTP = (By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/button")
    PASSWORD_txtbox = (By.ID, "mat-input-3")
    NEXT_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[2]/button[1]")
    VERIFY = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]")
    PROFILE = (By.ID, "user-details")
    Logout_button = (By.ID, "header-logout")
    Confirm_logout = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    Logout_err_msg = (By.ID, "toast-container")
    def select_Login(self):
        self.find_element(self.LOGIN).click()

    def enter_mobileno(self, mobno):
        self.find_element(self.MOBILE_NO_txtbox).clear()
        self.find_element(self.MOBILE_NO_txtbox).send_keys(mobno)


    def enter_otp(self, otp):
        self.find_element(self.OTP_txtbox).send_keys(otp)

    def click_send_otp(self):
        self.find_element(self.Send_OTP).click()

    def enter_password(self, mobno, pwd):
        self.find(self.PASSWORD_radio).click()
        self.find_element(By.ID, "mat-input-2").sendkeys(mobno)
        self.find_element(self.PASSWORD_txtbox).send_keys(pwd)

    def click_next(self):
        self.find_element(self.NEXT_button).click()

    def verify_login(self):
        self.wait(3)
        v = self.find_element(self.VERIFY)
        if bool(v) == 1:
            return True
        else:
            return False

    def user_details(self):
        self.find_element(self.PROFILE).click()

    def logout(self):
        self.find_element(self.Logout_button).click()
        self.find_element(self.Confirm_logout).click()

    def verify_logout(self):
        v = self.locate_by_invisibility(self.VERIFY)
        if self.current_url() == "https://ibpodev.home.tatamotors/edukaan_ui/#/" and bool(v) == 1:
            return True
        else:
            return False

    def login_error_msg(self):
        err = self.find_element(self.Logout_err_msg)
        if bool(err) == 1:
            return True
        else:
            return False


class UserRegistration(LoginPage):
    Registration = (By.LINK_TEXT, "Click here")


    def click_register(self):
        self.find_element(self.Registration).click()
import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys

class HolidayCalender(BasePage):
    Master = (By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/ul/li[9]")
    Holiday_Calender = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/app-submenu-list/div/ul/li[1]/a")
    Division = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[1]/ng-select/div/div/div[2]/input")
    Holiday_Name = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[2]/input")
    Holi_date = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[3]/input")
    Date = (By.TAG_NAME, "td")
    Add = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[4]/button[1]")
    Reset = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[4]/button[2]")
    AddOK = (By.XPATH, "/html/body/div[3]/div/div[6]/button[1]")
    Delete = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[3]/div[1]/div/div/div/table/tr[2]/td[9]/div")
    ConfirmDelete = (By.XPATH, "/html/body/div/div/div[6]/button[1]")
    DeleteOK = (By.XPATH, "/html/body/div/div/div[6]/button[1]")
    VerifyAdd = (By.XPATH, "/html/body/div[2]/div/h2")
    VerifyDelete = (By.XPATH, "/html/body/div[2]/div/h2")

    def click_master(self):
        self.find_element(self.Master).click()

    def click_holiday(self):
        self.find_element(self.Holiday_Calender).click()

    def select_division(self):
        self.find_element(self.Division).click()
        self.find_element(self.Division).send_keys("2080800-Parts-Bhiwandi-ParPvt_1-49RI1KH", Keys.ENTER)

    def enter_holiday_name(self):
        self.find_element(self.Holiday_Name).send_keys("TestFODemo")

    def select_date(self):
        self.find_element(self.Holi_date).click()
        time.sleep(5)
        d = self.find_all_elements(self.Date)
        for i in d:
            if i == d[58]:
                i.send_keys(Keys.ENTER)

    def add_holidate(self):
        self.find_element(self.Add).click()
        time.sleep(5)
        self.find_element(self.AddOK).click()

    def delete_holiday(self):
        self.find_element(self.Delete).click()

    def confirm_delete(self):
        self.find_element(self.ConfirmDelete).click()
        self.find_element(self.DeleteOK).click()

    def verify(self):
        a = self.find_element(self.VerifyAdd)
        print(a.text)
        return a.text


class ReturnPolicy(HolidayCalender):

    Return_policy = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/app-submenu-list/div/ul/li[2]/a")
    CreateReturnPolicy = (By.XPATH, "/html/body/app-root/app-adminlayout/app-return-policy/section/div[1]/div[1]/button")
    ReturnDays = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[3]/div[1]/input")
    StartDate = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/button")
    SelectDate = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[2]/div[2]/div/div/ngb-datepicker/div[2]/div/ngb-datepicker-month")
    RefundDays = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[3]/div[2]/input")
    Save = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[4]/button[2]")
    Confirm = (By.XPATH, "/html/body/div[3]/div/div[6]/button[1]")
    Verify = (By.TAG_NAME, "h2")

    def update_policy(self):
        self.click_master()
        time.sleep(5)
        self.find_element(self.Return_policy).click()
        self.find_element(self.CreateReturnPolicy).click()

    def create_return_policy(self):
        self.find_element(self.ReturnDays).send_keys("15")
        self.find_element(self.StartDate).click()
        self.find_element(self.SelectDate).click()
        self.find_element(self.RefundDays).send_keys("7")

    def save_policy(self):
        self.find_element(self.Save).click()
        time.sleep(5)
        self.verify_policy()
        self.find_element(self.Confirm).click()

    def verify_policy(self):
        a = self.find_element(self.Verify)
        print(a.text)

class Notification(ReturnPolicy):

    Notification = (By.XPATH, "/html/body/app-root/app-adminlayout/app-notification/app-submenu-list/div[1]/ul")
    AddNew = (By.XPATH, "/html/body/app-root/app-adminlayout/app-notification/section/div/button")
    FromDate = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/button")
    ToDate = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/button")
    CustomerType = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[4]/div[2]/ul/mat-checkbox[1]/label/div")
    SingleUpload = (By.ID, "customerSingle")
    Title = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[9]/div[2]/input")
    Message = (By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[10]/div[2]/angular-editor/div/div/div")

    def click_notification(self):
        self.click_master()
        time.sleep(10)
        a = self.find_element(self.Notification).click()

    def add_notification(self):
        self.find_element(self.AddNew).click()

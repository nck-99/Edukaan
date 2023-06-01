import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys

class HolidayCalender(BasePage):
    Master = (By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/ul/li[9]")
    Holiday_Calender = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/app-submenu-list/div/ul/li[1]/a")
    Division = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[1]/ng-select/div/div/div[3]/input")
    Holiday_Name = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[2]/input")
    Holi_date = (By.XPATH, "")
    Date = (By.TAG_NAME, "tbody")
    Add = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[4]/button[1]")
    Reset = (By.XPATH, "/html/body/app-root/app-adminlayout/app-holiday-calender/section/div/div[1]/form/div/div[4]/button[2]")
    

    def click_master(self):
        self.find_element(self.Master).click()

    def click_holiday(self):
        self.find_element(self.Holiday_Calender).click()

    def select_division(self):
        self.find_element(self.Division).send_keys("2080120-Parts-Srinagar-SurajM_1-1IJGRE6")
        self.find_element(self.Division).send_keys(Keys.ENTER)

    def enter_holiday_name(self):
        self.find_element(self.Holiday_Name).send_keys("TestFODemo")

    def select_date(self):
        self.find_element(self.Holi_date).click()
        #self.find_element(self.Holi_date).send_keys("7/1/23")
        time.sleep(2)
        d = self.find_all_elements(self.Date)
        for a in d:
            print(a)
            print(a.text)
            for a.text in d == 1:
                a.click()

    def add_holidate(self):
        self.find_element(self.Add).click()
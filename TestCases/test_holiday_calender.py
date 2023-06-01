import time
from pageObject.Master import HolidayCalender
from pageObject.AdminLoginPage import LoginPage

class TestHolidayCalender:

    def test_create_holiday(self, setup):
        lp = LoginPage(setup)
        lp.Distributor_login()
        time.sleep(3)
        m = HolidayCalender(setup)
        m.click_master()
        m.wait(5)
        m.click_holiday()
        time.sleep(3)
        m.select_division()
        m.enter_holiday_name()
        m.select_date()
        time.sleep(5)
        m.add_holidate()


    def test_delete_holiday(self, setup):
        lp = LoginPage(setup)
        lp.Distributor_login()
        time.sleep(5)
        m = HolidayCalender(setup)
        m.click_master()
        m.click_holiday()
        m.delete_holiday()
        time.sleep(5)
        m.confirm_delete()


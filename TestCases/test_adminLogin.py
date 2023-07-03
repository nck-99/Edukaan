import time
import pytest
import openpyxl
from pageObject.AdminLoginPage import LoginPage
from Utilities.excel_methods import ExcelMethods

workbook = openpyxl.load_workbook('C:\Selenium\EdukaanAdmin.xlsx')

class Test_Login_Logout():
    @pytest.mark.parametrize('Test_Case_ID,Objective,User_name,Password,Condition,Expected_Results', ExcelMethods(workbook["Login"]).get_parametrize_list())
    def test_Login(self, setup, Test_Case_ID, Objective, User_name, Password, Condition, Expected_Results):
        ap = LoginPage(setup)
        ap.enter_user_name(User_name)
        ap.enter_password(Password)
        ap.click_sign_in()
        time.sleep(5)
        if ap.current_url() == "https://ibpodev.home.tatamotors/edukaan_Admin/#/pages/Dashboard":
            if ap.verify_login() == True:
                status = "TC PASSED"
            else:
                status = "TC FAILED"
        else:
            time.sleep(7)
            ap.pop_up_msg()
            status = "TC FAILED"

        ExcelMethods(workbook["Login"]).update_result_in_excel(Test_Case_ID, status)
        workbook.save("C:\Selenium\EdukaanAdmin.xlsx")

    def test_Logout(self, setup):
        ap = LoginPage(setup)
        ap.Distributor_login()
        time.sleep(7)
        ap.logout()
        time.sleep(5)
        assert ap.current_url() == "https://ibpodev.home.tatamotors/edukaan_Admin/#/session/Login"

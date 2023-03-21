import pytest
from pageObject import CustomerPage
from Utilities.excel_methods import ExcelMethods

class Test_Login_Logout_pos():
    @pytest.mark.parametrize('Test_Case_ID,Objective,Mobile_NO,OTP,Condition,Expected_Results', ExcelMethods("Login").get_parametrize_list())
    def test_Login(self, setup, Test_Case_ID, Objective, Mobile_NO, OTP, Condition, Expected_Results):
        cp = CustomerPage.LoginPage(setup)
        cp.wait(7)
        cp.select_Login()
        if Condition == "+":
            cp.enter_mobileno(Mobile_NO)
            cp.click_send_otp()
            cp.wait(5)
            cp.enter_otp(OTP)
            cp.click_next()
            cp.wait(5)
            assert cp.verify_login() == True
            status = "TC PASSED"
        elif Condition == "-":
            cp.enter_mobileno(Mobile_NO)
            cp.click_send_otp()
            cp.wait(5)
            assert cp.catch_error_msg() == True
            status = "TC PASSED"
        else:
            status = "TC FAILED"

        ExcelMethods("Login").update_result_in_excel(Test_Case_ID, status)

'''
    def test_TC_004(self, setup):
        cp = CustomerPage.LoginPage(setup)
        time.sleep(10)
        cp.user_details()
        cp.logout()
        cp.wait(10)
        assert cp.verify_logout() == True

class Test_Login_logout_neg:
    def test_TC_002(self, setup):
        cp = CustomerPage.LoginPage(setup)
        cp.wait(7)
        cp.select_Login()
        cp.enter_mobileno("8828091028")
        cp.click_send_otp()
        assert cp.catch_error_msg() == True and cp.current_url() == "https://ibpodev.home.tatamotors/edukaan_ui/#/account/login?isLogin=true"

    def test_TC_003(self, setup):
        cp = CustomerPage.LoginPage(setup)
        cp.wait(5)
        cp.enter_mobileno(" ")
        cp.click_send_otp()
        assert cp.catch_error_msg() == True and cp.current_url() == "https://ibpodev.home.tatamotors/edukaan_ui/#/account/login?isLogin=true"   
'''
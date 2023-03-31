import time
from pageObject import WhishList
from pageObject import OrdersPage

class TestOrderActions:
    def test_add_to_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        time.sleep(5)
        assert op.verify_add_cart(setup) == True

    def test_remove_from_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.remove_from_cart(setup)
        time.sleep(5)
        assert op.verify_remove_cart() == True

    def test_empty_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        time.sleep(7)
        assert op.empty_cart(setup) == True

class Test_PlaceOrder_CancelOrder(TestOrderActions):
    def test_place_order(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        time.sleep(7)
        op.place_order()
        op.move_to_payment(setup)


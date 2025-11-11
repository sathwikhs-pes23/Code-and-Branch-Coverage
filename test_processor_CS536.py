# test_processor_CS536.py
import pytest
from order_processor import calculate_discount, update_order_status

# ---------- calculate_discount tests ----------
@pytest.mark.parametrize("cust,amount,expected", [
    ("regular", 500, 0),          # regular, below threshold
    ("regular", 1000, 0),         # regular, exactly threshold -> no discount
    ("regular", 1500, 1500 * 0.05), # regular, >1000
    ("premium", 2000, 2000 * 0.1),  # premium -> 10%
    ("vip", 3000, 3000 * 0.1),      # vip but <=5000 -> 10%
    ("vip", 6000, 6000 * 0.2),      # vip >5000 -> 20%
])
def test_calculate_discount_various(cust, amount, expected):
    assert calculate_discount(cust, amount) == pytest.approx(expected)

def test_calculate_discount_unknown_customer():
    with pytest.raises(ValueError):
        calculate_discount("student", 100)

# ---------- update_order_status tests ----------
def test_update_order_pending_paid_changes_to_processing():
    order = {"status": "pending", "paid": True, "items_available": False}
    new_status = update_order_status(order)
    assert new_status == "processing"
    assert order["status"] == "processing"

def test_update_order_pending_unpaid_changes_to_awaiting_payment():
    order = {"status": "pending", "paid": False, "items_available": True}
    new_status = update_order_status(order)
    assert new_status == "awaiting_payment"
    assert order["status"] == "awaiting_payment"

def test_update_order_processing_items_available_shipped():
    order = {"status": "processing", "paid": True, "items_available": True}
    new_status = update_order_status(order)
    assert new_status == "shipped"
    assert order["status"] == "shipped"

def test_update_order_processing_items_not_available_backorder():
    order = {"status": "processing", "paid": True, "items_available": False}
    new_status = update_order_status(order)
    assert new_status == "backorder"
    assert order["status"] == "backorder"

# edge: if other statuses passed, update_order_status returns unchanged status
def test_update_order_other_status_unchanged():
    order = {"status": "shipped", "paid": True, "items_available": True}
    new_status = update_order_status(order)
    assert new_status == "shipped"
    assert order["status"] == "shipped"

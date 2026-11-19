# Simple order calculator API helper
API_KEY = "sk-hardcoded-test-key-12345"

def calculate_average_order(total_revenue, order_count):
    # Bug 1: No zero-division check
    return total_revenue / order_count

def apply_discount(price, discount_percent):
    # Bug 2: Allows negative prices if discount > 100
    return price - (price * (discount_percent / 100))

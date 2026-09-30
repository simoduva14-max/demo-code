from sconto import calculate_discounted_price

expected_price = 80
actual_price = calculate_discounted_price(100, 20)
assert actual_price == expected_price, f"FAILED: expected {expected_price}, got {actual_price}"
print("OK: test passed successfully!")

import re

str = "55 AND 4 OR 5656 BUT57.*?98.99AND100.101.102+103|104&105<106>107=108/109%110 1111 111 11 1234"
m = re.findall(r"(?<!\d)\d{2,3}(?!\d)", str)

print m

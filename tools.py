import datetime


# 🛒 TOOL 1: Discount system
def redeem_discount(user_id, code):
    DISCOUNTS = {
        "WELCOME50": False,
        "SUMMER20": False
    }

    REGISTERED_USERS = {"user_123", "user_456"}

    if user_id not in REGISTERED_USERS:
        return "User not registered"

    code = code.upper().strip()

    if code not in DISCOUNTS:
        return "Invalid code"

    if DISCOUNTS[code]:
        return "Code already used"

    DISCOUNTS[code] = True
    return f"{code} redeemed successfully for {user_id}"


# 🧮 TOOL 2: Calculator
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"


# 🕒 TOOL 3: Time tool
def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
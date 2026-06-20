import tools

MEMORY = {
    "name": None,
    "last_command": None
}


def run_agent(user_id, command):
    print("DEBUG INPUT:", command)

    command = command.lower().strip()
    MEMORY["last_command"] = command

    # 👋 greeting
    if command in ["hi", "hello", "hey"]:
        if MEMORY["name"]:
            return f"Hey {MEMORY['name']} 👋"
        return "Hey 👋 What's your name?"

    # 🧠 name setting
    if "my name is" in command:
        name = command.replace("my name is", "").strip()
        MEMORY["name"] = name
        return f"Nice to meet you, {name} 😊"

    # 🧮 calculator
    if any(op in command for op in ["+", "-", "*", "/"]):
        return tools.calculator(command)

    if "calc" in command or "calculate" in command:
        expr = input("Enter expression: ")
        return tools.calculator(expr)

    # 🕒 time
    if "time" in command:
        return tools.get_time()

    # 🛒 discount
    if "welcome" in command or "summer" in command:
        return tools.redeem_discount(user_id, command)

    # ❗ fallback
    return "I can help with: calculator, time, discounts"
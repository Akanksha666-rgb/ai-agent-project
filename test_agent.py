import agent


def test_discount():
    result = agent.run_agent("user_123", "WELCOME50")
    assert "redeemed" in result


def test_calculator():
    result = agent.run_agent("user_123", "2+2")
    assert result == "4"


def test_time():
    result = agent.run_agent("user_123", "what is time")
    assert "202" in result  # year check
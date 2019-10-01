def currency_amount(amount, currency="USD"):
    amount = str(amount)
    if currency == "JPY":
        return "¥" + amount
    elif currency == "USD":
        return "$" + amount    
    elif currency == "EUR":
        return "€" + amount
    else:
        return amount
print(currency_amount(5,))
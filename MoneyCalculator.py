def calculate_change(amount):
    # Type checking
    if isinstance(amount, str):
        raise TypeError("Amount must be a number, not a string")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    
    # Negative amount checking
    if amount < 0:
        raise ValueError("Amount cannot be negative")
        
    # Round to 2 decimal places
    amount = round(amount, 2)
    amount_in_cents = round(amount * 100)
    
    if amount == 0:
        return {}
    
    # Define denominations in cents
    denominations = {
        '100 bill': 10000,
        '50 bill': 5000,
        '20 bill': 2000,
        '10 bill': 1000,
        '5 bill': 500,
        '1 bill': 100,
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1
    }
    
    change = {}
    for denom, value in denominations.items():
        count = amount_in_cents // value
        if count > 0:
            change[denom] = count
            amount_in_cents %= value
    
    return change
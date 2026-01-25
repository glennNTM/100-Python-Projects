def currency_conv():
    amount = int(input("Enter the amount in USD: "))
    currency = int(input("Select target currency (1 for EUR, 2 for GBP, 3 for JPY): "))

    if currency == 1:
        conv_amount = amount * 0.85
        print(f"Converted amount in EUR: {conv_amount}")
    elif currency == 2:
            conv_amount = amount * 0.74
            print(f"Converted amount in GBP: {conv_amount}")

    elif currency == 3:
            conv_amount = amount * 156
            print(f"Converted amount in JPY: {conv_amount}")

currency_conv()

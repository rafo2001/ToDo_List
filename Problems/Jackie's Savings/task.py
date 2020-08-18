def final_deposit_amount(*interest, amount=1000):
    final_amount = amount
    for i in interest:
        final_amount = final_amount * (1 + (i / 100))
    return round(final_amount, 2)

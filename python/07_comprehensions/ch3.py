# ---------------------Dictionary comprehensions ----------------------

tea_prices_inr = {
    "Masala chai":40,
    "Green tea":50,
    "Lemon tea":200
}
tea_prices_usd = {tea:price*95  for tea,price in tea_prices_inr.items() }
print(tea_prices_usd)


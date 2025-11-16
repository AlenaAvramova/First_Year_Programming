eur_to_usd = 1.08
gbp_to_usd = 1.25
chf_to_usd = 1.10

print("\n____________European Currency → USD Converter___________\n")

eur = float(input("Euros: "))
gbp = float(input("Pounds: "))
chf = float(input("Francs: "))

total_usd = eur * eur_to_usd + gbp * gbp_to_usd + chf * chf_to_usd

print("\n______ Conversion Breakdown ______")

print("EUR → USD: ", round(eur * eur_to_usd, 2), "USD")
print("GBP → USD: ", round(gbp * gbp_to_usd, 2), "USD")
print("CHF → USD: ", round(chf * chf_to_usd, 2), "USD")

print("\n______ Total ______\n")

print("Total in USD:",round(total_usd, 2))


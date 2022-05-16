import time
from libs.openexchange import OpenExchangeClient

APP_ID = "25116dae1039404ba6408ea8cbfcace1"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
# start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
# end = time.time()

# print(end-start)

print(f"USD {usd_amount} is GBP {gbp_amount:.2f}\n")

print("Current Exchange Rates:")
for x, y in client.latest['rates'].items():
    print(x, y)
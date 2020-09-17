coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
new_dict = {}
for i, k in zip(coin, code):
    new_dict[i] = k
print(new_dict)
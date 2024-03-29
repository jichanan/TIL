coin_list = [500,100,50,1]

def min_cost_count(value, coin_list):
  total_coin_count = 0
  details = []
  coin_list.sort(reverse=True)
  for coin in coin_list:
    coin_num = value // coin
    total_coin_count += coin_num
    value -= coin * coin_num
    details.append([coin, coin_num])
  return total_coin_count, details

print(min_cost_count(4720, coin_list))
# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры !!!!


banknotes = [10, 20, 50, 100, 200, 500, 1000]

amount = int(input("Plese enter the ammount"))
limit  = 10
final_banknote = False
for index, nominal in enumerate(banknotes):

  current_limit = limit
  test_sum = limit * nominal
  next_index = index + 1
  if(next_index > len(banknotes)):
    final_banknote = True
  if(test_sum <= amount) and not final_banknote:

    while ((amount - test_sum) % banknotes [next_index]):
      test_sum = test_sum - nominal
      current_limit -= 1
    amount -= test_sum

    print("Take", current_limit, ' of ', nominal )
    if amount ==0:
      break
  else:
    current_limit = amount // nominal
    if not (amount % nominal):
      print("Take", current_limit, ' of ', nominal )
      break

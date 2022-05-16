num = 0
tot = 0.0
while True :
  text = input('Enter a number:')
  if text == 'done' :
    break
  try:
    atext = float(text)
  except:
    print('Invalid input')
    continue
    num = num + 1
    tot = tot + atext
print(tot,num,tot/num)

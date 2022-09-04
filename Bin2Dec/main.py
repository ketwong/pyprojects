while True:
  binary = raw_input('enter up to 8 binary number: ')
  if len(binary) < 8:
    res = int(binary, 2)
    print(res)
    print('program finished')
    break
  else:
    print('cannot accept more than 8 chars! ')

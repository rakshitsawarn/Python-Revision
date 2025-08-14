def print_number_reverse(n):
  if n == 0:
    return
  print(n)
  print_number_reverse(n-1)

print_number_reverse(19)
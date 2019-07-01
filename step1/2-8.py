prime_num = []
for p in range(2, 101):
  mod = [k for k in range(2, p-1) if p%k == 0]
  if len(mod) == 0:
    prime_num.append(p)
print(prime_num)

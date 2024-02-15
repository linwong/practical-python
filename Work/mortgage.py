# mortgage.py
#
# Exercise 1.7

# change me
extra_payment_start_month = 61
extra_payment_end_month =  108
extra_payment = 1000

principal = 500000
rate = .05
payment = 2684.11
total_paid = 0
times_paid = 0

while principal > 0:
  times_paid += 1

  if principal < payment:
    total_paid += principal
    principal = 0
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (times_paid > extra_payment_start_month-1 and
        times_paid < extra_payment_end_month-1):
      principal -= extra_payment
      total_paid += extra_payment

  print(f'{times_paid:3d} {total_paid:10.2f} {principal:10.2f}')
# print(times_paid, round(total_paid, 2), round(principal, 2))

print('Months:', times_paid)
print('Total paid:', round(total_paid, 2))

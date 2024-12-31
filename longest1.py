def longest_consecutive_ones(n):
  binary_string = bin(n)[2:]
  current_count = 0
  max_count = 0

  for digit in binary_string:
    if digit == '1':
      current_count += 1
    else:
      current_count = 0
    max_count = max(max_count, current_count)
  return max_count

number = int(input("Enter an integer: "))
print(bin(number)[2:])
result = longest_consecutive_ones(number)
print(f"The longest consecutive sequence of 1s in the binary representation of {number} is: {result}")
number = int(input())
def get_next_palindrom(num):
    num = str(num)
    if num == num[::-1]:
        return num
    if len(num) % 2 == 0:
        left_part = num[:len(num) // 2]
        if int(left_part + left_part[::-1]) < int(num):
            left_part = str(int(left_part) + 1)
        return int(left_part + left_part[::-1])
    else:
        mid_digit = num[len(num) // 2]
        left_part = num[:len(num) // 2]
        if int(left_part + mid_digit + left_part[::-1]) < int(num):
            left_part_with_mid = str(int(left_part + mid_digit) + 1)
            ledt_part = left_part_with_mid[:-1]
            mid_digit = left_part_with_mid[-1]
        return left_part + mid_digit + left_part[::-1]
print(get_next_palindrom(number))
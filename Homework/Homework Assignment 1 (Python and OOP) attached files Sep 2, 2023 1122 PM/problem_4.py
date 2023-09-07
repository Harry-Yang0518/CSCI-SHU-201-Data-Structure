def is_palindrome(num):
    original = num
    reversed_num = 0
    while num:
        # Shift the reversed number to the left to make space for the next bit
        reversed_num <<= 1
        # Add the least significant bit of num to reversed_num
        reversed_num |= num & 1
        # Shift num to the right to process the next bit
        num >>= 1
    # Check if the original number is equal to its reversed counterpart
    return original == reversed_num

def main():
    print(is_palindrome(220395))  # should print True
    # 220395 is 110101110011101011 in binary (valid palindrome)

    print(is_palindrome(1060))  # should print False
    # 220395 is 10000100100 in binary (not a palindrome)

    print(is_palindrome(75817))  # should print True
    # 220395 is 10010100000101001 in binary (valid palindrome)

    print(is_palindrome(820))  # should print False
    # 220395 is 1100110100 in binary (not a palindrome)

    print(is_palindrome(5557))  # should print True
    # 220395 is 1010110110101 in binary (valid palindrome)


if __name__ == '__main__':
    main()

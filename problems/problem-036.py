den_num = 0
palindrome_sum = 0

def binary_convert(den_num):
    bin_num = ""

    while den_num > 0:
        bin_num = str(den_num & 1) + bin_num
        den_num >>= 1

    return bin_num

while den_num < 1_000_000:
    palindrom_chance = True

    def palindrome_check(num):
        for i in range(int(len(str(num))/2)):
            if str(num)[i] != str(num)[-i-1]:
                return False
        return True
    
    palindrom_chance = palindrome_check(den_num)

    if palindrom_chance:
        palindrom_chance = palindrome_check(binary_convert(den_num))

    if palindrom_chance:
        palindrome_sum += den_num

    den_num+=1

print(palindrome_sum)
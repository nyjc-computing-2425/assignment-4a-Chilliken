nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0]
numbers = nric[1:8]
suffix = nric[-1]
first_letter = "STFG"
digit_weight = "2765432"
st_digit = "JZIHGFEDCBA"
fg_digit = "XWUTRQPNMLK"
invalidity = "NRIC is invalid."
validity = "NRIC is valid."

if prefix not in first_letter:
    print(invalidity)
elif len(nric) != 9:
    print(invalidity)
elif numbers.isnumeric() is False:
    print(invalidity)
elif numbers.isnumeric():
    sum = 0
    count =0
    for i in numbers:
        i=int(i)
        sum+= i*int(digit_weight[count])
        count+=1
    if prefix in "TG":
                    sum +=4

    remainder = sum % 11

    checkdigit = ''
    if prefix in "ST":
                    checkdigit = st_digit[remainder]
    elif prefix in "FG":
                    checkdigit = fg_digit[remainder]

    if suffix == checkdigit:
                    print(validity)
    else:
                    print(invalidity)



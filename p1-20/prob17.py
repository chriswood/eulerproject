#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.



def tens(tn):
    tn = int(tn)
    return {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 
            4: 'forty', 5: 'fifty', 6: 'sixty', 
            7: 'seventy', 8: 'eighty', 9: 'ninety'}[tn]

def ones(on):
    on = int(on)
    return {0: '', 1: 'one', 2: 'two', 3: 'three', 
            4: 'four', 5: 'five', 6: 'six', 
            7: 'seven', 8: 'eight', 9: 'nine'}[on]

def hundreds(hn, skip_and):
    hn = int(hn)
    words = ones(hn) + ' hundred '
    return words if skip_and else words + 'and '

def teens(t):
    return {11: 'eleven', 12: 'twelve', 13: 'thirteen', 
            14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}[t]

def spellnum(n):
    words = ''
    str_num = str(n)

    if n > 999:
        return 'one thousand'
    if n > 99:
        words += hundreds(str_num[0], (n%100==0))
        str_num = str_num[1:3]
    if 10 < n % 100 < 20:
        return words + teens(n % 100)
    if n > 9:
        words += tens(str_num[0])
    words += ones(str_num[n > 9])
    return words

total = 0
for n in range(1, 1001):
    result = spellnum(n)
    print result
    total += len(result.replace(' ', ''))
print total



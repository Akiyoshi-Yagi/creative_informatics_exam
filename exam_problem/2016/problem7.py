"""
方針としては、100000以下なので、1000と100は最大で一回ずつしか出てこない、
これらの値でリストを区切る。

"""

def eng_num_translator(str_list):
    d = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
    }

    num_list = []
    for s in str_list:
        num_list.append(d[s])

    #str_listの長さが１の時
    if len(num_list) == 1:
        return num_list[0]

    #str_listの長さが２以上の時
    temp = num_list[0]
    ans = 0
    max_mul = 0
    for i in range(1,len(num_list)):
        if num_list[i] > num_list[i-1]:
            ans += temp * num_list[i]
            temp = 0
        else:
            temp += num_list[i]
        if i == len(num_list)-1:
            ans += temp

    return ans

str_list =list(input().split())
print(eng_num_translator(str_list))

'''
fifty four thousand three hundred twelve

one hundred thousand thirty one

'''




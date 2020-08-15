def tran_char_to_num(string):
    def translate(char):
        if char == "I":
            return 1
        elif char == "V":
            return 5
        elif char == "X":
            return 10
        elif char == "L":
            return 50
        elif char == "C":
            return 100
        elif char == "D":
            return 500
        elif char == "M":
            return 1000

    def sub_translate(char):
        if char == "IV":
            return 4
        elif char == "IX":
            return 9
        elif char == "XL":
            return 40
        elif char == "XC":
            return 90
        elif char == "CD":
            return 400
        elif char == "CM":
            return 900

    i = 0
    ans = 0
    while i <= len(string)-1:
        #引き算記法かどうかの確認
        if string[i:i+2] in ["IV","IX","XL","XC","CD","CM"]:
            num = sub_translate(string[i:i+2])
            ans += num
            i += 2
        else:
            num = translate(string[i])
            ans += num
            i += 1
    return ans

if __name__ == "__main__":
    print(tran_char_to_num(input()))



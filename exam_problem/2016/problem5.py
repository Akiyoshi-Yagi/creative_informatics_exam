def tran_num_to_char(num):
    #各、位が4,9の時だけ特別扱い。
    def special_tran(number):
        if number == 4:
            return "IV"
        elif number == 9:
            return "IX"
        elif number == 40:
            return "XL"
        elif number == 90:
            return "XC"
        elif number == 400:
            return "CD"
        elif number == 900:
            return "CM"

    def normal_tran(number, s):
        #numの値で場合分け
        if 5 <= number <= 8:
            a = 1
            b = number - 5
        else:
            a = 0
            b = number
        res = []
        if s == 1:
            res.extend(a*"V")
            res.extend(b*"I")
        elif s == 10:
            res.extend(a * "L")
            res.extend(b * "X")
        elif s == 100:
            res.extend(a * "D")
            res.extend(b * "C")
        return res


    #まず処理をしやすいように先頭に０を加える
    num_l = list(str(num))
    num = [0] * (4-len(num_l))
    num.extend(num_l)

    #1000だけ特別扱い
    ans = []
    ans.extend(["M"]*int(num[0]))

    s = 100
    for i in num[1:]:
        i = int(i)
        if i in [4,9]:
            ans.extend(special_tran(s*i))
        else:
            ans.extend(normal_tran(i,s))
        s *= 1/10

    return "".join(ans)

if __name__ == "__main__":
    i = int(input())
    print(tran_num_to_char(i))

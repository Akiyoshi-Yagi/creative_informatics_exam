'''
kadai1-monndai1
'''

import random
import collections
import numpy as np

#一回の試行を関数化
def one_game():
    trump_list = []
    for i in range(1,14):
        trump_list += [i,i,i,i]
    for k in range(1,11):
        random_list = []
        for x in range(5):
            num = random.choice(trump_list)
            random_list.append(num)
            trump_list.remove(num)
        num_list = list(collections.Counter(random_list).values())
        if num_list == [1,1,1,1,1]:
            if k == 10:
                return 20
            else:
                pass
        else:
            return k

score_list = []
#試行回数指定
exp_length = 10000
for m in range(exp_length):
    score_list.append(one_game())

#期待値
ave = sum(score_list)/exp_length
#推定誤差
est_error = np.sqrt(np.dot(np.array(score_list)-ave,np.array(score_list)-ave)/exp_length)

print("期待値 "+str(ave))
print("推定誤差 "+str(est_error))

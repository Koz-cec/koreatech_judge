'''
koreatech judge 1007
텔동 한쪽에 있는 마을 "짝" 에는 모든 숫자들이 두개씩 쌍을 이루어 존재하고 있습니다. 
하지만 어디에도 솔로는 존재하듯, 이곳에도 짝을 이루지 못한 숫자 하나가 있지요. 
그나마 다행인건 단 하나의 숫자만 짝이 없을 뿐, 나머지는 짝이 있어요.
짝을 만들어주기 위하여 단 하나만 있는 숫자를 찾아 주세요.
'''

testcase = int(input())
result = []

for f1 in range(testcase):
    inputnum = int(input())
    nums =  [*map(int,input().split())]
    nums_set = list(set(nums))

    for f2 in range(len(nums_set)):
        num_count = 0
        num_count = nums.count(nums[f2])
        if num_count == 1:
            result.append(nums[f2])
            f2 = 0
            break

for f3 in range(testcase):
    print(result[f3])

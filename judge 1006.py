'''
koreatech judge 1006 
최근 개인 사업을 시작한 광성이는 매일 아침마다 은행에 가서 동전과 지폐들을 교환해 오는것이 일이다. 
현금으로 물건 값을 지불할 경우 조금 더 싸게 한 덕분에 현금으로 구입하는 사람이 많은데, 
대부분의 손님들이 물건값보다는 더 많은 돈을 내서 꼭 거스름돈이 필요해지는 일이 발생하기 때문이다.
그래서 최대한 적은 지폐랑 동전을 사용하여 거스름돈을 주고 싶은데, 광성이를 위해서 물건값(C)와 받은 금액(R) 이 주어졌을때, 
거스름돈으로 지불할 지폐 혹은 동전의 최소 갯수를 출력하는 프로그램을 작성하라.
예를들여 물건값이 1천원이고, 받은 돈이 1만원이면 거스름돈은 5천원 한장과 1천원 4장으로 총 5장의 현금이 필요하며, 
물건값이 520원이고 받은돈이 1천원일 경우 1백원 짜리 동전 4개와 50원짜리 동전 1개, 그리고 10원짜리 3개로 총 8개의 동전이 필요합니다.
'''

testcase = int(input()) #테스트 케이스의 수
obj = [None]*1000
obj_charge = [None]*1000

for i in range(testcase):
    Nobj_str,Nobj_charge_str = input().split()
    Nobj = int(Nobj_str)
    Nobj_charge = int(Nobj_charge_str)
    obj[i] = Nobj
    obj_charge[i] = Nobj_charge

for f1 in range(testcase):
    change_value = [0,0,0,0,0,0,0,0]
    Nmoney = obj_charge[f1] - obj[f1]
    m50000 = Nmoney//50000
    Nmoney = Nmoney%50000
    change_value[0] = m50000
    m10000 = Nmoney//10000
    Nmoney = Nmoney%10000
    change_value[1] = m10000
    m5000 = Nmoney//5000
    Nmoney = Nmoney%5000
    change_value[2] = m5000
    m1000 = Nmoney//1000
    Nmoney = Nmoney%1000
    change_value[3] = m1000
    m500 = Nmoney//500
    Nmoney = Nmoney%500
    change_value[4] = m500
    m100 = Nmoney//100
    Nmoney = Nmoney%100
    change_value[5] = m100
    m50 = Nmoney//50
    Nmoney = Nmoney%50
    change_value[6] = m50
    m10 = Nmoney//10
    change_value[7] = m10
    Nmoney = 0
    for f2 in range(8):
        print(change_value[f2], end = ' ')
    print()

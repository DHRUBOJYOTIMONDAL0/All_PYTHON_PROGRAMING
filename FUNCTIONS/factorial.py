# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact*i
# print(fact) 

num = int(input("Enter a number: "))
def cal_fact(num):
    fact = 1
    for i in range (1, num+1):
        fact = fact*i
    return fact
res_fact = cal_fact(num)
print(res_fact)          
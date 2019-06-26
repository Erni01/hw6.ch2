# 6. Given an integer. Print its tens digit.


n = int(input())
tens = n % 100 - n % 10
new = tens // 10
print(str(new))
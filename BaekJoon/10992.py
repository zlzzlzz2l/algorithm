num = int(input())

for i in range(1, num+1):
    if i == num:
        print('*'*(2*num-1)) # 맨 마지막, 2*입력값-1이 출력
    elif i == 1:
        print(' '* (num-i)+"*") # 맨 처음, num보다 -1 작은 값이 공백으로 출력
    else:
        print(' '*(num-i)+'*'+' '*(i*2-3)+'*') # 중간,
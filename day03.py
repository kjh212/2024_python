# %s 문자열
# %d 10진수
# %x 16진수
# %o 8진수
# %f 10진 부동소수점
# %e 지수로 나타낸 부동소수점
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('%d%%' % 100) # %%=문자 %
print("our cas %s weights %s pounds" % (40,50))

thing='woodchuck'
print('%s' % thing)
print('%12s' % thing) # 12칸 오른쪽
print('%+12s' % thing)
print('%-12s' % thing) # 12칸 왼쪽 정렬
print('%.3s' % thing) # 3개만 사용
print('%12.3s' % thing) # 12칸 오른쪽 3개 사용
print('%-12.3s' % thing)




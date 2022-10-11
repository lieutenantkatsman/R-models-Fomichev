import collections

def checked():
    arr_input = input()
    # arr_input = '1,1,2,2,3,4,2,10,3,131422,3421341,2342,10'
    k = int(input())
    arr = arr_input.split(',')
    arr = [int (x) for x in arr]
    c = collections.Counter()
    for i in arr:
        c[i] += 1
    tmp = c.most_common(k)
    final = []
    for i in tmp:
        tmp1 = list(i)
        final.append(tmp1[0])
    print(final)
    
checked()
n = int(input())                                            # number of soldiers
item_list = [i for i in range(1, n + 1)]                    # sidewalk
k = int(input())
while len(item_list) > 2:                                 
    if k > len(item_list):
        pass
    else:
        count = 0                                       
    for i in range(len(item_list)):
            count += 1
            if count == k:
                item_list[i] = 'd'
                count = 0
    else: 
        if 'd' not in item_list:
            continue                                         
    new_l = item_list[-count:] + item_list[:-count]         # list compounder
    item_list = [c for c in new_l if c != 'd']              # item_list
    if len(item_list) < k:
        count = 0
if k % 2 != 0:
    res = item_list[::-1]
else:
    res = item_list
print(res[0])
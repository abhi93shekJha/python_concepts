from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future


def merge(left_future, right_future):
    left_list = left_future.result()
    right_list = right_future.result()
    sorted_list = []
    i = 0
    j = 0
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1
    while(i<len(left_list)):
        sorted_list.append(left_list[i])
        i += 1
    while(j<len(right_list)):
        sorted_list.append(right_list[j])
        j += 1
    return sorted_list         
    

def merge_sort(my_list, threadPoolExecutor):
    if len(my_list)==1:
        return my_list
    mid = len(my_list)//2
    left_list = my_list[0:mid]
    right_list = my_list[mid:]
    # print("left list ", left_list)
    # print("right list ", right_list)
    left_future = threadPoolExecutor.submit(merge_sort, left_list, threadPoolExecutor)
    right_future = threadPoolExecutor.submit(merge_sort, right_list, threadPoolExecutor)
    return merge(left_future, right_future)
    

if __name__=='__main__':
    my_list = [8, 4, 5, 1, 3, 19]
    executor = ThreadPoolExecutor()
    future = executor.submit(merge_sort, my_list, executor)
    print(future.result())
    executor.shutdown()
        
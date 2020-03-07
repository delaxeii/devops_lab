#!/usr/bin/env python3

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


def compare_list(list1, list2):
    if len(list1) != len(list2):
        diff = len(list1) - len(list2)
        for i in range(diff):
            list2.append(None)
    return dict(zip(list1, list2))


print(compare_list(list1, list2))

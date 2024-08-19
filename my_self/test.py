# # def merge(left_arr, right_arr):
# #     result = []
# #     while left_arr and right_arr:
# #         if left_arr[0] < right_arr[0]:
# #             result.append(left_arr.pop(0))
# #         else:
# #             result.append(right_arr.pop(0))
# #     if left_arr:
# #         result += left_arr
# #     if right_arr:
# #         result += right_arr
# #     return result


# # def merge_sort(arr):
# #     if len(arr) < 2:
# #         return arr
# #     middle = len(arr) // 2
# #     left_arr = merge_sort(arr[:middle])
# #     right_arr = merge_sort(arr[middle:])
# #     return merge(left_arr, right_arr)


# # print(merge_sort([3, 2, 1, 4, 5]))


# def score_tool(input_str):
#     score = 0
#     number = 0
#     up_char = 0
#     low_char = 0
#     other = 0

#     if len(input_str) < 5:
#         score += 5
#     elif len(input_str) >= 5 and len(input_str) <= 7:
#         score += 10
#     else:
#         score += 25

#     for i in input_str:
#         if i.isdigit():
#             number += 1
#         elif i.isupper():
#             up_char += 1
#         elif i.islower():
#             low_char += 1
#         else:
#             other += 1

#     if up_char == 0 or low_char == 0:
#         score += 10
#     else:
#         score += 20

#     if number == 1:
#         score += 10
#     elif number > 1:
#         score += 20

#     if other == 1:
#         score += 10
#     elif other > 1:
#         score += 25

#     if number > 0 and up_char > 0 and low_char > 0 and other > 0:
#         score += 5
#     elif number > 0 and up_char + low_char > 0 and other > 0:
#         score += 3
#     elif number > 0 and up_char + low_char > 0:
#         score += 2
#     return score


# def level(score):
#     if score >= 0 and score < 25:
#         return "VERY_WEAK"
#     elif score >= 25 and score < 50:
#         return "WEAK"
#     elif score >= 50 and score < 60:
#         return "AVERAGE"
#     elif score >= 60 and score < 70:
#         return "STRONG"
#     elif score >= 70 and score < 80:
#         return "VERY_STRONG"
#     elif score >= 80 and score < 90:
#         return "SECURE"
#     elif score >= 90:
#         return "VERY_SECURE"


# input_str = "38$@NoNoN"

# score = score_tool(input_str)
# level(score)


# input_number = 28
# # i = 15
# count = 0
# for i in range(1, input_number):
#     number_list = []
#     for j in range(1, i):
#         if i % j == 0:
#             number_list.append(j)

#     if i == sum(number_list):
#         count += 1

# print(count)

y, m, d = 2176, 5, 21

flag = 0

if y % 4 == 0 and y % 100 != 0:
    flag = 1
elif y % 400 == 0:
    flag = 1

flag_0_dict = {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181,
               7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
flag_1_dict = {1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182,
               7: 213, 8: 244, 9: 274, 10: 305, 11: 335, 12: 366}

if flag == 0:
    if m == 1:
        print(d)
    else:
        print(flag_0_dict[m-1]+d)
else:
    if m == 1:
        print(d)
    else:
        print(flag_1_dict[m-1]+d)

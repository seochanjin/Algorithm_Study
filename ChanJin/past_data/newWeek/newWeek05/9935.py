# import sys
#
# a = input().strip()
# b = input().strip()
# lenB = len(b)
# listB = []
# for i in b:
#     listB.append(i)
# stack = []
#
# for i in a:
#     stack.append(i)
#
#     if stack[-lenB:] == listB:
#         for j in range(lenB):
#             stack.pop()
#             if not stack:
#                 break
#
# if not stack:
#     print("FRULA")
# else:
#     for i in stack:
#         print("".join(stack))
#

###########################################################################


import sys

a = input().strip()
b = input().strip()
lenB = len(b)
listB = []
for i in b:
    listB.append(i)
lastB = listB[-1]
stack = []

for i in a:
    stack.append(i)

    if i == lastB and len(stack) >= lenB:
        if stack[-lenB:] == listB:
            for _ in range(lenB):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))

# class Element:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head
#         print(self.head)
#     def append(self, new_element):
#         current = self.head
#         print(current)
#         if self.head:
#             print('if')
#             while current.next:
#                 print('cur')
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element
#
# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)
# print(e1.value, e1.next)
# print(e2.value, e2.next)
# print(e3.value, e3.next)
# print(e4.value, e4.next)
# ll = LinkedList(e1)
# ll.append(e2)
# print(e1.value, e1.next)
# print(e2.value, e2.next)
# #print(ll)
# #print(ll.head, e1.value)
# #print(ll.head, e1.value)

# d = {'a':14, 'a':34, 'a':12 }
# print(d['a'])
#
# d = {'a':14, 'a':34, 'a':98 }
# print(d['a'])
#
# d = {'a':14, 'a':34, 'a':'asd' }
# print(d['a']) #takes the last value assigned


def find_duplicates(arr1, arr2):
  duplicates = []
  i, j = 0, 0
  while (i<len(arr1) and j<len(arr2)):
    print('init', i, j)
    if arr1[i] == arr2[j]:
      duplicates.append(arr1[i])
      print(arr1[i])
      print('-'*12)
      i+=1
      j+=1
    elif arr1[i] < arr2[j]:
      print(arr1[i])
      print('_'*12)
      duplicates.append(arr1[i])
      i+=1
    else:
      print(arr2[i])
      print('='*12)
      duplicates.append(arr2[j])
      j+=1
  #print(duplicates)
  #for i in arr1 and j in arr2
  pass # your code goes here

#find_duplicates([11], [11])
l = [12,23,45]
j = [12,34,45,65]
find_duplicates(l, j)

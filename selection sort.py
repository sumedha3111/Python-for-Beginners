def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j


        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

n =input()
l=[]
for i in range(n):
 l[i]=input()
selection_sort(l)
print(l)
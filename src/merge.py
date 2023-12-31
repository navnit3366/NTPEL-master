def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid =len(nlist)//2
        lefthalf=nlist[:mid]
        righthalf=nlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(nlist,lefthalf,righthalf)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1
    while i< len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
    while j< len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    print('Merging ',nlist)
nlist=[]
n=int(input('Enter the no of elements: '))
for i in range(0,n):
    ele=int(input())
    nlist.append(ele)
print('Unsorted List: ',nlist)
mergeSort(nlist)
print('Sorted List', nlist)

def min(a):
    min=a[0]
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
    return min





d=[4,3,2,5,6,3,9]
print(min(d))

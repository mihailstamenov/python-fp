def get_median_font_size(font_sizes):
    list = font_sizes[:]

    if len(list) == 0:
        return None
    
    list.sort()
    even = len(list) % 2 == 0

    if even:
        mid = int((len(list)/2)-1)
    else:
        mid = int(len(list)//2)

    return list[mid]
   


list = [8, 8, 8]
print(sorted(list)[(len(list)-1)//2])
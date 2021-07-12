def insertio(array):
    for i in range(1,len(array)):
        up = array[i]
        j = i - 1
        while j >= 0 and array[j]>up:
            array[j+1]= array[j]
            j-=1
        array[j+1] = up
    return (array)

def Bucketsort(arr):
    array = []
    slot_numbers = 10
    for i in range(slot_numbers):
        array.append([])
    for j in arr:
        index_b = int(slot_numbers*j)
        array[index_b].append(j)
    for i in range(slot_numbers):
        array[i] = insertio(array[i])
    k = 0
    for i in range(slot_numbers):
        for j in range(len(array[i])):
            arr[k] = array[i][j]
            k+=1
    return arr


if __name__ == "__main__":
    array = [0.897,0.565,0.656,0.5432,0.5143]
    print("this is the sorted array")
    print(Bucketsort(array))
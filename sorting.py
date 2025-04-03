class Sort():
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        arr = self.data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self):
        arr = self.data.copy()
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]  
        return arr

    def insertion_sort(self):
        arr = self.data.copy()
        n = len(arr)
        for i in range(1, n):
            curr = arr[i]
            prev = i - 1
            while prev >= 0 and arr[prev] > curr:
                arr[prev + 1] = arr[prev]
                prev -= 1
            arr[prev + 1] = curr
        return arr

    def merge_sort(self):
        arr = self.data.copy()

        def merge(arr, st, mid, end):
            temp = []
            i, j = st, mid + 1
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= end:
                temp.append(arr[j])
                j += 1
            for idx in range(len(temp)):
                arr[st + idx] = temp[idx]

        def _merge_sort(arr, st, end):
            if st < end:
                mid = st + (end - st) // 2
                _merge_sort(arr, st, mid)
                _merge_sort(arr, mid + 1, end)
                merge(arr, st, mid, end)

        _merge_sort(arr, 0, len(arr) - 1)
        return arr

    def quick_sort(self):
        arr = self.data.copy()

        def partition(arr, st, end):
            idx = st - 1
            pivot = arr[end]
            for j in range(st, end):
                if arr[j] <= pivot:
                    idx += 1
                    arr[idx], arr[j] = arr[j], arr[idx]
            idx += 1
            arr[idx], arr[end] = arr[end], arr[idx]
            return idx

        def _quick_sort(arr, st, end):
            if st < end:
                pi = partition(arr, st, end)
                _quick_sort(arr, st, pi - 1)
                _quick_sort(arr, pi + 1, end)

        _quick_sort(arr, 0, len(arr) - 1)
        return arr



sort_type = input("""Please select from the following options:
1. Bubble sort
2. Selection sort
3. Insertion sort
4. Merge sort
5. Quick sort
""")

valid_options = {'1', '2', '3', '4', '5'}
if sort_type not in valid_options:
    print("Invalid selection. Please choose a number from 1 to 5.")
    exit()


while True:
    a = input("Enter numbers separated by space: ")
    try:
        data = list(map(int, a.split()))
        break
    except ValueError:
        print("Please enter integers only.\n")

if not data:
    print("You entered an empty list.")
    exit()


if data == sorted(data):
    print("The list is already sorted.")
    exit()

if len(set(data)) == 1:
    print("Only one element cannot me sorted.")
    exit()


sort = Sort(data)

if sort_type == '1':
    print("Sorted:", sort.bubble_sort())
elif sort_type == '2':
    print("Sorted:", sort.selection_sort())
elif sort_type == '3':
    print("Sorted:", sort.insertion_sort())
elif sort_type == '4':
    print("Sorted:", sort.merge_sort())
elif sort_type == '5':
    print("Sorted:", sort.quick_sort())

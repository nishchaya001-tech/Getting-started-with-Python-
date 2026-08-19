list = [4, 7, 8, 12, 45, 99]

def bin(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        m = list[mid]

        if m == n:
            print("Ele found in the index:", mid)
            return

        elif m < n:
            l = mid + 1

        else:
            u = mid - 1

    print("Element not found")


n = int(input("Enter the no. u wanna find: "))
bin(list, n)
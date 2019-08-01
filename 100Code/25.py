nums = [1,2,3,4,5,6,7,8,9,0]

while True:
    num = input("inssert your num for search: ")
    if num == 't':
        print("exit...")
        break
    try:
        num = int(num)
        print(nums[num])
    except ValueError:
        print("insert right number.")
    except IndexError:
        print("number is not exist.")
#search dar array ba handel kardan error ha.
from dynamic_array import DynamicArray


def main():
    nums = DynamicArray(size=1)
    nums.add(1)
    nums.add(2)
    nums.add(3)
    value = nums.get(1)  # index=1, value=2
    nums.delete(1)  # index=1, value=2 is deleted
    value = nums.get(1)  # index=1, value=3


if __name__ == "__main__":
    main()

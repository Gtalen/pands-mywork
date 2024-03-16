def collatz(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # print the final value (1)


def main():
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            collatz(number)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
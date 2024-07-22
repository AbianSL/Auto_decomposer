#  @file main.py
#  @author AbianSL
#  @brief decomposer the input image into prime numbers
#  @version 0.1
#  @date 2024-07-22

import decomposer

def main():
    """
    Main function
    """
    number = 0
    
    number = int(input("Enter a number greater than 0: "))

    primes = decomposer.decomposer(number)

    print(f"Prime numbers: {primes}")


if __name__ == "__main__":
    main()

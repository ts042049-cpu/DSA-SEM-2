# AERT - Algorithmic Efficiency & Recursion Toolkit
# Name = Tushar saini 
# Roll no. = 2501730053
# Course: B.Tech CSE (AI Ml), 2nd Semester


#  Stack ADT 
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


#  Factorial 
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 1
    return n * factorial(n - 1)


#  Fibonacci 
call_count_naive = 0
def fib_naive(n):
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


call_count_memo = 0
memo = {}
def fib_memo(n):
    global call_count_memo
    call_count_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


#  Tower of Hanoi 
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)


#  Binary Search 
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


#  MAIN 
if __name__ == "__main__":
    print("Factorial Tests:")
    for n in [0,1,5,10]:
        print(n, factorial(n))

    print("\nFibonacci Tests:")
    for n in [5,10,20]:
        call_count_naive = 0
        print(f"Naive fib({n}) =", fib_naive(n), "calls:", call_count_naive)

        call_count_memo = 0
        memo.clear()
        print(f"Memo fib({n}) =", fib_memo(n), "calls:", call_count_memo)

    print("\nTower of Hanoi (N=3):")
    hanoi(3, 'A', 'B', 'C')

    print("\nBinary Search:")
    arr = [1,3,5,7,9,11,13]
    for key in [7,1,13,2]:
        print(f"Search {key}:", binary_search(arr, key, 0, len(arr)-1))
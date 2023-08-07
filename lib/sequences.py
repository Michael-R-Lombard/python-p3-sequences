#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    if length > 0:
        fib_seq.append(0)

    for i in range(length - 1):  
        if i == 0 and length > 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])

    print(fib_seq)

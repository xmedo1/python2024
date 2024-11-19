import random


def binary_iterator():
    while True:
        yield 0
        yield 1


def world_directions():
    while True:
        yield random.choice(["N", "E", "S", "W"])


def weekdays():
    while True:
        for day in range(7):
            yield day


print("Binary iterator:")
b_iter = binary_iterator()
for _ in range(10):
    print(next(b_iter), end=" ")

print("\n\nRandom world directions:")
w_dir = world_directions()
for _ in range(10):
    print(next(w_dir), end=" ")

print("\n\nWeekdays:")
weekday_iter = weekdays()
for _ in range(15):
    print(next(weekday_iter), end=" ")

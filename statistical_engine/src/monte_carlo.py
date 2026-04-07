import random

def simulate_crashes(days, crash_probability=0.045):
    crashes = 0

    for _ in range(days):
        if random.random() < crash_probability:
            crashes += 1

    return crashes, crashes / days


def run_simulation():
    days_list = [30, 365, 10000]

    for days in days_list:
        crashes, prob = simulate_crashes(days)

        print(f"\nDays: {days}")
        print(f"Total Crashes: {crashes}")
        print(f"Simulated Probability: {prob:.4f}")
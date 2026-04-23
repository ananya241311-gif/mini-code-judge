# code_judge.py

def check_solution(user_func, test_cases):
    passed = 0

    for i, (inp, expected) in enumerate(test_cases, 1):
        try:
            result = user_func(inp)
            if result == expected:
                print(f"Test Case {i}: PASS")
                passed += 1
            else:
                print(f"Test Case {i}: FAIL (Expected {expected}, Got {result})")
        except Exception as e:
            print(f"Test Case {i}: ERROR ({e})")

    print(f"\nPassed {passed}/{len(test_cases)} test cases")


# -------------------------------
# SAMPLE USER SOLUTION
# -------------------------------
def user_solution(n):
    # Example: Fibonacci
    if n <= 1:
        return nwha
    return user_solution(n-1) + user_solution(n-2)


# -------------------------------
# TEST CASES
# -------------------------------
test_cases = [
    (0, 0),
    (1, 1),
    (5, 5),
    (6, 8),
    (7, 13)
]


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print("Running Code Judge...\n")
    check_solution(user_solution, test_cases)
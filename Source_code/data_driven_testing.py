"""
Project : Data-Driven Testing Lab

This program reads test cases from a CSV file,
compares expected and actual results, and
generates a simple test report.
"""

import csv

INPUT_FILE = "test_data.csv"
OUTPUT_FILE = "test_report.txt"

passed = 0
failed = 0

print("=" * 50)
print("DATA-DRIVEN TESTING LAB")
print("=" * 50)

with open(INPUT_FILE, mode="r") as file:
    reader = csv.DictReader(file)

    report = []

    for row in reader:

        test_case = row["Test Case"]
        expected = row["Expected Result"]
        actual = row["Actual Result"]

        if expected == actual:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        report.append(
            f"{test_case} : {status}"
        )

        print(f"{test_case:<20} {status}")

with open(OUTPUT_FILE, "w") as file:

    file.write("DATA-DRIVEN TEST REPORT\n")
    file.write("-" * 35 + "\n\n")

    for line in report:
        file.write(line + "\n")

    file.write("\n")
    file.write(f"Passed Tests : {passed}\n")
    file.write(f"Failed Tests : {failed}\n")

print("\nSummary")
print("-" * 20)
print("Passed :", passed)
print("Failed :", failed)

print("\nReport saved as test_report.txt")
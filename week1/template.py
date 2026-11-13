"""
RECORD CHECK  -  my version
===========================

Name  : Kshaunish Satsangi
Lane  :  Cyber     (delete two)
Date  : 08-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
label = input("Enter label/name: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.
diff = first - second
perc = (first / second) * 100 if second != 0 else 0.0

# =================================================================== OUTPUT
# 3. Print the report.
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"First value: {first:>21.2f}")
print(f"Second value: {second:>20.2f}")
print(f"Difference: {diff:>22.2f}")
print(f"Percentage: {perc:>21.2f}%")
print(f"Signed Diff: {diff:>+21.2f}")

print("=" * 34)

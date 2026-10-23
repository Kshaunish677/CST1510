"""
RECORD CHECK  -  my version
===========================

Name  :KSHAUNISH SATSANGI
Lane  :  Cyber    (delete two)
Date  : 11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(percent):
    if percent >= 100:
        print("OVER LIMIT")
    elif percent >= 90:
        print("WARNING")
    else:
        print("OK")

def check(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    print(difference, percent)

def print_report(label, value, limit, difference, percent, status):
    print(f"[{status}] {label}: Value={value}, Limit={limit}, Diff={difference}, {percent:.1f}%")

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter a name/a hostname/an IP: ")
value = float(input("Enter number: "))
limit = float(input("Enter number: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = value - limit
percent = (value / limit) * 100     
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.
import math 

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Status: {status}")
print(f"Value: {round(value, 2)}")
print(f"Limit: {round(limit, 2)}")
print(f"Difference: {round(difference, 2)}")
print(f"Percent: {round(percent, 2)}%")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

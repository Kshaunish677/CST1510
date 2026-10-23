'''Mini-project · 80 min

Open **`template.py`** (in this `LAB` folder). It has the structure already — you fill in the marked sections.

## Choose your lane

Pick **one**. All three are the same program with different words.

| Lane | Your three inputs | Example |
|---|---|---|
| **AI / Data Science** | dataset name, rows loaded, rows expected | `survey_2026`, `1187`, `1200` |
| **Cyber Security** | source IP, failed logins, total attempts | `10.0.0.5`, `12`, `400` |
| **IT** | hostname, GB used, GB total | `srv-01`, `87`, `120` |

## What to build

**Threshold — pass standard.** Write `status_of(percent)`. Ask for the three values,
work out the difference and percentage inline, call `status_of` for the status, and
print a bordered report including it.

```
==================================
  RECORD CHECK  -  srv-01
==================================
  Used        : 87
  Total       : 120
  Status      : OK
==================================
```

**Typical.** Also write `check(value, limit)`, returning the difference and
percentage — call it instead of calculating inline. Numbers show 2 decimal places,
right-aligned.

```
==================================
  RECORD CHECK  -  srv-01
==================================
  Used        :      87.00
  Total       :     120.00
  Free        :      33.00
  Percent     :      72.50 %
  Status      :         OK
==================================
```

**Excellent.** Also write `print_report(...)` — every `print()` for the report
happens inside it, nowhere else. Wrap the input/process/output steps in a loop so you
can check as many records as you like in one run — type `quit` to stop. Keep count of
how many came back `OVER LIMIT` and print that once, after the loop ends.

## Rules

- **Every function does one job.** If a function both calculates and prints, split it.
- Do not calculate the same thing in two different places.
- **Give every function you write a one-line docstring** saying what it does.
- **No lists yet** — that is Week 4.

## When it works

1. Run it three times with different inputs. Does it still look right?
2. Run it with a total of `0`. Write the error down.'''

"""
Week 3 Mini-project · Record Check (IT Lane)
Author: Student
"""
# Percent rankings function
def status(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# Calculations
def check(value, limit):
    free = limit - value
    percent = (value / limit) * 100
    return free, percent

# Report with 2 decimal places
def print_report(hostname, used, total, free, percent, current_status):
    print("==================================")
    print(f"  RECORD CHECK  -  {hostname}")
    print("==================================")
    print(f"  Used        : {used:10.2f}")
    print(f"  Total       : {total:10.2f}")
    print(f"  Free        : {free:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {current_status:>10}")
    print("==================================\n")

# Main program
hostname = input("Enter hostname: ")
used = float(input("Enter GB used: "))
total = float(input("Enter GB total: "))
free, percent = check(used, total)
current_status = status(percent)

print_report(hostname, used, total, free, percent, current_status)


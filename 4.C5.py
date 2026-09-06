employees = {
    "emp101": {
        "name": "Sarah Connor",
        "department": "Engineering",
        "salary": 95000
    },
    "emp102": {
        "name": "Marcus Vance",
        "department": "Marketing",
        "salary": 72000
    },
    "emp103": {
        "name": "Elena Rostova",
        "department": "Finance",
        "salary": 88000
    }
}
for emp_id, info in employees.items():
    print(f"ID: {emp_id}")
    print(f"  Name: {info['name']}")
    print(f"  Department: {info['department']}")
    print(f"  Salary: ${info['salary']:,}")
    print("-" * 25)

#OUTPUT
"""
ID: emp101
  Name: Sarah Connor
  Department: Engineering
  Salary: $95,000
ID: emp102
  Name: Marcus Vance
  Department: Marketing
  Salary: $72,000
ID: emp103
  Name: Elena Rostova
  Department: Finance
  Salary: $88,000
  """

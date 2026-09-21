student_marks = {
    "Nani": 85,
    "Thanush": 92,
    "Kushal": 78,
    "Charan": 90
}

print("Original Dictionary:", student_marks)

removed_val = student_marks.pop("Charan")
print(f"\nRemoved 'Charan' with score: {removed_val}")
print("Dictionary after pop():", student_marks)

missing_key = "Ram"
safe_value = student_marks.get(missing_key,"Not Found")

print(f"\nAttempted to access '{missing_key}': {safe_value}")
print("Dictionary remains unchanged:", student_marks)

#OUTPUT
"""Original Dictionary: {'Nani': 85, 'Thanush': 92, 'Kushal': 78, 'Charan': 90}

Removed 'Charan' with score: 90
Dictionary after pop(): {'Nani': 85, 'Thanush': 92, 'Kushal': 78}

Attempted to access 'Ram': Not Found
Dictionary remains unchanged: {'Nani': 85, 'Thanush': 92, 'Kushal': 78}
"""

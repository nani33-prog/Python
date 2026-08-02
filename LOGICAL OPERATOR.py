percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)

# 0UTPUT
# Enter percentage: 79
# Enter attendance %: 84
# Eligible for scholarship: False

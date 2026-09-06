MovieDir={"RRR":"SSR","Pushpa":"Sukumar","Athadu":"Trivikram"}
print("Movie and Directors:",MovieDir)

key="Pushpa"
if key in MovieDir:
    print(f"{key} is Found and value is {MovieDir[key]}")
else:
    print(f"{key} is Not Found")

#OUTPUT
"""
Movie and Directors: {'RRR': 'SSR', 'Pushpa': 'Sukumar', 'Athadu': 'Trivikram'}
Pushpa is Found and value is Sukumar
"""

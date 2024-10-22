# Belajar Tipe Data Dictionary

customer = {"Name": "Andi", "Age": 30, "Address": "Subang"}

nama = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Andi Setiawan"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}: {value}")
# Belajar Set

# List => []
# Tuple => ()
# Set => {}

nama = {"Adi", "Joko", "Adi", "Joko", "Andi"}

nama.add('Setiawan')
nama.add('Setiawan')
nama.add('Setiawan')

for data in nama:
    print(data)

nama.remove("Adi")
nama.remove("Andi")

print(tuple(nama))
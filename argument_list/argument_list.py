# Belajar Argument List

def jumlahkan(*list_angka):
    total = 0

    for angka in list_angka:
        total = total + angka

    print(total)

jumlahkan(10, 10, 10, 10, 10, 10)
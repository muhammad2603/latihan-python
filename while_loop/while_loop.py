# Belajar While-Loop

data = ""

while data != "x":
    print("masuk perulangan")
    try:
        data = input("data : ")
    except EOFError:
        print("Input tidak tersedia, menghentikan program!")
        break
# Belajar Default Argument Value

def say_hello(first_name="Budi", last_name=""):
    print(f"Hello {first_name} - {last_name}")

say_hello("Andi")

say_hello(last_name="Setiawan", first_name="Andi")
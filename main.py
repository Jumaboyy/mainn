i = 1
while True:
    name = input("Ism: ")
    if name.lower() == 'stop':
        break
    lastname = input("Familiya: ")
    age = input("Yosh: ")
    if not age.isdigit():
        print("Yosh raqam kiritilmadi!!!\nBarcha ma'lumotlarni qayta kiriting!!!")
        continue
    age = int(age)
    phone = input("Tel: ")
    if not phone.startswith("+998") and not len(phone) == 13:
        print("Tel raqam kiritilmadi!!!\nBarcha ma'lumotlarni qayta kiriting!!!")
        continue
    email = input("Pochta: ")
    address = input("Manzil: ")

    text = f'''Id: {i}
N: {name}
L: {lastname}
A: {age}
P: {phone}
E: {email}
AD: {address}\n\n'''

    with open("users_info.txt", mode="a", encoding="utf-8") as file:
        file.write(text)

    i += 1

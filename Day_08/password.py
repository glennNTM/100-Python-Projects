from faker import Faker

fake = Faker()

def random_password_generator(len:int):
    len = int(input("Enter the desired password length: "))
    password_gen = fake.password(length=len)
    print(f"Generated password: {password_gen}")

if __name__=="__main__":
    random_password_generator(12)

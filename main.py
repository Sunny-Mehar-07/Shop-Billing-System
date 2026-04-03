import os
from datetime import datetime

cart = []
bill_number = 1

# Create folder if not exists
if not os.path.exists("bills"):
    os.makedirs("bills")


def add_product():
    global cart
    customer = input("Customer ka naam daalo: ") if not cart else cart[0][3]

    product = input("Saman ka naam daalo: ")
    price = float(input("Ek piece ki keemat (₹): "))
    qty = int(input("Quantity kitni: "))

    cart.append((product, price, qty, customer))
    print(f"{qty} x {product} bill me jod diya!")


def save_bill():
    global bill_number, cart

    if not cart:
        print("Bill khali hai, pehle saman add karo!")
        return

    filename = f"bill_{bill_number}.txt"
    path = os.path.join("bills", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("===== SHOP BILL =====\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write(f"Bill No: {bill_number}\n")
        f.write(f"Customer: {cart[0][3]}\n\n")

        total = 0
        for item in cart:
            product, price, qty, customer = item
            cost = price * qty
            f.write(f"{product} - {qty} x {price} = {cost}\n")
            total += cost

        f.write(f"\nTotal = {total}\n")
        f.write("=====================\n")

    print(f"\nBill bana aur save ho gaya! File: {path}")
    bill_number += 1
    cart = []


def view_bill():
    files = sorted(os.listdir("bills"))

    if not files:
        print("Abhi tak koi bill save nahi hai.")
        return

    print("\nAvailable bills:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    choice = int(input("Kaunsa bill dekhna hai (number): "))

    if 1 <= choice <= len(files):
        path = os.path.join("bills", files[choice - 1])
        with open(path, "r", encoding="utf-8") as f:
            print("\n----- Saved Bill -----\n")
            print(f.read())
            print("----------------------\n")
    else:
        print("Galat choice hai.")


def main():
    while True:
        print("\n1. Saman Add karo")
        print("2. Bill banao aur save karo")
        print("3. Band karo")
        print("4. Saved bill dekho")

        choice = input("Kya karna hai? (1/2/3/4): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            save_bill()
        elif choice == "3":
            print("Billing System band ho gaya.")
            break
        elif choice == "4":
            view_bill()
        else:
            print("Galat option dala, dobara try karo.")


if __name__ == "__main__":
    main()

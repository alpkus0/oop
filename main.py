from product import Product
from customer import Customer
from cart import Cart
from order import Order


def main():
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 10),
        Product("Kulaklık", 500, 20)
    ]

    name = input("Müşteri Adınızı ve Soyadınızı Girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name, email)

    cart = Cart()

    while True:
        print("\n---------------------------")
        print("         ÜRÜNLER          ")
        print("---------------------------")
        for i, product in enumerate(products):
            print(f"{i + 1}. {product}")

        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("\nSeçiminizi Yapın: ")

        if choice == "1":
            product_index = int(input("Hangi ürünü eklemek istiyorsunuz? (Numara): ")) - 1
            if 0 <= product_index < len(products):
                quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                cart.add_product(products[product_index], quantity)
            else:
                print("Geçersiz ürün numarası!")

        elif choice == "2":
            product_name = input("Hangi ürünü çıkarmak istiyorsunuz? (İsim): ")
            cart.remove_product(product_name)
            print(f"{product_name} sepetten çıkarıldı.")

        elif choice == "3":
            print("\n---------------------------")
            print("         SEPETİNİZ        ")
            print("---------------------------")
            if not cart.items:
                print("Sepetiniz boş!")
            else:
                print(f"{'Ürün':<15} {'Adet':<5} {'Birim Fiyat':<12} {'Toplam Fiyat':<12}")
                print("-" * 50)
                for item in cart.items.values():
                    product = item['product']
                    quantity = item['quantity']
                    total_price = product.price * quantity
                    print(f"{product.name:<15} {quantity:<5} {product.price:<12} {total_price:<12}")
                print("-" * 50)
                print(f"Toplam Tutar: {cart.get_total()} TL")

        elif choice == "4":
            if cart.get_total() > 0:
                print("\n---------------------------")
                print("     SİPARİŞ ÖZETİ       ")
                print("---------------------------")
                cart.display_cart()
                print(f"\nToplam Tutar: {cart.get_total()} TL")

                confirm = input("\nSiparişi onaylıyor musunuz? (E/H): ").strip().lower()
                if confirm == "e":
                    order = Order(customer, cart)
                    order.place_order()
                    print("\nSiparişiniz başarıyla oluşturuldu! Teşekkür ederiz.")
                    print("\n---------------------------")
                    print("          FATURA           ")
                    print("---------------------------")
                    print(f"Müşteri: {customer.name}")
                    print(f"E-Posta: {customer.email}")
                    print("\nSipariş Detayları:")
                    cart.display_cart()
                    print(f"\nÖdenecek Tutar: {cart.get_total()} TL")
                    print("\n---------------------------")
                    print("Sipariş tamamlandı. Çıkış yapılıyor...")
                    return
                else:
                    print("\nSipariş iptal edildi.")

            else:
                print("\nSepetiniz boş! Sipariş oluşturamazsınız.")

        elif choice == "5":
            print("Çıkış yapılıyor...")
            return

        else:
            print("Seçiminiz yanlış, tekrar deneyiniz.")


if __name__ == "__main__":
    main()

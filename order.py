class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart

    def place_order(self):
        total = self.cart.get_total()  # Toplam tutarı direkt metottan al
        if total > 0:
            print("\nSipariş başarıyla oluşturuldu.")
            print(self.customer)
            print("\nSipariş Detayları:")
            self.cart.display_cart()
            print(f"\nToplam Tutar: {total} TL")
        else:
            print("\nSepet boş, sipariş oluşturulamadı.")

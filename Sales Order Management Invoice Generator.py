class Order:
    # Conversion rate for EURO to USD
    EURO_TO_USD_RATE = 1.10

    def __init__(self, client_name, contact_first_name, contact_last_name, contact_email, customer_country, items_ordered, order_date):
        self.client_name = client_name
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.contact_email = contact_email
        self.customer_country = customer_country
        self.items_ordered = items_ordered
        self.order_date = order_date

    def calculate_pre_tax_total(self):
        total = sum(item['quantity'] * item['cost'] for item in self.items_ordered.values())
        return total

    def calculate_tax_due(self):
        tax_rate = 0

        if self.customer_country == 'Ireland':
            tax_rate = 0.23
        elif self.customer_country == 'Germany':
            tax_rate = 0.19
        elif self.customer_country == 'USA':
            state = input("Enter the state (California or Texas): ").strip()
            if state == 'California':
                tax_rate = 0.0725
            elif state == 'Texas':
                tax_rate = 0.0625
            else:
                print("Invalid state entered. Tax calculation not possible.")
                return 0

        tax_due = self.calculate_pre_tax_total() * tax_rate
        return tax_due

    def calculate_grand_total(self):
        pre_tax_total = self.calculate_pre_tax_total()
        tax_due = self.calculate_tax_due()
        grand_total = pre_tax_total + tax_due

        if self.customer_country == 'USA':
            grand_total *= self.EURO_TO_USD_RATE

        return grand_total

    def display_invoice(self):
        print("===== Invoice =====")
        print(f"Client: {self.client_name}")
        print(f"Contact Person: {self.contact_first_name} {self.contact_last_name}")
        print(f"Contact Email: {self.contact_email}")
        print(f"Customer Country: {self.customer_country}")
        print("Items Ordered:")
        for item_id, item_data in self.items_ordered.items():
            print(f"  {item_data['name']} (Quantity: {item_data['quantity']}, Cost: {item_data['cost']} EURO)")
        print(f"Order Date: {self.order_date}")
        print(f"Pre-tax Total: {self.calculate_pre_tax_total()} EURO")
        print(f"Tax Due: {self.calculate_tax_due()} EURO")
        print(f"Grand Total: {self.calculate_grand_total()} EURO")

# Example usage:
order_data = {
    1: {'name': 'Pen (Black)', 'quantity': 2, 'cost': 0.80},
    2: {'name': 'Pen (Red)', 'quantity': 1, 'cost': 0.90}
}

order = Order(
    client_name="ABC Company",
    contact_first_name="John",
    contact_last_name="Doe",
    contact_email="john.doe@example.com",
    customer_country="Ireland",
    items_ordered=order_data,
    order_date="2023-11-27"
)

order.display_invoice()

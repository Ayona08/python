from decimal import Decimal as d

class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self._part_number = part_number
        self._part_description = part_description
        self._quantity = quantity
        self._price_per_item = d(price_per_item)

    @property
    def part_number(self):
        return self._part_number

    @property
    def part_description(self):
        return self._part_description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Quantity cannot be negative. Setting quantity to 0.")
            self._quantity = 0
        else:
            self._quantity = value

    @property
    def price_per_item(self):
        return self._price_per_item

    @price_per_item.setter
    def price_per_item(self, value):
        if value < d('0.00'):
            print("Price per item cannot be negative. Setting price to 0.")
            self._price_per_item = d('0.00')
        else:
            self._price_per_item = d(value)

    def calculate_invoice(self):
        return self._quantity * self._price_per_item

# User input for creating an invoice
part_number = input("Enter part number: ")
part_description = input("Enter part description: ")

quantity = int(input("Enter quantity: "))
if quantity < 0:
    raise ValueError("Quantity cannot be negative.")

price_per_item = d(input("Enter price per item: "))
if price_per_item < d('0.00'):
    raise ValueError("Price per item cannot be negative.")
    
# Create Invoice instance
invoice = Invoice(part_number, part_description, quantity, price_per_item)

# Display invoice details
print(f"\nInvoice Details:")
print(f"Part Number: {invoice.part_number}")
print(f"Part Description: {invoice.part_description}")
print(f"Quantity: {invoice.quantity}")
print(f"Price per Item: {invoice.price_per_item}")

# Calculate and display the total invoice amount
print(f"Total Invoice Amount: {invoice.calculate_invoice()}")

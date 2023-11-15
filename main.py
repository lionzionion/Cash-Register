# 1. Fisrt step > Import necessary modules from the tkinter library
import tkinter as tk
from tkinter import ttk, messagebox

# 2. Second step > Menu dictionary with item names as keys and prices as values
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
    "Carnitas": 22.00
}

# 3. Third step > Define the main application class
class TaqueriaApp:
    def __init__(self, master):
        # Initialize the application with the main window
        self.master = master
        self.master.title("Felipe's Taqueria")
        self.total_cost = 0.00
        self.order_items = []

        # 4. Fourth step > Create and pack a label for the menu
        self.label_menu = tk.Label(master, text="Menu:")
        self.label_menu.pack()

        # 5. Fifth step > Create and pack a listbox for displaying menu items
        self.menu_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE, height=10)
        for item, price in menu.items():
            self.menu_listbox.insert(tk.END, f"{item}: ${price:.2f}")
        self.menu_listbox.pack()

        # 6. Sixth step > Create and pack a label for item selection
        self.label = tk.Label(master, text="Select items to add to your order:")
        self.label.pack()

        # 7. Seventh step > Create and pack a dropdown menu for item selection
        self.item_var = tk.StringVar()
        self.item_dropdown = ttk.Combobox(master, textvariable=self.item_var, values=list(menu.keys()))
        self.item_dropdown.pack()

        # 8. Eighth step > Create and pack a button to add selected item to the order
        self.button_add_item = tk.Button(master, text="Add Item", command=self.add_item)
        self.button_add_item.pack()

        # 9. Nineth step > Create and pack a button to complete the order and display the receipt
        self.button_cash_out = tk.Button(master, text="Cash Out", command=self.cash_out)
        self.button_cash_out.pack()

        # 10. Tenth step > Create and pack a label for displaying the total cost
        self.total_label = tk.Label(master, text="Total cost: $0.00")
        self.total_label.pack()

    def add_item(self):
        # 11. Eleventh step > Get the selected item from the dropdown
        item = self.item_var.get()

        if item in menu:
            # 12. Twelveth step > Add the item to the order and update the total cost
            self.order_items.append(item)
            self.total_cost += menu[item]
            self.total_label.config(text=f"Total cost: ${self.total_cost:.2f}")
        else:
            # 13. Terteenth step > Show an error message for invalid items
            messagebox.showerror("Error", "Invalid item. Please select a valid item from the menu.")

    def cash_out(self):
        if not self.order_items:
            # 14. Show a warning if no items are selected before cashing out
            messagebox.showwarning("Warning", "No items in the order. Please add items before cashing out.")
        else:
            # 15. Generate the receipt and display it in an info message box
            receipt_text = self.generate_receipt()
            messagebox.showinfo("Order Complete", receipt_text)
            # 16. Reset the order after completing the transaction
            self.reset_order()

    def generate_receipt(self):
        # 17. Generate the receipt text with itemized details and total cost
        items_text = "\n".join([f"{item}: ${menu[item]:.2f}" for item in self.order_items])
        total_text = f"\nTotal cost: ${self.total_cost:.2f}"
        receipt_text = f"Order Summary:\n{items_text}\n{total_text}"
        return receipt_text

    def reset_order(self):
        # 18. Reset the order details to start a new transaction
        self.total_cost = 0.00
        self.order_items = []
        self.total_label.config(text="Total cost: $0.00")

# 19. Run the application if the script is executed as the main program
if __name__ == "__main__":
    # Create the main Tkinter window and run the application
    root = tk.Tk()
    app = TaqueriaApp(root)
    root.mainloop()

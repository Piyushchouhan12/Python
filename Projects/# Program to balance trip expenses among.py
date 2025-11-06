import tkinter as tk
from tkinter import messagebox

class TripExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trip Expense Splitter 💰")
        self.root.geometry("450x500")
        self.root.config(bg="#1e1e1e")

        self.entries = []

        tk.Label(root, text="Trip Expense Splitter", font=("Helvetica", 18, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

        self.people_frame = tk.Frame(root, bg="#1e1e1e")
        self.people_frame.pack(pady=10)

        tk.Label(self.people_frame, text="Number of People:", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=5)
        self.num_entry = tk.Entry(self.people_frame, width=10)
        self.num_entry.grid(row=0, column=1, padx=5)

        tk.Button(self.people_frame, text="Add People", command=self.create_people_entries, bg="#00bfa6", fg="white").grid(row=0, column=2, padx=5)

        self.input_frame = tk.Frame(root, bg="#1e1e1e")
        self.input_frame.pack(pady=10)

        tk.Button(root, text="Calculate", command=self.calculate, bg="#ff9800", fg="black", font=("Helvetica", 12, "bold")).pack(pady=10)

        self.output_box = tk.Text(root, height=10, width=50, bg="#252526", fg="white", wrap="word")
        self.output_box.pack(pady=10)

    def create_people_entries(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        try:
            n = int(self.num_entry.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number of people.")
            return

        self.entries.clear()
        for i in range(n):
            tk.Label(self.input_frame, text=f"Name {i+1}:", fg="white", bg="#1e1e1e").grid(row=i, column=0, padx=5, pady=5)
            name_entry = tk.Entry(self.input_frame)
            name_entry.grid(row=i, column=1, padx=5)

            tk.Label(self.input_frame, text="Paid ₹", fg="white", bg="#1e1e1e").grid(row=i, column=2)
            paid_entry = tk.Entry(self.input_frame, width=10)
            paid_entry.grid(row=i, column=3, padx=5)
            self.entries.append((name_entry, paid_entry))

    def calculate(self):
        people = {}
        for name_entry, paid_entry in self.entries:
            name = name_entry.get().strip()
            try:
                paid = float(paid_entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid amount for {name or 'person'}.")
                return
            if not name:
                messagebox.showerror("Error", "Name cannot be empty.")
                return
            people[name] = paid

        total = sum(people.values())
        n = len(people)
        if n == 0:
            messagebox.showerror("Error", "Add at least one person.")
            return
        equal_share = total / n

        output = f"----- Trip Summary -----\n"
        output += f"Total Trip Amount: ₹{total:.2f}\n"
        output += f"Each Person's Share: ₹{equal_share:.2f}\n\n"

        for name, paid in people.items():
            balance = paid - equal_share
            if balance > 0:
                output += f"{name} should get back ₹{balance:.2f}\n"
            elif balance < 0:
                output += f"{name} should pay ₹{abs(balance):.2f}\n"
            else:
                output += f"{name} is settled up.\n"

        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, output)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TripExpenseApp(root)
    root.mainloop()

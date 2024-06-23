import tkinter as tk
from tkinter import ttk, messagebox
from DrugIntercation_Class import DrugInteractionChecker

class DrugInteractionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Drug Interaction Checker")

        self.checker = DrugInteractionChecker()  # Initialize DrugInteractionChecker instance

        self.label1 = tk.Label(root, text="Enter the first drug:")
        self.label1.pack(pady=10)

        self.entry1_var = tk.StringVar()
        self.entry1 = ttk.Combobox(root, width=30, textvariable=self.entry1_var)
        self.entry1.pack()
        self.entry1['values'] = self.checker.drug_names
        self.entry1.bind("<KeyRelease>", self.update_suggestions)

        self.label2 = tk.Label(root, text="Enter the second drug:")
        self.label2.pack(pady=10)

        self.entry2_var = tk.StringVar()
        self.entry2 = ttk.Combobox(root, width=30, textvariable=self.entry2_var)
        self.entry2.pack()
        self.entry2['values'] = self.checker.drug_names
        self.entry2.bind("<KeyRelease>", self.update_suggestions)

        self.check_button = tk.Button(root, text="Check Interaction", command=self.check_interaction)
        self.check_button.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def update_suggestions(self, event):
        current_entry = event.widget
        current_text = current_entry.get().strip().lower()
        if current_text == "":
            current_entry['values'] = self.checker.drug_names
        else:
            filtered_suggestions = [drug for drug in self.checker.drug_names if current_text in drug.lower()]
            current_entry['values'] = filtered_suggestions

    def check_interaction(self):
        drug1 = self.entry1_var.get().strip()
        drug2 = self.entry2_var.get().strip()

        if drug1 == "" or drug2 == "":
            messagebox.showerror("Error", "Please enter both drugs.")
            return

        interaction_result = self.checker.check_interaction(drug1, drug2)
        self.result_label.config(text=interaction_result, font=("Helvetica", 13))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x300")
    app = DrugInteractionGUI(root)
    root.mainloop()



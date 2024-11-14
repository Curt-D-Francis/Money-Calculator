import unittest
from MoneyCalculator import calculate_change
from TestMoneyCalculation import TestCalculateChange

def create_gui():
    import customtkinter as ctk
    from tkinter import messagebox
    
    # Initialize custom GUI
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Create the main window
    root = ctk.CTk()
    root.title("Change Calculator")
    root.geometry("400x400")

    # Title label
    title_label = ctk.CTkLabel(root, text="Exact Change Calculator", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=(20, 10))

    # Amount entry
    label_amount = ctk.CTkLabel(root, text="Enter amount in USD:")
    label_amount.pack(pady=(10, 5))

    entry_amount = ctk.CTkEntry(root, width=200, placeholder_text="e.g., 19.99")
    entry_amount.pack(pady=(0, 10))

    # Output text box
    output_frame = ctk.CTkFrame(root)
    output_frame.pack(pady=10, fill="both", expand=True)

    output_text = ctk.CTkTextbox(output_frame, height=150, width=300)
    output_text.pack(padx=10, pady=10, fill="both", expand=True)

    # Function to display the change
    def show_change():
        try:
            amount_str = entry_amount.get()
            try:
                amount = float(amount_str)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")
                return
                
            change = calculate_change(amount)
            
            # Clear the output text box
            output_text.delete(1.0, "end")
            for denom, count in change.items():
                output_text.insert("end", f"{denom}: {count}\n")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except TypeError as e:
            messagebox.showerror("Error", str(e))

    # Calculate button
    calculate_button = ctk.CTkButton(root, text="Calculate Change", command=show_change)
    calculate_button.pack(pady=(10, 20))

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    # Run the tests
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateChange)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    # launch the GUI if all tests pass
    if test_result.wasSuccessful():
        print("\nAll tests passed! Starting the application...")
        create_gui()
    else:
        print("\nTests failed. Please fix the issues before running the application.")
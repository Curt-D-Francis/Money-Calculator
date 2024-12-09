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
    root.geometry("500x500")

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
            amount = float(entry_amount.get())
            
        
                
            change = calculate_change(amount)
            
            # Clear the output text box
            output_text.delete(1.0, "end")
            
            # Handle bills and coins
            for denom, count in change.items():
                
                if denom == "penny":
                    multi_denom = "pennies" if count > 1 else "penny"
                elif denom in ["dime", "nickel", "quarter"]:
                    multi_denom = denom if count == 1 else f"{denom}s"
                elif denom in ["100 bill", "50 bill", "20 bill", "10 bill", "5 bill", "1 bill"]:
                    multi_denom = f"${denom}" if count == 1 else f"${denom}s"
                else:
                    multi_denom = denom

    
                output_text.insert("end", f"* {count} - {multi_denom}\n")
                
        except (ValueError, TypeError) as e:
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
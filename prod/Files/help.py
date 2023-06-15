from .__init__ import *

class HelpDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calculator Help")
        self.resizable(False,False)
        self.ico = Image.open("Icons/help.png")
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        help_text = """
        Calculator Help:

        1. Basic Operations:
           - Addition (+): Enter the first number, press the '+' button, enter the second number, and click '=' to see the result.
           - Subtraction (-): Enter the first number, press the '-' button, enter the second number, and click '=' to see the result.
           - Multiplication (*): Enter the first number, press the *' button, enter the second number, and click '=' to see the result.
           - Division (/): Enter the first number, press the '/' button, enter the second number, and click '=' to see the result.

        2. Clearing the Display:
           - C (All Clear): Click the 'C' button to clear the entire display.

        3. Decimal Numbers:
           - Use the decimal point (.) button to input decimal numbers. For example, enter '3.14' for Pi.

        4. Other Functions:
           - Percentage (%): To calculate percentages, enter the number, press the '%' button, and click '=' to see the result.

        Note: The calculator follows the order of operations (BODMAS) for complex calculations.
        """

        help_label = tk.Label(self, text=help_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)
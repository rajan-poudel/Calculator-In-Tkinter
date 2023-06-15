from .__init__ import *



class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.resizable(False,False)
        self.ico = Image.open("Icons/about.png")
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        about_text = """
Welcome to the Calculator GUI!

Created with passion and dedication by Rajan Poudel, a budding computer coding and programming enthusiast, 
this calculator represents my first step into the world of software development. With a deep love for 
computers and a desire to bring functionality to life, I embarked on this journey to create a user-friendly 
and efficient calculator application.

As a beginner in the world of coding, I embraced the challenge of building this GUI-based calculator from 
scratch. With every line of code written, I discovered the power and creativity that programming offers. This 
project has not only honed my technical skills but has also ignited a fire within me to explore the limitless 
possibilities of software development.

The Calculator GUI aims to provide you with a reliable and intuitive tool for all your mathematical needs. 
Whether you're a student, professional, or simply someone who enjoys crunching numbers, this calculator is 
designed to make your calculations swift and accurate. This application has covered some basic arithmetic 
operations only.

My vision for this calculator is to create a user-friendly experience that allows anyone, regardless of their 
coding expertise, to easily perform calculations with confidence. I hope that this tool will not only assist 
you in your daily mathematical tasks but also inspire you to delve further into the fascinating world of 
computer programming.

Thank you for joining me on this exciting journey as I take my first steps into the realm of coding. Your 
support and feedback are invaluable to me as I continue to learn and grow. Feel free to explore the various 
features of this calculator GUI, and may it bring simplicity and efficiency to your mathematical endeavors.

Happy calculating!
Rajan Poudel
        """

        help_label = tk.Label(self, text=about_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)
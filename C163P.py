from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Heart diagnose Report")
root.geometry("900x900")

radio_var1 = tk.StringVar()
radio_var2 = tk.StringVar()
radio_var3 = tk.StringVar()
radio_var4 = tk.StringVar()
radio_var5 = tk.StringVar()


def calculate_score():
    score = 0
    
    if radio_var1.get() == "yes":
        score += 10
    
    if radio_var2.get() == "yes":
        score += 10
  
    if radio_var3.get() == "yes":
        score += 10
    
    if radio_var4.get() == "yes":
        score += 10
 
    if radio_var5.get() == "yes":
        score += 10
    
   
    if score <= 10:
        messagebox.showinfo("Health Assessment", "You don't need to visit a doctor.")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Health Assessment", "You might perhaps have to visit a doctor.")
    else:
        messagebox.showinfo("Health Assessment", "I strongly advise you to visit a doctor")


question1_label = tk.Label(root, text="Question 1: Do you have fever?", background="lightgray", foreground="black")
question2_label = tk.Label(root, text="Question 2: Do you have persistent cough?", background="lightgray", foreground="black")
question3_label = tk.Label(root, text="Question 3: Do you have difficulty breathing?", background="lightgray", foreground="black")
question4_label = tk.Label(root, text="Question 4: Do you have body aches?", background="lightgray", foreground="black")
question5_label = tk.Label(root, text="Question 5: Do you have fatigue?", background="lightgray", foreground="black")


question1_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
question2_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
question3_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
question4_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
question5_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


radio_yes1 = tk.Radiobutton(root, text="Yes", variable=radio_var1, value="yes", background="lightgray")
radio_no1 = tk.Radiobutton(root, text="No", variable=radio_var1, value="no", background="lightgray")
radio_yes2 = tk.Radiobutton(root, text="Yes", variable=radio_var2, value="yes", background="lightgray")
radio_no2 = tk.Radiobutton(root, text="No", variable=radio_var2, value="no", background="lightgray")
radio_yes3 = tk.Radiobutton(root, text="Yes",)


root.mainloop()
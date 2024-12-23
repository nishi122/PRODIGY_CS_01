import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    # Criteria weights
    length_criteria = len(password) >= 12
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate score
    score = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Use at least 8 characters.")
    if not upper_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one number.")
    if not special_criteria:
        feedback.append("Include at least one special character.")

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def evaluate_password():
    password = entry_password.get()
    result = assess_password_strength(password)

    # Update results in the GUI
    label_strength.config(text=f"Password Strength: {result['strength']}")
    feedback_text = "\n".join(result['feedback'])
    text_feedback.config(state=tk.NORMAL)
    text_feedback.delete(1.0, tk.END)
    text_feedback.insert(tk.END, feedback_text)
    text_feedback.config(state=tk.DISABLED)

# Create the main GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="black")

# Password input
label_prompt = tk.Label(root, text="Enter a password to assess its strength:", bg="black", fg="white")
label_prompt.pack(pady=10)

entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

# Evaluate button
button_evaluate = tk.Button(root, text="Evaluate", command=evaluate_password)
button_evaluate.pack(pady=10)

# Strength label
label_strength = tk.Label(root, text="Password Strength:", font=("Arial", 12), bg="black", fg="white")
label_strength.pack(pady=5)

# Feedback text area
text_feedback = tk.Text(root, height=8, width=50, state=tk.DISABLED, bg="black", fg="white")
text_feedback.pack(pady=10)

# Run the GUI event loop
root.mainloop()
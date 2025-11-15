from tkinter import *
from tkinter import messagebox

def check_dfa():
    try:
        states = states_entry.get().split(',')
        alphabet = alphabet_entry.get().split(',')
        start_state = start_entry.get().strip()
        final_states = final_entry.get().split(',')
        transitions_text = transition_entry.get("1.0", END).strip()
        input_string = string_entry.get().strip()

        transitions = {}
        for line in transitions_text.splitlines():
            if '=' in line:
                left, right = line.split('=')
                left = left.strip()
                right = right.strip()
                if ',' in left:
                    state, symbol = left.split(',')
                    state, symbol = state.strip(), symbol.strip()
                    transitions[(state, symbol)] = right

        current_state = start_state
        for symbol in input_string:
            if (current_state, symbol) in transitions:
                current_state = transitions[(current_state, symbol)]
            else:
                result_label.config(text="Invalid Symbol ❌", fg="orange")
                return

        if current_state in final_states:
            result_label.config(text="Accepted ✅", fg="green")
        else:
            result_label.config(text="Rejected ❌", fg="red")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI
main = Tk()
main.title("DFA Simulator")
main.geometry("400x500")

Label(main, text="Enter DFA Details", font=("Arial", 14, "bold")).pack(pady=10)

Label(main, text="States (comma separated):").pack()
states_entry = Entry(main, width=40)
states_entry.pack()

Label(main, text="Alphabet (comma separated):").pack()
alphabet_entry = Entry(main, width=40)
alphabet_entry.pack()

Label(main, text="Start State:").pack()
start_entry = Entry(main, width=40)
start_entry.pack()

Label(main, text="Final States (comma separated):").pack()
final_entry = Entry(main, width=40)
final_entry.pack()

Label(main, text="Transitions (e.g., q0,0=q1):").pack()
transition_entry = Text(main, width=40, height=6)
transition_entry.pack()

Label(main, text="Input String:").pack()
string_entry = Entry(main, width=40)
string_entry.pack(pady=5)

Button(main, text="Check DFA", command=check_dfa).pack(pady=10)

result_label = Label(main, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

main.mainloop()

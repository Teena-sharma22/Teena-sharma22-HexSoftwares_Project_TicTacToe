import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != '':
            for index in combo:
                buttons[index].config(bg='green')  # Change background color for the winning buttons
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return True

    # Check for tie
    if all(button['text'] != '' for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "Tied Game")
        root.quit()
        return True

    return False

def button_click(index):
    if buttons[index]['text'] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index].config(fg='blue' if current_player == 'X' else 'Black')
        if check_winner():
            return
        toggle_player()

def toggle_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()    
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text='', font=('normal', 25), width=6, height=2, bg='lightgrey', padx=5, pady=5, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = 'X'
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 26), bg='lightgray')
label.grid(row=3, column=0, columnspan=3) 

root.mainloop()

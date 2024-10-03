import tkinter #graphical user interface library
def set_tile(row, column):
    global curr_player, last_player
    if not game_over and board[row][column]["text"] == "":  # Check if the game is not over
        board[row][column]["text"] = curr_player  # Mark the tile
        last_player = curr_player  # Store the last player
        if curr_player == playerX:  # Change player
            curr_player = playerO
        else:
            curr_player = playerX
        label["text"] = curr_player + "'s turn"
        
        # Check for win
        check_winner()
def check_winner():
    global game_over, turns
    turns += 1

    # Check horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    # Check vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    # Check diagonally, check top-left to bottom-right
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    # Check diagonally, check top-right to bottom-left
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][2 - i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    #tie
    if turns == 9:
        label.config(text="Tie!", foreground=color_yellow)
        game_over = True
        

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    # Set the starting player to the last player who made a move
    curr_player = playerO if last_player == playerX else playerX
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=color_gray, foreground=color_blue)
    label.config(text=curr_player + "'s turn", foreground="white")  # Reset label color


#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
# Initialize the last player to the starting player
last_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue= "#4584b6"
color_yellow ="#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns=0
game_over = False

#window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0,columnspan=3,sticky="we")
for row in range (3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                         background=color_gray,foreground=color_blue, width=3, height=1,
                                         command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Reset", font=("Consolas", 20),background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+x+y"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()

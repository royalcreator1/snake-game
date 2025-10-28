"""Snake Game with Nokia Phone UI"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from database import Database


class SnakeGame:
    def __init__(self):
        self.db = Database()
        self.user_name = None
        self.user_id = None
        
        # Game settings
        self.GRID_WIDTH = 20
        self.GRID_HEIGHT = 20
        self.CELL_SIZE = 25
        
        # Game state
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.food = None
        self.score = 0
        self.game_over = False
        self.paused = False
        self.showing_leaderboard = False
        
        # Initialize UI
        self.setup_ui()

    def setup_ui(self):
        """Create the Nokia phone-like UI"""
        self.root = tk.Tk()
        self.root.title("Nokia Snake Game")
        self.root.configure(bg='#f0f0f0')
        
        # Outer phone body with white strip on left
        phone_container = tk.Frame(self.root, bg='#2c2c2c', relief='flat', bd=0)
        phone_container.pack(padx=20, pady=20)
        
        # White strip on left side (characteristic Nokia feature)
        white_strip = tk.Frame(phone_container, bg='#ffffff', width=12, relief='flat')
        white_strip.pack(side=tk.LEFT, fill=tk.Y)
        
        # Main phone body (dark grey)
        phone_body = tk.Frame(phone_container, bg='#4a4a4a', relief='raised', bd=5)
        phone_body.pack(side=tk.LEFT)
        
        # Phone face (silver-grey front panel)
        phone_face = tk.Frame(phone_body, bg='#d0d0d0', relief='sunken', bd=3)
        phone_face.pack(padx=8, pady=8)
        
        # Screen area with NOKIA branding
        screen_container = tk.Frame(phone_face, bg='#2c2c2c', relief='sunken', bd=3)
        screen_container.pack(padx=5, pady=5)
        
        # NOKIA text above screen
        nokia_label = tk.Label(
            screen_container, text='NOKIA', font=('Courier', 8, 'bold'),
            bg='#2c2c2c', fg='#a0a0a0', pady=2
        )
        nokia_label.pack()
        
        # Screen frame (yellowish-green bezel)
        screen_frame = tk.Frame(screen_container, bg='#9db52d', relief='flat', bd=2)
        screen_frame.pack(padx=3, pady=2)
        
        # Game canvas with monochrome green
        canvas_width = self.GRID_WIDTH * self.CELL_SIZE
        canvas_height = self.GRID_HEIGHT * self.CELL_SIZE
        self.canvas = tk.Canvas(
            screen_frame,
            width=canvas_width,
            height=canvas_height,
            bg='#a7c739',  # Nokia green screen
            highlightthickness=0
        )
        self.canvas.pack(padx=2, pady=2)
        
        # Control buttons area
        control_frame = tk.Frame(phone_face, bg='#d0d0d0')
        control_frame.pack(pady=10)
        
        # Call button (Green) - Start Game
        call_btn = tk.Button(
            control_frame, text='CALL', font=('Arial', 11, 'bold'),
            bg='#2ecc71', fg='white', relief='raised', bd=3,
            width=6, height=2, command=self.start_new_game,
            activebackground='#27ae60', activeforeground='white'
        )
        call_btn.pack(side=tk.LEFT, padx=10)
        
        # Navigation controls - D-pad style
        nav_controls = tk.Frame(control_frame, bg='#d0d0d0')
        nav_controls.pack(side=tk.LEFT, padx=15)
        
        # Navigation title
        nav_label = tk.Label(
            nav_controls, text='DIRECTION', font=('Arial', 7, 'bold'),
            bg='#d0d0d0', fg='#2c2c2c'
        )
        nav_label.grid(row=0, column=0, columnspan=3, pady=(0, 2))
        
        # Create a container for the D-pad
        dpad_frame = tk.Frame(nav_controls, bg='#d0d0d0')
        dpad_frame.grid(row=1, column=0, columnspan=3)
        
        # Up button
        self.up_btn = tk.Button(
            dpad_frame, text='↑', font=('Arial', 16, 'bold'),
            bg='#34495e', fg='white', width=3, height=1,
            command=lambda: self.change_direction('UP'),
            relief='raised', bd=2,
            activebackground='#2c3e50', activeforeground='white'
        )
        self.up_btn.grid(row=0, column=1, padx=2, pady=2)
        
        # Left button
        self.left_btn = tk.Button(
            dpad_frame, text='←', font=('Arial', 16, 'bold'),
            bg='#34495e', fg='white', width=3, height=1,
            command=lambda: self.change_direction('LEFT'),
            relief='raised', bd=2,
            activebackground='#2c3e50', activeforeground='white'
        )
        self.left_btn.grid(row=1, column=0, padx=2, pady=2)
        
        # Center button (Select/Pause)
        center_btn = tk.Button(
            dpad_frame, text='●', font=('Arial', 12),
            bg='#34495e', fg='white', width=3, height=1,
            command=self.toggle_pause,
            relief='raised', bd=2,
            activebackground='#2c3e50', activeforeground='white'
        )
        center_btn.grid(row=1, column=1, padx=2, pady=2)
        
        # Right button
        self.right_btn = tk.Button(
            dpad_frame, text='→', font=('Arial', 16, 'bold'),
            bg='#34495e', fg='white', width=3, height=1,
            command=lambda: self.change_direction('RIGHT'),
            relief='raised', bd=2,
            activebackground='#2c3e50', activeforeground='white'
        )
        self.right_btn.grid(row=1, column=2, padx=2, pady=2)
        
        # Down button
        self.down_btn = tk.Button(
            dpad_frame, text='↓', font=('Arial', 16, 'bold'),
            bg='#34495e', fg='white', width=3, height=1,
            command=lambda: self.change_direction('DOWN'),
            relief='raised', bd=2,
            activebackground='#2c3e50', activeforeground='white'
        )
        self.down_btn.grid(row=2, column=1, padx=2, pady=2)
        
        # End button (Red) - View Leaderboard
        end_btn = tk.Button(
            control_frame, text='END', font=('Arial', 11, 'bold'),
            bg='#e74c3c', fg='white', relief='raised', bd=3,
            width=6, height=2, command=self.show_leaderboard,
            activebackground='#c0392b', activeforeground='white'
        )
        end_btn.pack(side=tk.LEFT, padx=10)
        
        # Status label
        self.status_label = tk.Label(
            phone_face,
            text="Ready to play - Press Green or Space",
            font=('Arial', 9),
            bg='#d0d0d0',
            fg='#2c2c2c',
            pady=5
        )
        self.status_label.pack()
        
        # Keyboard bindings
        self.root.bind('<Up>', lambda e: self.change_direction('UP'))
        self.root.bind('<Down>', lambda e: self.change_direction('DOWN'))
        self.root.bind('<Left>', lambda e: self.change_direction('LEFT'))
        self.root.bind('<Right>', lambda e: self.change_direction('RIGHT'))
        self.root.bind('<space>', lambda e: self.start_new_game())
        self.root.bind('<Return>', lambda e: self.toggle_pause())
        self.root.focus_set()
        
        self.root.mainloop()

    def get_user_name(self):
        """Prompt for user name"""
        name = simpledialog.askstring(
            "Enter Your Name",
            "Please enter your name:",
            initialvalue="Player"
        )
        return name

    def start_new_game(self):
        """Start a new game"""
        # Close leaderboard if open
        self.showing_leaderboard = False
        
        if self.user_name is None:
            self.user_name = self.get_user_name()
            if not self.user_name:
                return
            self.user_id = self.db.get_or_create_user(self.user_name)
        
        # Initialize game state
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        self.paused = False
        
        self.spawn_food()
        high_score = self.db.get_user_high_score(self.user_id)
        self.status_label.config(text=f'Score: {self.score} | High: {high_score}')
        self.update_game()

    def toggle_pause(self):
        """Toggle game pause"""
        if not self.game_over:
            self.paused = not self.paused
            if self.paused:
                self.status_label.config(text='PAUSED - Press Enter to Resume')
            else:
                high_score = self.db.get_user_high_score(self.user_id)
                self.status_label.config(text=f'Score: {self.score} | High: {high_score}')
                self.update_game()

    def change_direction(self, new_dir):
        """Change snake direction"""
        # Prevent 180-degree turns
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_dir != opposites.get(self.direction):
            self.next_direction = new_dir

    def spawn_food(self):
        """Spawn food at random location"""
        while True:
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def update_game(self):
        """Update game state and render"""
        if self.game_over or self.paused or self.showing_leaderboard:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        
        # Check for collision with walls
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.end_game()
            return
        
        # Check for collision with self
        if new_head in self.snake:
            self.end_game()
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            self.snake.pop()
        
        # Update status
        high_score = self.db.get_user_high_score(self.user_id)
        self.status_label.config(text=f'Score: {self.score} | High: {high_score}')
        
        # Render game
        self.render()
        
        # Schedule next update
        self.root.after(150, self.update_game)

    def render(self):
        """Render the game on canvas"""
        self.canvas.delete('all')
        
        # Draw grid lines (very subtle for monochrome display)
        for i in range(self.GRID_WIDTH + 1):
            self.canvas.create_line(
                i * self.CELL_SIZE, 0,
                i * self.CELL_SIZE, self.GRID_HEIGHT * self.CELL_SIZE,
                fill='#8a9843', width=1
            )
        for i in range(self.GRID_HEIGHT + 1):
            self.canvas.create_line(
                0, i * self.CELL_SIZE,
                self.GRID_WIDTH * self.CELL_SIZE, i * self.CELL_SIZE,
                fill='#8a9843', width=1
            )
        
        # Draw snake (darker green for contrast on green screen)
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * self.CELL_SIZE, y * self.CELL_SIZE,
                (x + 1) * self.CELL_SIZE, (y + 1) * self.CELL_SIZE,
                fill='#2c4a18', outline='#1a2e0e'
            )
        
        # Draw head (slightly different shade)
        head_x, head_y = self.snake[0]
        self.canvas.create_rectangle(
            head_x * self.CELL_SIZE, head_y * self.CELL_SIZE,
            (head_x + 1) * self.CELL_SIZE, (head_y + 1) * self.CELL_SIZE,
            fill='#3d5e22', outline='#2c4a18'
        )
        
        # Draw food (black dot on green screen)
        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * self.CELL_SIZE + 3, food_y * self.CELL_SIZE + 3,
            (food_x + 1) * self.CELL_SIZE - 3, (food_y + 1) * self.CELL_SIZE - 3,
            fill='#1a2e0e', outline='#0f1a09'
        )

    def end_game(self):
        """Handle game over"""
        self.game_over = True
        
        # Save score
        self.db.save_score(self.user_id, self.score)
        
        # Check if new high score
        high_score = self.db.get_user_high_score(self.user_id)
        
        message = f"Game Over!\nYour Score: {self.score}"
        if self.score == high_score and self.score > 0:
            message += "\n🎉 New High Score! 🎉"
        
        messagebox.showinfo("Game Over", message)
        self.status_label.config(text=f'Game Over! Score: {self.score} | High: {high_score}')

    def show_leaderboard(self):
        """Display leaderboard on the phone screen"""
        if self.showing_leaderboard:
            # If already showing leaderboard, go back to game
            self.showing_leaderboard = False
            self.status_label.config(text="Ready to play - Press CALL or Space")
            self.canvas.delete('all')
            if not self.game_over and not self.paused:
                self.render()
        else:
            # Show leaderboard
            self.showing_leaderboard = True
            leaderboard = self.db.get_leaderboard(10)
            self.render_leaderboard(leaderboard)
            self.status_label.config(text="Press END again to go back")

    def render_leaderboard(self, leaderboard):
        """Render leaderboard on the canvas"""
        self.canvas.delete('all')
        
        # Title
        self.canvas.create_text(
            self.GRID_WIDTH * self.CELL_SIZE / 2, 15,
            text="TOP SCORES",
            font=('Arial', 12, 'bold'),
            fill='#1a2e0e'
        )
        
        # Draw entries
        y_offset = 40
        max_entries = min(8, len(leaderboard))  # Fit on screen
        
        if not leaderboard:
            self.canvas.create_text(
                self.GRID_WIDTH * self.CELL_SIZE / 2,
                self.GRID_HEIGHT * self.CELL_SIZE / 2,
                text="No scores yet!\nBe the first!",
                font=('Arial', 10),
                fill='#1a2e0e',
                justify='center'
            )
        else:
            for rank, (name, score) in enumerate(leaderboard[:max_entries], 1):
                # Highlight current user
                color = '#1a2e0e' if name == self.user_name else '#2c4a18'
                font_weight = 'bold' if name == self.user_name else 'normal'
                
                # Create entry text
                entry_text = f"{rank}. {name[:12]:<12} {score}"
                
                self.canvas.create_text(
                    15, y_offset,
                    text=entry_text,
                    font=('Arial', 9, font_weight),
                    fill=color,
                    anchor='w'
                )
                y_offset += 30


if __name__ == "__main__":
    game = SnakeGame()


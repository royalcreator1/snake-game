# Nokia Snake Game

A retro-style Snake game with a Nokia phone interface, complete with leaderboard tracking and score persistence.

## Features

🐍 Classic Snake Game
📱 Authentic Nokia phone design with:
   - Dark grey phone body with white side strip
   - Silver-grey face panel
   - Monochrome green display (just like old Nokia!)
   - NOKIA branding above screen
   - Directional D-pad controls (↑↓←→●)
   - Green CALL button to start game
   - Red END button to view leaderboard
   - Leaderboard displays on-screen (no popup windows)
🏆 Leaderboard system showing top 10 players
💾 SQLite database for persistent score storage
👤 Player name registration and tracking
⌨️ Support for both on-screen buttons and keyboard controls (arrow keys)
🎮 Pause/Resume functionality

## Requirements

- Python 3.6+
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone or download this repository
2. Install dependencies (if tkinter is not available):
   ```bash
   # On Linux (Ubuntu/Debian)
   sudo apt-get install python3-tk
   
   # On macOS
   brew install python-tk
   ```

## How to Run

Simply run the main game file:

```bash
python3 snake_game.py
```

## How to Play

1. **Starting a Game**: 
   - Press the **CALL** button (green button)
   - Or press **SPACE** on your keyboard
2. **Enter Your Name**: Enter your name when prompted
3. **Controls**:
   - **Arrow Buttons**: Use the D-pad navigation buttons (↑↓←→) 
   - **Keyboard**: Use keyboard arrow keys (↑ ↓ ← →)
   - **Pause**: Press the center button (●) on the D-pad or press ENTER
4. **Gameplay**: 
   - Eat the dark food dots to grow and increase your score (+10 per dot)
   - Navigate with the Nokia-style green monochrome screen
   - Grow longer by eating food!
5. **Avoid**: Hitting walls or your own tail (game ends)
6. **Leaderboard**: 
   - Press the **END** button (red button) to view the leaderboard
   - Leaderboard displays on the phone screen
   - Press **END** again to return to game

## Scoring

- Eating food: +10 points
- Leaderboard displays your highest score
- Beat your high score to see the celebration message!

## Database

The game uses SQLite to store:
- User names
- Individual scores
- Timestamps

The database file `snake_game.db` is created automatically in the same directory as the game.

## Files

- `snake_game.py` - Main game file with Nokia UI
- `database.py` - Database management for scores and users
- `snake_game.db` - SQLite database (created automatically)

## Leaderboard

Click the "Leaderboard" button to view:
- Top 10 players by highest score
- Your rank and high score
- All-time best players

Enjoy the game! 🎮


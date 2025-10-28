# Nokia Snake Game

**First app made with Cursor AI Assistant in just 5 minutes! 🚀**  

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

## Quick Setup

```bash
python3 snake_game.py
```

That's it! No dependencies needed - uses Python's built-in `tkinter` and `sqlite3`.

*(If you get an error about tkinter, install it with: `brew install python-tk` on Mac or `sudo apt-get install python3-tk` on Linux)*

## How to Play

**Quick Start:**
1. Click **CALL** or press **SPACE** to start
2. Enter your name when prompted
3. Use arrow buttons or keyboard (↑↓←→) to move
4. Eat the food dots to grow and score points

**Controls:**
- **CALL button** (green) - Start new game
- **Arrow buttons** (↑↓←→) - Move the snake  
- **Center button** (●) - Pause/Resume
- **END button** (red) - View leaderboard
- **Keyboard** - Arrow keys for movement, Space to start

**Rules:**
- Eat food = +10 points
- Avoid walls and your own tail
- Press END to see high scores
- High scores saved automatically!

## What's Under the Hood

**Tech Stack:**
- **Python 3** - Built-in `tkinter` for UI, `sqlite3` for database
- **SQLite** - Stores user names and scores locally
- **Zero dependencies** - Everything uses Python's standard library

**Files:**
- `snake_game.py` - Complete game with Nokia UI (400+ lines of logic!)
- `database.py` - Score tracking and leaderboard system
- `snake_game.db` - Auto-created database file

**Key Features:**
- Real database with user tracking
- On-screen leaderboard (no popups!)
- Authentic Nokia phone interface
- Full game state management

Enjoy the nostalgic fun! 🎮📱


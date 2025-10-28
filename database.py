"""Database module for managing users and scores"""

import sqlite3
import os
from typing import List, Tuple, Optional


class Database:
    def __init__(self, db_path: str = "snake_game.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                score INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        conn.commit()
        conn.close()

    def get_or_create_user(self, name: str) -> int:
        """Get existing user or create a new one, returns user_id"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Try to get existing user
        cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            user_id = result[0]
        else:
            # Create new user
            cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            user_id = cursor.lastrowid

        conn.commit()
        conn.close()
        return user_id

    def save_score(self, user_id: int, score: int):
        """Save a score for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO scores (user_id, score) VALUES (?, ?)", (user_id, score))

        conn.commit()
        conn.close()

    def get_highest_score(self) -> Optional[int]:
        """Get the highest score across all users"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(score) FROM scores")
        result = cursor.fetchone()

        conn.close()
        return result[0] if result[0] is not None else 0

    def get_user_high_score(self, user_id: int) -> int:
        """Get the highest score for a specific user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(score) FROM scores WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()

        conn.close()
        return result[0] if result[0] is not None else 0

    def get_leaderboard(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Get top players with their highest scores"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT u.name, MAX(s.score) as high_score
            FROM users u
            JOIN scores s ON u.id = s.user_id
            GROUP BY u.id, u.name
            ORDER BY high_score DESC
            LIMIT ?
        ''', (limit,))

        results = cursor.fetchall()
        conn.close()

        return results

    def get_all_users(self) -> List[Tuple[int, str]]:
        """Get all users"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM users")
        results = cursor.fetchall()

        conn.close()
        return results


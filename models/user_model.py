import sqlite3  
from database.db import get_db_connection  

class UserModel:
    
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()  
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()  
        return user  

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()  
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  

    @staticmethod
    def find_by_id(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def update_user(id, username=None, password=None):
        fields = []
        values = []
        if username is not None:
            fields.append('username = ?')
            values.append(username)
        if password is not None:
            fields.append('password = ?')
            values.append(password)
        if not fields:
            return False

        conn = get_db_connection()
        try:
            cursor = conn.execute(
                f"UPDATE users SET {', '.join(fields)} WHERE id = ?",
                (*values, id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_user(id):
        conn = get_db_connection()
        try:
            cursor = conn.execute('DELETE FROM users WHERE id = ?', (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()


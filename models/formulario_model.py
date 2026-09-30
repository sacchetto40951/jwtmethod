import sqlite3 
from database.db import get_db_connection  

class FormularioModel:
    
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  

    @staticmethod
    def find_by_id(id):
        conn = get_db_connection()
        formulario = conn.execute(
            'SELECT * FROM formularios WHERE id = ?', (id,)
        ).fetchone()
        conn.close()
        return formulario

    @staticmethod
    def update_formulario(id, data):
        allowed_fields = ('nome', 'email', 'data_nascimento', 'cpf', 'genero')
        fields = [field for field in allowed_fields if field in data]
        if not fields:
            return False

        values = [data[field] for field in fields]
        assignments = ', '.join(f'{field} = ?' for field in fields)
        conn = get_db_connection()
        try:
            cursor = conn.execute(
                f'UPDATE formularios SET {assignments} WHERE id = ?',
                (*values, id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(id):
        conn = get_db_connection()
        try:
            cursor = conn.execute('DELETE FROM formularios WHERE id = ?', (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()
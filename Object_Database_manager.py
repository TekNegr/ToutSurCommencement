import sqlite3


class DatabaseManager:
    def __init__(self, db_name='courses_chevaux.db'):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        # Connexion à la base de données SQLite (ou création si elle n'existe pas)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Création des tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cavalier (
            id_cavalier INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_cavalier TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cheveaux (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_cheval TEXT NOT NULL,
            id_cavalier INTEGER,
            moyenne_des_rang INTEGER,
            FOREIGN KEY (id_cavalier) REFERENCES cavalier (id_cavalier) ON DELETE CASCADE
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS course_futures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trac TEXT NOT NULL,
            date TEXT NOT NULL,
            cheaux_qui_participe TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS course_passées (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trac TEXT NOT NULL,
            date TEXT NOT NULL,
            les_trois_gagnants TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS participation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cheval INTEGER,
            id_course INTEGER NOT NULL,
            is_future_course BOOLEAN NOT NULL,
            FOREIGN KEY (id_cheval) REFERENCES cheveaux (id) ON DELETE CASCADE,
            FOREIGN KEY (id_course) REFERENCES course_passées (id) ON DELETE CASCADE
        );
        ''')

        conn.commit()
        conn.close()
        print("Base de données et tables créées avec succès.")

    def insert_into_table(self, table_name, data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            if table_name == 'cavalier':
                cursor.execute('INSERT INTO cavalier (nom_cavalier) VALUES (?);', (data['nom_cavalier'],))

            elif table_name == 'cheveaux':
                cursor.execute(
                    'INSERT INTO cheveaux (nom_cheval, id_cavalier, moyenne_des_rang) VALUES (?, ?, ?);',
                    (data['nom_cheval'], data['id_cavalier'], data['moyenne_des_rang']))

            elif table_name == 'course_futures':
                cursor.execute('INSERT INTO course_futures (trac, date, cheaux_qui_participe) VALUES (?, ?, ?);',
                               (data['trac'], data['date'], data['cheaux_qui_participe']))

            elif table_name == 'course_passées':
                cursor.execute('INSERT INTO course_passées (trac, date, les_trois_gagnants) VALUES (?, ?, ?);',
                               (data['trac'], data['date'], data['les_trois_gagnants']))

            elif table_name == 'participation':
                cursor.execute('INSERT INTO participation (id_cheval, id_course, is_future_course) VALUES (?, ?, ?);',
                               (data['id_cheval'], data['id_course'], data['is_future_course']))

            else:
                print(f"Table '{table_name}' non reconnue.")
                return

            conn.commit()
            print(f"Données insérées avec succès dans la table '{table_name}'.")

        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion dans la table '{table_name}': {e}")

        finally:
            conn.close()

    def display_table(self, table_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute(f'SELECT * FROM {table_name};')
            rows = cursor.fetchall()

            if not rows:
                print(f"La table '{table_name}' est vide.")
                return

            column_names = [description[0] for description in cursor.description]
            print(f"Contenu de la table '{table_name}':")
            print("\t".join(column_names))

            for row in rows:
                print("\t".join(map(str, row)))

        except sqlite3.Error as e:
            print(f"Erreur lors de l'accès à la table '{table_name}': {e}")

        finally:
            conn.close()

    def update_record(self, table_name, record_id, data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            if table_name == 'cavalier':
                cursor.execute('UPDATE cavalier SET nom_cavalier = ? WHERE id_cavalier = ?;',
                               (data['nom_cavalier'], record_id))

            elif table_name == 'cheveaux':
                cursor.execute(
                    'UPDATE cheveaux SET nom_cheval = ?, id_cavalier = ?, moyenne_des_rang = ? WHERE id = ?;',
                    (data['nom_cheval'], data['id_cavalier'], data['moyenne_des_rang'], record_id))

            elif table_name == 'course_futures':
                cursor.execute('UPDATE course_futures SET trac = ?, date = ?, cheaux_qui_participe = ? WHERE id = ?;',
                               (data['trac'], data['date'], data['cheaux_qui_participe'], record_id))

            elif table_name == 'course_passées':
                cursor.execute('UPDATE course_passées SET trac = ?, date = ?, les_trois_gagnants = ? WHERE id = ?;',
                               (data['trac'], data['date'], data['les_trois_gagnants'], record_id))

            elif table_name == 'participation':
                cursor.execute(
                    'UPDATE participation SET id_cheval = ?, id_course = ?, is_future_course = ? WHERE id = ?;',
                    (data['id_cheval'], data['id_course'], data['is_future_course'], record_id))

            else:
                print(f"Table '{table_name}' non reconnue.")
                return

            conn.commit()
            print(f"Enregistrement mis à jour avec succès dans la table '{table_name}'.")

        except sqlite3.Error as e:
            print(f"Erreur lors de la mise à jour dans la table '{table_name}': {e}")

        finally:
            conn.close()
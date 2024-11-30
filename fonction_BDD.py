import sqlite3

def create_database():
    # Connexion à la base de données SQLite (ou création si elle n'existe pas)
    conn = sqlite3.connect('courses_chevaux.db')
    cursor = conn.cursor()

    # Création de la table cavalier
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cavalier (
        id_cavalier INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_cavalier TEXT NOT NULL
    );
    ''')

    # Création de la table cheveaux
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cheveaux (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_cheval TEXT NOT NULL,
        id_cavalier INTEGER,
        moyenne_des_rang INTEGER,
        FOREIGN KEY (id_cavalier) REFERENCES cavalier (id_cavalier) ON DELETE CASCADE
    );
    ''')

    # Création de la table course_futures
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS course_futures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trac TEXT NOT NULL,
        date TEXT NOT NULL, 
        cheaux_qui_participe TEXT NOT NULL  
    );
    ''')

    # Création de la table course_passées
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS course_passées (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trac TEXT NOT NULL,
        date TEXT NOT NULL,  
        les_trois_gagnants TEXT NOT NULL  
    );
    ''')

    # Création de la table participation (optionnelle)
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

    # Valider les changements et fermer la connexion
    conn.commit()
    conn.close()
    print("Base de données et tables créées avec succès.")


def insert_into_table(table_name, data):
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('courses_chevaux.db')
    cursor = conn.cursor()

    try:
        # Préparation de la requête d'insertion en fonction de la table
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

        # Valider les changements
        conn.commit()
        print(f"Données insérées avec succès dans la table '{table_name}'.")

    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion dans la table '{table_name}': {e}")

    finally:
        # Fermeture de la connexion
        conn.close()

def display_table(table_name):
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('courses_chevaux.db')
    cursor = conn.cursor()

    try:
        # Exécution de la requête pour récupérer les données de la table spécifiée
        cursor.execute(f'SELECT * FROM {table_name};')
        rows = cursor.fetchall()

        # Vérification si la table est vide
        if not rows:
            print(f"La table '{table_name}' est vide.")
            return

        # Affichage des en-têtes de colonne
        column_names = [description[0] for description in cursor.description]
        print(f"Contenu de la table '{table_name}':")
        print("\t".join(column_names))

        # Affichage des lignes de la table
        for row in rows:
            print("\t".join(map(str, row)))

    except sqlite3.Error as e:
        print(f"Erreur lors de l'accès à la table '{table_name}': {e}")

    finally:
        # Fermeture de la connexion
        conn.close()





# Exemple d'utilisation
insert_into_table('cavalier', {'nom_cavalier': 'John Doe'})
insert_into_table('cheveaux', {'nom_cheval': 'Lightning', 'id_cavalier': 1, 'moyenne_des_rang': 2})
insert_into_table('course_futures', {'trac': 'Trac A', 'date': '2024-05-01', 'cheaux_qui_participe': '1,2'})
insert_into_table('course_passées', {'trac': 'Trac B', 'date': '2024-04-01', 'les_trois_gagnants': '1,3,4'})
insert_into_table('participation', {'id_cheval': 1, 'id_course': 1, 'is_future_course': True})


# Exemple d'utilisation
display_table('cheveaux')  # Remplacez 'cheveaux' par le nom de la table que vous souhaitez afficher
display_table('cavalier')
display_table('course_futures')
display_table('course_passées')
display_table('participation')
# Appel de la fonction pour créer la base de données
#create_database()
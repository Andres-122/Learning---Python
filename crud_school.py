import sqlite3
from datetime import datetime

# Función para conectarse a la base de datos
def connect_database():
    return sqlite3.connect('school.db')

# Función para insertar un país
def create_country(conn):
    name = input("Nombre del país: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripción: ")
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO countries (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                     (name, abrev, descrip, created_at, updated_at))
    print("País creado exitosamente.")

# Función para insertar un departamento
def create_department(conn):
    name = input("Nombre del departamento: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripción: ")
    id_country = int(input("ID del país al que pertenece: "))
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO departments (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                     (name, abrev, descrip, id_country, created_at, updated_at))
    print("Departamento creado exitosamente.")

# Función para insertar una ciudad
def create_city(conn):
    name = input("Nombre de la ciudad: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripción: ")
    id_dept = int(input("ID del departamento al que pertenece: "))
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                     (name, abrev, descrip, id_dept, created_at, updated_at))
    print("Ciudad creada exitosamente.")

# Función para insertar un tipo de identificación
def create_identification_type(conn):
    name = input("Nombre del tipo de identificación: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripción: ")
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                     (name, abrev, descrip, created_at, updated_at))
    print("Tipo de identificación creado exitosamente.")

# Función para insertar un usuario
def create_user(conn):
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    status = bool(input("Estado (0 para inactivo, 1 para activo): "))
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                     (email, password, status, created_at, updated_at))
    print("Usuario creado exitosamente.")

# Función para insertar una persona
def create_person(conn):
    first_name = input("Nombre: ")
    last_name = input("Apellido: ")
    id_ident_type = int(input("ID del tipo de identificación: "))
    ident_number = input("Número de identificación: ")
    id_exp_city = int(input("ID de la ciudad de expedición: "))
    address = input("Dirección: ")
    mobile = input("Número de teléfono móvil: ")
    id_users = int(input("ID del usuario asociado: "))
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                     (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users, created_at, updated_at))
    print("Persona creada exitosamente.")

# Función para insertar un estudiante
def create_student(conn):
    code = input("Código del estudiante: ")
    id_persons = int(input("ID de la persona asociada: "))
    status = bool(input("Estado (0 para inactivo, 1 para activo): "))
    created_at = updated_at = datetime.now()

    with conn:
        conn.execute("INSERT INTO students (code, id_persons, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                     (code, id_persons, status, created_at, updated_at))
    print("Estudiante creado exitosamente.")

# Función principal
def main():
    conn = connect_database()
    while True:
        print("\nMain menú")
        print("[1]. Crear país")
        print("[2]. Crear departamento")
        print("[3]. Crear ciudad")
        print("[4]. Crear tipo de identificación")
        print("[5]. Crear usuario")
        print("[6]. Crear persona")
        print("[7]. Crear estudiante")
        print("[8]. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_country(conn)
        elif choice == '2':
            create_department(conn)
        elif choice == '3':
            create_city(conn)
        elif choice == '4':
            create_identification_type(conn)
        elif choice == '5':
            create_user(conn)
        elif choice == '6':
            create_person(conn)
        elif choice == '7':
            create_student(conn)
        elif choice == '8':
            break
        else:
            print("Opción invalida. Inténtelo de nuevo.")

    conn.close()

if __name__ == "__main__":
    main()

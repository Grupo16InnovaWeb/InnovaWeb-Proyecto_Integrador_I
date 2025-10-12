from services import list_users, create_user

def seed_admin():
    users = list_users()
    if len(users) == 0:
        print("No hay usuarios. Creando usuario admin inicial.")
        username = input("Admin username (ej: admin): ").strip()
        email = input("Admin email (ej: admin@example.com): ").strip()
        password = input("Admin password: ").strip()
        create_user(username=username, email=email, password=password, role="admin")
        print("Admin creado.")
    else:
        print("Ya existen usuarios. Saltando seed.")

if __name__ == "__main__":
    seed_admin()

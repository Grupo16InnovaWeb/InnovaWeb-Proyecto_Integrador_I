# main.py
from services import create_user, authenticate_user, update_user_profile, get_user_by_username_or_email
from admin_cli import admin_menu
from seed_admin import seed_admin

def user_menu(user):
    while True:
        print(f"\n--- Bienvenido {user['username']} (rol: {user['role']}) ---")
        print("1) Ver mis datos")
        print("2) Editar perfil (username/email/password)")
        print("3) Logout")
        opt = input("Opción: ").strip()
        if opt == "1":
            print(f"ID: {user['id']}\nUsername: {user['username']}\nEmail: {user['email']}\nRol: {user['role']}\nCreado: {user['created_at']}")
        elif opt == "2":
            new_username = input("Nuevo username (enter = sin cambios): ").strip() or None
            new_email = input("Nuevo email (enter = sin cambios): ").strip() or None
            change_pwd = input("Cambiar password? (si/no): ").strip().lower()
            new_password = None
            if change_pwd == "si":
                while True:
                    new_password = input("Nuevo password: ").strip()
                    if new_password:
                        break
                    print("La contraseña no puede estar vacía.")
            updated = update_user_profile(user['id'], username=new_username, email=new_email, password=new_password)
            if updated:
                user = get_user_by_username_or_email(new_username or user['username'])
                print("Perfil actualizado.")
            else:
                print("No se realizaron cambios.")
        else:
            break

def main():
    # Crear admin si no existe
    seed_admin()

    while True:
        print("\n--- InnovaWeb (Consola) ---")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("3) Salir")
        choice = input("Opción: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            while True:
                pwd = input("Password: ").strip()
                if pwd:
                    break
                print("La contraseña no puede estar vacía.")
            try:
                create_user(username=username, email=email, password=pwd, role="user")
                print("Registrado correctamente. Hacé login para continuar.")
            except Exception as e:
                print("Error al registrar:", e)

        elif choice == "2":
            u = input("Username o email: ").strip()
            p = input("Password: ").strip()
            user = authenticate_user(u, p)
            if user:
                print("Login OK.")
                if user['role'] == "admin":
                    admin_menu(user)
                else:
                    user_menu(user)
            else:
                print("Credenciales inválidas.")

        elif choice == "3":
            print("Saliendo. Chau!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

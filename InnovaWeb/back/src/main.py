from services import create_user, authenticate_user, update_user_profile, get_user_by_username
from admin_cli import admin_menu
from seed_admin import seed_admin
import getpass

def user_menu(user):
    while True:
        print(f"\n--- Bienvenido {user.username} (rol: {user.role}) ---")
        print("1) Ver mis datos")
        print("2) Editar perfil (username/email/password)")
        print("3) Logout")
        opt = input("Opción: ").strip()
        if opt == "1":
            print(f"ID: {user.id}\nUsername: {user.username}\nEmail: {user.email}\nRol: {user.role}\nCreado: {user.created_at}")
        elif opt == "2":
            new_username = input("Nuevo username (enter = sin cambios): ").strip() or None
            new_email = input("Nuevo email (enter = sin cambios): ").strip() or None
            change_pwd = input("Cambiar password? (si/no): ").strip().lower()
            new_password = None
            if change_pwd == "si":
                new_password = getpass.getpass("Nuevo password: ")
            updated = update_user_profile(user.id, username=new_username, email=new_email, password=new_password)
            user = updated  # actualizar el objeto en sesión local
            print("Perfil actualizado.")
        else:
            break

def main():
    seed_admin()  # opcional: crea admin si no hay usuarios
    while True:
        print("\n--- InnovaWeb (Consola) ---")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("3) Salir")
        choice = input("Opción: ").strip()
        if choice == "1":
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            pwd = getpass.getpass("Password: ")
            try:
                user = create_user(username=username, email=email, password=pwd, role="user")
                print("Registrado correctamente. Hacé login para continuar.")
            except Exception as e:
                print("Error al registrar:", e)
        elif choice == "2":
            u = input("Username o email: ").strip()
            p = getpass.getpass("Password: ")
            user = authenticate_user(u, p)
            if user:
                print("Login OK.")
                if user.role == "admin":
                    admin_menu(user)
                else:
                    user_menu(user)
            else:
                print("Credenciales inválidas.")
        else:
            print("Saliendo. Chau!")
            break

if __name__ == "__main__":
    main()

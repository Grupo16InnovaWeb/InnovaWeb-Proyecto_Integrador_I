from services import list_users, change_role, delete_user

def admin_menu(admin_user):
    while True:
        print("\n--- Menú Admin ---")
        print("1) Listar usuarios")
        print("2) Cambiar rol de usuario")
        print("3) Eliminar usuario")
        print("4) Volver / Logout")
        opt = input("Opción: ").strip()
        if opt == "1":
            users = list_users()
            print("\nID | Username | Email | Role | Created")
            for u in users:
                print(f"{u.id} | {u.username} | {u.email} | {u.role} | {u.created_at}")
        elif opt == "2":
            uid = int(input("ID de usuario a modificar: "))
            new_role = input("Nuevo rol (user/admin): ").strip()
            try:
                user = change_role(uid, new_role)
                print(f"Rol actualizado: {user.username} -> {user.role}")
            except Exception as e:
                print("Error:", e)
        elif opt == "3":
            uid = int(input("ID de usuario a eliminar: "))
            confirm = input("Confirma eliminación? (si): ").strip().lower()
            if confirm == "si":
                try:
                    delete_user(uid)
                    print("Usuario eliminado.")
                except Exception as e:
                    print("Error:", e)
        else:
            break

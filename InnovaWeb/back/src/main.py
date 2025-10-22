from sistema_auth import SistemaAuth
from menu_sistema import MenuSistema

def mostrar_menu_principal():
    print("\n=== SISTEMA DE E-COMMERCE TECNOLOGÍA ===")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Ver productos (sin registro)")
    print("4. Salir")

def main():
    auth = SistemaAuth()
    menu = MenuSistema()

    try:
        while True:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                auth.registrar_usuario()
            elif opcion == "2":
                usuario = auth.iniciar_sesion()
                if usuario:
                    if usuario.rol == "admin":
                        menu.mostrar_menu_admin(auth)
                    else:
                        menu.mostrar_menu_usuario(usuario)
            elif opcion == "3":
                # Permitir ver productos sin estar logueado
                menu.gestor_productos.listar_productos()
            elif opcion == "4":
                print("¡Hasta luego! 👋")
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-4.")
    finally:
        auth.cerrar_conexion()
        menu.gestor_productos.cerrar_conexion()

if __name__ == "__main__":
    main()
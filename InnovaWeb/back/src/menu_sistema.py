from gestor_productos import GestorProductos

class MenuSistema:
    def __init__(self):
        self.gestor_productos = GestorProductos()

    def mostrar_menu_usuario(self, usuario):
        while True:
            print(f"\n--- MENÚ USUARIO: {usuario.nombre_usuario} ---")
            print("1. Ver todos los productos")
            print("2. Buscar productos por categoría")
            print("3. Ver mis datos")
            print("4. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestor_productos.listar_productos()
            elif opcion == "2":
                self.gestor_productos.buscar_productos_por_categoria()
            elif opcion == "3":
                print(f"\n--- MIS DATOS ---")
                print(usuario.mostrar_datos())
            elif opcion == "4":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.")

    def mostrar_menu_admin(self, auth):
        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Gestión de Usuarios")
            print("2. Gestión de Productos")
            print("3. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_gestion_usuarios(auth)
            elif opcion == "2":
                self.menu_gestion_productos()
            elif opcion == "3":
                print("Saliendo del menú de administrador...")
                break
            else:
                print("Opción inválida.")

    def menu_gestion_usuarios(self, auth):
        while True:
            print("\n--- GESTIÓN DE USUARIOS ---")
            print("1. Ver todos los usuarios")
            print("2. Cambiar rol de usuario")
            print("3. Eliminar usuario")
            print("4. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuarios = auth.obtener_todos_usuarios()
                print("\n--- LISTA DE USUARIOS ---")
                for usuario in usuarios:
                    print(usuario.mostrar_datos())

            elif opcion == "2":
                nombre = input("Ingrese el nombre de usuario a modificar: ")
                usuario = auth.buscar_usuario(nombre)
                if usuario:
                    print(f"Usuario actual: {usuario.mostrar_datos()}")
                    nuevo_rol = input("Nuevo rol (admin/usuario): ").lower()
                    if nuevo_rol in ["admin", "usuario"]:
                        if auth.actualizar_rol_usuario(nombre, nuevo_rol):
                            print("✅ Rol actualizado correctamente.")
                        else:
                            print("❌ Error al actualizar el rol.")
                    else:
                        print("❌ Rol inválido. Debe ser 'admin' o 'usuario'.")
                else:
                    print("❌ Usuario no encontrado.")

            elif opcion == "3":
                nombre = input("Ingrese el nombre de usuario a eliminar: ")
                usuario = auth.buscar_usuario(nombre)
                if usuario:
                    if usuario.nombre_usuario == "admin":
                        print("❌ No se puede eliminar al usuario admin por defecto.")
                    else:
                        confirmacion = input(f"¿Está seguro de eliminar a {nombre}? (s/n): ")
                        if confirmacion.lower() == 's':
                            if auth.eliminar_usuario(nombre):
                                print("✅ Usuario eliminado correctamente.")
                            else:
                                print("❌ Error al eliminar usuario.")
                else:
                    print("❌ Usuario no encontrado.")

            elif opcion == "4":
                break
            else:
                print("❌ Opción inválida.")

    def menu_gestion_productos(self):
        while True:
            print("\n--- GESTIÓN DE PRODUCTOS ---")
            print("1. Crear producto")
            print("2. Listar todos los productos")
            print("3. Buscar productos por categoría")
            print("4. Actualizar producto")
            print("5. Eliminar producto")
            print("6. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Para crear producto necesitamos un usuario, usar admin por defecto
                from user import Usuario
                admin_usuario = Usuario("admin", "", "admin", 1)
                self.gestor_productos.crear_producto(admin_usuario)
            elif opcion == "2":
                self.gestor_productos.listar_productos()
            elif opcion == "3":
                self.gestor_productos.buscar_productos_por_categoria()
            elif opcion == "4":
                self.gestor_productos.actualizar_producto()
            elif opcion == "5":
                self.gestor_productos.eliminar_producto()
            elif opcion == "6":
                break
            else:
                print("❌ Opción inválida.")
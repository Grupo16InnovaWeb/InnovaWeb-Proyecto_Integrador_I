Documentación del Proyecto Integrador
 Estructura del Proyecto

Frontend
Contiene los recursos de la interfaz gráfica del sistema:
- css/ → hojas de estilo (layout, colores, tipografías).  
- img/ → imágenes, íconos y recursos gráficos optimizados.  
- js/ → lógica del lado del cliente (validaciones, dinámicas de UI).  

Convenciones:
- Archivos en minúsculas con guiones medios (`main-style.css`, `form-validation.js`).  
- Imágenes optimizadas (`.jpg`, `.png`, `.webp`).  
- Scripts comentados para explicar su uso.  

---
Backend
Contiene la lógica de negocio y gestión de datos:
- sql/ → scripts SQL de creación de tablas, relaciones y datos de prueba.  
- src/ → código fuente del backend (modelos, controladores, servicios).  

Convenciones:
- Scripts SQL numerados según orden de ejecución (`01-create-tables.sql`, `02-insert-data.sql`).  
- Código en `src/` organizado en módulos, respetando la nomenclatura estándar de clases y métodos.  
- Separación clara de responsabilidades (modelo, vista, controlador).  

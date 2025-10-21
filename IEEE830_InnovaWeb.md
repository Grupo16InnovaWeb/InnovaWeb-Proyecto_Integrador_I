Especificación de Requisitos de Software (SRS)
 Proyecto: Plataforma de Comercio Electrónico InnovaWeb - Versión 1.0
 Equipo InnovaWeb
 1. Introducción
 1.1 Propósito
 El presente documento especifica los requisitos del software para el desarrollo de la plataforma de
 comercio electrónico InnovaWeb. Está dirigido al equipo de desarrollo, responsables de pruebas,
 administradores del sistema y demás interesados. Su objetivo es definir de forma clara y verificable
 las funcionalidades, restricciones y características del sistema.
 1.2 Alcance
 InnovaWeb será una plataforma de comercio electrónico escalable que permitirá: experiencia de
 compra segura e intuitiva para los usuarios finales, herramientas de gestión robustas para
 administradores, sistema modular, adaptable y escalable, e infraestructura técnica sólida y
 mantenible.
 1.3 Definiciones, siglas y abreviaturas
 MVP: Producto Mínimo Viable DER: Diagrama Entidad-Relación BD: Base de Datos SRS:
 Software Requirements Specification
 1.4 Referencias
 IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.
 Documentación técnica interna del equipo InnovaWeb (versión 1.0).
 1.5 Visión general del documento
 El documento se estructura en: descripción general del sistema, requisitos funcionales y no
 funcionales, interfaces externas, consideraciones adicionales (seguridad, legales y métricas) y
 apéndices.
 2. Descripción general
 2.1 Perspectiva del producto
 El producto se desarrollará como una plataforma web modular con arquitectura escalable y base
 de datos relacional normalizada.
 2.2 Funcionalidades del producto
Catálogo de productos, gestión de usuarios, carrito de compras, sistema de pagos e integración
 con pasarelas externas, y administración.
 2.3 Características de los usuarios
 Clientes finales (usuarios) y administradores.
 2.4 Restricciones
 Uso de base de datos relacional con integridad referencial, cumplimiento de normativas de
 privacidad de datos, MVP en un plazo de 8-10 semanas.
 2.5 Suposiciones y dependencias
 Infraestructura en la nube para despliegue, servicios externos (pasarelas de pago, logística, correo
 electrónico).
 3. Requisitos específicos
 3.1 Requisitos funcionales
 Gestión de usuarios: registro, inicio de sesión, actualización y eliminación. Catálogo de productos:
 alta, baja, modificación, búsqueda, filtros y reseñas. Carrito de compras: gestión de artículos,
 persistencia de sesión, cálculo automático. Sistema de pagos: integración con múltiples pasarelas,
 confirmaciones automáticas, historial de órdenes. Administración: panel de control, reportes y
 gestión de roles.
 3.2 Requisitos no funcionales
 Rendimiento: tiempo de carga menor a 2 segundos. Disponibilidad: 99.9% de tiempo en línea.
 Seguridad: encriptación de datos sensibles. Escalabilidad: crecimiento automático bajo carga.
 3.3 Interfaces externas
 Interfaces de usuario: interfaz web responsiva. Interfaces de software: APIs de pasarelas de pago
 y logística. Interfaces de comunicación: notificaciones vía email/SMS.
 4. Otros requisitos
 4.1 Consideraciones de seguridad
 Encriptación de contraseñas y datos sensibles, protocolos de seguridad actualizados, protección
 contra fraudes y vulnerabilidades.
 4.2 Restricciones legales y normativas
Cumplimiento de normativas de privacidad (ej. GDPR/leyes locales), políticas de protección de
 datos de clientes.
 4.3 Métricas de éxito
 Tiempo de carga < 2 segundos, escalabilidad demostrada en pruebas de carga, satisfacción del
 usuario medida en encuestas.
 5. Apéndices
 Glosario ampliado. Diagramas: DER, casos de uso, clases (ubicados en docs/). Cronograma de
 fases: Planificación (2-3 semanas), Desarrollo núcleo (8-10 semanas), Funcionalidades avanzadas
 (6-8 semanas), Pruebas y lanzamiento (2-3 semanas). Ejemplos de scripts SQL y ejecución en
 consola
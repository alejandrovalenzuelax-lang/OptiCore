# Requerimientos funcionales y no funcionales

## Objetivo del documento

Este documento define qué debe hacer el sistema OptiCore en su primera etapa y qué condiciones técnicas y operativas deben cumplirse durante su desarrollo.

---

## 1. Requerimientos funcionales

### 1.1 Gestión de óptica
El sistema debe permitir:

- registrar la información principal de una óptica
- almacenar nombre comercial, dirección, teléfonos y datos de contacto
- almacenar branding básico como logo y colores
- relacionar usuarios, pacientes, productos, ventas y citas con una óptica específica

### 1.2 Gestión de usuarios
El sistema debe permitir:

- iniciar sesión
- cerrar sesión
- registrar usuarios internos
- asignar roles
- restringir acceso según permisos
- activar o desactivar usuarios

### 1.3 Gestión de pacientes
El sistema debe permitir:

- crear pacientes
- editar información de pacientes
- consultar pacientes existentes
- buscar pacientes por nombre, teléfono o folio
- consultar el historial de expedientes de un paciente

Campos relevantes iniciales:
- nombre
- edad
- ocupación
- teléfonos
- empresa
- compañía
- domicilio
- colonia
- municipio
- beneficiario
- parentesco

### 1.4 Gestión de expedientes
El sistema debe permitir:

- crear expedientes clínicos
- editar expedientes
- consultar expedientes anteriores
- registrar receta anterior
- registrar receta actual
- registrar observaciones clínicas
- registrar condiciones visuales y médicas
- registrar uso previo de lentes
- registrar datos del armazón
- registrar optometrista y vendedor asociados
- registrar fecha de entrega
- generar un folio interno por expediente o paciente según se defina

El expediente debe contemplar al menos:
- datos generales del paciente
- RX anterior
- historial visual y médico
- RX actual
- tipo de lente
- observaciones
- datos de armazón
- responsable de atención
- datos de entrega

### 1.5 Gestión de inventario
El sistema debe permitir administrar productos de distintas categorías:

- armazones
- lentes
- lentes de sol
- pupilentes
- soluciones
- accesorios

Operaciones mínimas:
- alta de producto
- edición de producto
- activación o desactivación
- consulta de existencias
- búsqueda y filtrado
- control de stock
- definición de precio de compra y precio de venta

### 1.6 Punto de venta
El sistema debe permitir:

- registrar ventas
- asociar una venta a un paciente cuando aplique
- asociar una venta a un expediente cuando aplique
- registrar conceptos vendidos
- registrar armazón y lente como conceptos separados cuando sea necesario
- calcular total
- registrar anticipo
- calcular saldo pendiente
- registrar método de pago
- registrar fecha de venta
- registrar fecha de entrega
- registrar estatus de la venta

### 1.7 Gestión de citas
El sistema debe permitir:

- crear citas manualmente
- asignar fecha y hora
- relacionar la cita con un paciente
- registrar motivo
- cambiar estatus de la cita
- agregar notas

Integraciones futuras:
- confirmación por WhatsApp
- confirmación por SMS

### 1.8 Promociones y paquetes
El sistema debe permitir:

- crear promociones temporales
- definir vigencia
- activar o desactivar promociones
- crear paquetes con precio fijo
- asociar descripción de lo que incluye cada paquete

### 1.9 Reparación de lentes
El sistema debe permitir:

- registrar solicitudes de reparación
- guardar observaciones
- indicar fecha de recepción
- indicar fecha estimada de entrega
- actualizar estatus del servicio

### 1.10 Página pública de la óptica
El sistema debe permitir mostrar información pública básica:

- nombre de la óptica
- logo
- colores
- dirección
- ubicación
- medios de contacto
- servicios ofrecidos
- marcas manejadas
- productos destacados
- información general del negocio

Nota:
La página pública no requiere pagos en línea en la primera etapa.

---

## 2. Requerimientos no funcionales

### 2.1 Usabilidad
- la aplicación debe ser usable por personal no técnico
- la interfaz debe priorizar claridad y rapidez de captura
- el sistema debe ser responsive para escritorio, tablet y móvil

### 2.2 Seguridad
- los usuarios deben autenticarse para acceder a la parte administrativa
- cada usuario solo debe ver información correspondiente a su óptica
- debe existir control de permisos por rol
- los datos sensibles no deben exponerse públicamente

### 2.3 Escalabilidad
- aunque el sistema se use inicialmente en una sola óptica, la arquitectura debe permitir soportar múltiples ópticas en el futuro
- la estructura de datos debe contemplar separación por óptica desde el inicio

### 2.4 Mantenibilidad
- el proyecto debe estar documentado
- el código debe seguir una estructura clara por módulos
- las decisiones de negocio importantes deben quedar por escrito

### 2.5 Rendimiento
- las búsquedas principales deben responder de forma fluida en operaciones cotidianas
- el sistema debe soportar uso concurrente básico para una óptica pequeña

---

## 3. Prioridades iniciales

### Prioridad alta
- autenticación
- usuarios
- pacientes
- expedientes
- inventario
- ventas
- anticipos y saldos

### Prioridad media
- citas
- promociones
- paquetes
- reparaciones

### Prioridad baja en primera etapa
- página pública avanzada
- confirmaciones automatizadas
- facturación automatizada
- pagos en línea

---

## 4. Funcionalidades fuera del alcance inicial

Por ahora no forman parte del MVP:

- CFDI/facturación automatizada
- integración formal con PAC
- pagos en línea
- aplicación móvil nativa
- analítica avanzada
- multi-tenant comercial completo con autoservicio

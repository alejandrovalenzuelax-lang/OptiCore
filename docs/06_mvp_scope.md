# Alcance del MVP

## Objetivo del MVP

Construir una primera versión funcional de OptiCore que permita digitalizar procesos críticos de la óptica de origen sin intentar resolver todas las necesidades desde el inicio.

El MVP debe ser suficientemente útil para que el negocio pueda comenzar a operar con el sistema en tareas reales.

---

## 1. Qué debe resolver el MVP

El MVP debe resolver como mínimo estas necesidades:

- acceso seguro al sistema
- registro de usuarios internos
- registro y consulta de pacientes
- captura y consulta de expedientes
- control básico de inventario
- registro de ventas
- control de anticipos y saldos
- registro de fecha de entrega
- operación básica desde una interfaz web

---

## 2. Módulos incluidos en el MVP

### 2.1 Autenticación y usuarios
Incluye:
- login
- logout
- usuarios internos
- roles básicos

### 2.2 Pacientes
Incluye:
- alta de pacientes
- edición de pacientes
- búsqueda de pacientes
- consulta individual

### 2.3 Expedientes
Incluye:
- creación de expedientes
- edición de expedientes
- consulta de expedientes previos
- registro de RX anterior y actual
- observaciones y datos clínicos principales

### 2.4 Inventario
Incluye:
- alta de productos
- edición de productos
- clasificación por categoría
- visualización de existencias
- control básico de stock

### 2.5 Ventas
Incluye:
- creación de venta
- conceptos de venta
- total
- anticipo
- saldo
- método de pago
- fecha de entrega
- estatus básico

---

## 3. Qué no entra en el MVP inicial

Estas funciones se consideran fuera del alcance de la primera versión:

- facturación CFDI automatizada
- integración con PAC
- pagos en línea
- integración formal con WhatsApp
- confirmaciones automáticas por SMS
- reportes avanzados
- promociones complejas
- paquetes avanzados
- reparación de lentes completa
- página pública avanzada
- autoservicio multi-tenant comercial

---

## 4. Posibles funcionalidades para una versión intermedia

Después del MVP, podrían incorporarse:

- citas manuales
- dashboard con métricas básicas
- impresión/exportación de documentos
- promociones simples
- módulos de reparación
- página pública básica de la óptica

---

## 5. Criterios para considerar que el MVP está listo

Se puede considerar que el MVP está listo cuando:

- un usuario puede iniciar sesión correctamente
- se pueden registrar pacientes
- se pueden crear y consultar expedientes
- se pueden registrar productos en inventario
- se puede registrar una venta con total, anticipo y saldo
- se puede consultar información sin depender del expediente en papel
- la óptica puede usar el sistema en al menos parte de su operación diaria

---

## 6. Enfoque de implementación recomendado

Orden sugerido:

1. base del backend Django
2. autenticación y usuarios
3. pacientes
4. expedientes
5. inventario
6. ventas
7. frontend inicial en React
8. mejoras de experiencia de usuario

---

## 7. Meta real del MVP

La meta no es tener un producto comercial completo, sino una herramienta funcional, usable y útil para una óptica real.

Si además la base queda suficientemente ordenada para crecer a futuro, el MVP habrá cumplido una segunda meta estratégica.

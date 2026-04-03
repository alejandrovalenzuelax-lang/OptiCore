# Modelo de datos inicial

## Objetivo del documento

Definir las entidades principales, sus relaciones y la lógica general del modelo relacional de OptiCore.

El sistema se construirá primero para una sola óptica, pero el diseño de datos considerará desde el inicio la posibilidad de soportar múltiples ópticas.

---

## 1. Enfoque general

La base de datos estará orientada a una estructura relacional en PostgreSQL.

La entidad `optica` funcionará como referencia principal para separar la información de cada negocio. La mayoría de las entidades operativas del sistema deberán pertenecer a una óptica.

Este enfoque permite:

- usar una sola base de datos
- reutilizar la misma aplicación para varias ópticas
- aislar la información de cada negocio
- escalar sin reestructurar todo el sistema más adelante

---

## 2. Entidades principales

### 2.1 Optica
Representa un negocio específico dentro del sistema.

Campos sugeridos:
- id
- nombre
- slug
- telefono
- email
- direccion
- ciudad
- estado
- codigo_postal
- logo_url
- colores_tema
- activa
- created_at
- updated_at

### 2.2 Usuario
Representa a una persona que accede al sistema.

Campos sugeridos:
- id
- optica_id
- nombre
- apellidos
- email
- password_hash
- rol
- activo
- ultimo_acceso
- created_at
- updated_at

Nota:
En Django es recomendable extender o adaptar el modelo de usuario según la estrategia elegida.

### 2.3 Paciente
Representa a una persona atendida por la óptica.

Campos sugeridos:
- id
- optica_id
- folio_interno
- nombre
- apellidos
- fecha_nacimiento
- edad
- sexo
- ocupacion
- telefono_casa
- telefono_celular
- telefono_empresa
- extension_empresa
- empresa
- compania
- domicilio
- colonia
- municipio
- beneficiario
- parentesco
- notas_generales
- activo
- created_at
- updated_at

### 2.4 Expediente
Representa el registro clínico y administrativo asociado a una atención visual.

Campos sugeridos:
- id
- optica_id
- paciente_id
- folio
- fecha
- empresa
- observaciones_generales

#### RX anterior
- rx_anterior_od_sph
- rx_anterior_od_cyl
- rx_anterior_od_eje
- rx_anterior_od_add
- rx_anterior_oi_sph
- rx_anterior_oi_cyl
- rx_anterior_oi_eje
- rx_anterior_oi_add

#### Historial visual y médico
- fotofobia
- irritacion
- ardor
- lagrimeo
- cefalea
- borrosa
- cerca
- lejos
- glaucoma
- trauma_ocular
- estrabismo
- uveitis
- queratocono
- pterigion
- orzuelo
- conjuntivitis
- diabetes
- presion_arterial
- corazon
- operaciones
- uso_lentes
- tiempo_uso_lentes

#### RX actual
- rx_od_sph
- rx_od_cyl
- rx_od_eje
- rx_od_add
- rx_oi_sph
- rx_oi_cyl
- rx_oi_eje
- rx_oi_add

#### Lente y armazón
- tipo_lente
- observaciones_lente
- di
- alt
- armazon_marca
- armazon_modelo
- armazon_color
- armazon_tamano

#### Atención y seguimiento
- optometrista_id
- vendedor_id
- fecha_entrega
- observaciones_entrega
- created_at
- updated_at

### 2.5 Producto
Representa un artículo inventariable o vendible.

Campos sugeridos:
- id
- optica_id
- nombre
- categoria
- marca
- modelo
- color
- tamano
- descripcion
- sku
- codigo_barras
- precio_compra
- precio_venta
- stock_actual
- stock_minimo
- activo
- created_at
- updated_at

### 2.6 Venta
Representa una transacción comercial.

Campos sugeridos:
- id
- optica_id
- paciente_id
- expediente_id
- usuario_id
- folio
- subtotal
- descuento
- total
- anticipo
- saldo
- metodo_pago
- fecha_venta
- fecha_entrega
- estatus
- observaciones
- created_at
- updated_at

### 2.7 VentaDetalle
Representa cada concepto incluido en una venta.

Campos sugeridos:
- id
- venta_id
- producto_id
- descripcion
- cantidad
- precio_unitario
- descuento_linea
- total_linea
- created_at
- updated_at

### 2.8 Cita
Representa un evento de agenda.

Campos sugeridos:
- id
- optica_id
- paciente_id
- usuario_id
- fecha_hora
- motivo
- estatus
- notas
- canal_confirmacion
- created_at
- updated_at

### 2.9 Promocion
Representa una promoción temporal.

Campos sugeridos:
- id
- optica_id
- nombre
- descripcion
- fecha_inicio
- fecha_fin
- activa
- created_at
- updated_at

### 2.10 Paquete
Representa una combinación fija de productos o servicios.

Campos sugeridos:
- id
- optica_id
- nombre
- descripcion
- precio
- activo
- created_at
- updated_at

### 2.11 Reparacion
Representa un servicio de reparación.

Campos sugeridos:
- id
- optica_id
- paciente_id
- descripcion
- observaciones
- fecha_recepcion
- fecha_entrega_estimada
- fecha_entrega_real
- estatus
- created_at
- updated_at

---

## 3. Relaciones principales

- una óptica tiene muchos usuarios
- una óptica tiene muchos pacientes
- una óptica tiene muchos productos
- una óptica tiene muchas ventas
- una óptica tiene muchas citas
- una óptica tiene muchas promociones
- una óptica tiene muchos paquetes
- una óptica tiene muchas reparaciones
- un paciente pertenece a una óptica
- un paciente puede tener muchos expedientes
- un expediente pertenece a un paciente
- una venta puede asociarse a un paciente
- una venta puede asociarse a un expediente
- una venta tiene muchos detalles
- una cita puede asociarse a un paciente
- una reparación puede asociarse a un paciente

---

## 4. Decisiones iniciales de diseño

### Separación por óptica
Las tablas operativas deben incluir referencia a la óptica correspondiente para permitir aislamiento lógico de información.

### Soporte gradual para escalabilidad
Aunque la primera implementación esté enfocada en una sola óptica, el modelo debe evitar decisiones que obliguen a rediseñar la base de datos más adelante.

### Preferencia por claridad
En esta primera etapa se privilegia un modelo entendible y mantenible antes que una hiper-normalización prematura.

### Campos clínicos específicos
El expediente inicial se basará en el formato físico actualmente utilizado por la óptica de origen, para facilitar adopción y captura.

---

## 5. Entidades prioritarias para primera implementación

Las primeras entidades que deberían implementarse en Django son:

- Optica
- Usuario
- Paciente
- Expediente
- Producto
- Venta
- VentaDetalle
- Cita

Estas cubren la mayor parte del flujo operativo inicial del sistema.

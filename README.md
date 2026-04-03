# OptiCore

OptiCore es un sistema web para digitalizar y centralizar la operación de ópticas independientes.

El proyecto nace a partir de una necesidad real: una óptica familiar que actualmente maneja procesos operativos y administrativos de forma manual, principalmente en papel. La meta inicial es construir una solución funcional para ese negocio real, y al mismo tiempo sentar las bases para escalar la plataforma a otras ópticas en el futuro.

## Problema que resuelve

Muchas ópticas pequeñas o medianas no cuentan con herramientas digitales para administrar su operación diaria. Esto genera problemas como:

- expedientes físicos difíciles de consultar
- control deficiente de inventario
- poca visibilidad sobre ventas, anticipos y saldos
- dependencia de procesos manuales para citas y seguimiento
- dificultad para estandarizar la operación del negocio

OptiCore busca resolver estos problemas mediante una plataforma unificada, clara y escalable.

## Objetivos del proyecto

### Objetivo principal
Desarrollar una primera versión funcional que ayude a digitalizar la operación diaria de la óptica de origen.

### Objetivo secundario
Diseñar la solución con una arquitectura que permita reutilizar código y eventualmente ofrecer el sistema a otras ópticas.

### Objetivo personal del desarrollo
Construir un proyecto real, bien documentado y técnicamente sólido que también funcione como experiencia práctica y pieza de portafolio profesional.

## Módulos principales

- gestión de pacientes
- gestión de expedientes clínicos
- inventario de productos ópticos
- punto de venta
- control de anticipos y saldos
- agenda de citas
- configuración básica de la óptica
- futura página pública para promoción de servicios

## Stack tecnológico inicial

### Backend
- Django
- Django REST Framework

### Frontend
- React

### Base de datos
- PostgreSQL

### Estilos
- Tailwind CSS

## Arquitectura general

OptiCore se plantea como una aplicación web con frontend y backend desacoplados:

- un backend en Django expone la lógica de negocio, autenticación, administración y API REST
- un frontend en React consume la API y presenta la interfaz operativa
- PostgreSQL almacena la información relacional del sistema
- la estructura del modelo considera desde el inicio la posibilidad de soportar múltiples ópticas

## Estado actual

El proyecto se encuentra en fase de planeación y definición funcional/técnica.

Actualmente se trabaja en:

- definición de visión de producto
- documentación de requerimientos
- diseño del modelo de datos
- delimitación del alcance del MVP
- planeación del roadmap inicial de desarrollo

## Enfoque de desarrollo

El desarrollo seguirá una estrategia incremental:

1. definir requerimientos y reglas de negocio
2. modelar entidades y relaciones
3. implementar backend base
4. implementar frontend inicial
5. entregar una primera versión útil para operación diaria
6. iterar con retroalimentación real del negocio

## Roadmap inicial

### Fase 0
- documentación inicial del proyecto
- definición del alcance MVP
- diseño del modelo relacional

### Fase 1
- setup de backend con Django
- configuración de PostgreSQL
- autenticación básica
- modelo base de óptica, usuarios y pacientes

### Fase 2
- expedientes clínicos
- inventario
- ventas y control de pagos

### Fase 3
- citas
- mejoras de interfaz
- reportes básicos

### Fase 4
- página pública
- promociones y paquetes
- mejoras orientadas a comercialización futura

## Principios del proyecto

- resolver primero un problema real
- mantener una arquitectura limpia y entendible
- priorizar utilidad sobre complejidad innecesaria
- documentar decisiones importantes
- construir una base escalable sin sobreingeniería temprana

## Notas

OptiCore está siendo diseñado primero para una óptica específica, pero con la intención de dejar preparada una base suficientemente ordenada para escalar a más negocios en el futuro.

Proyecto: MVP Bares de Sevilla

1. OBJETIVO DE LA FASE

Definir la estructura funcional y técnica del MVP antes de comenzar el desarrollo completo del sistema.

Esta fase describe:

funcionamiento general
pantallas principales
flujo de usuario
estructura frontend/backend
comunicación entre tecnologías

2. ESTRUCTURA GENERAL DEL SISTEMA

La aplicación se dividirá en:

Frontend

Responsable de:

interfaz visual
navegación
filtros
renderizado de bares

Tecnologías:

React
JavaScript
HTML
CSS
Backend

Responsable de:

lógica del sistema
API REST
consultas base de datos

Tecnologías:

Python
Django
Base de datos

Responsable de almacenar:

bares
categorías
zonas
información descriptiva

Tecnología:

MySQL
3. FLUJO GENERAL DEL USUARIO
Entrada principal

El usuario accederá a la pantalla Home.

En ella verá:

nombre/logo de la aplicación
categorías principales
zonas destacadas
listado inicial de bares
Navegación prevista

El usuario podrá:

seleccionar categoría
seleccionar zona
entrar en la ficha individual de un bar
4. PANTALLAS PRINCIPALES DEL MVP
HOME
Contenido
barra principal
categorías
filtros rápidos
bares destacados
Funcionalidad técnica

React cargará la información desde Django mediante peticiones API.

LISTADO DE BARES
Contenido
cards de bares
imagen
categoría
zona
especialidad
Funcionalidad técnica

El frontend solicitará datos filtrados al backend.

DETALLE INDIVIDUAL DEL BAR
Contenido
descripción
dirección
especialidad
imágenes
Funcionalidad técnica

La información será obtenida desde la API mediante el ID del bar.

5. COMUNICACIÓN FRONTEND ↔ BACKEND
Flujo técnico
Usuario
↓
React
↓ petición HTTP
Django API
↓ consulta SQL
MySQL
↓ respuesta JSON
React renderiza información

6. ESTRUCTURA INICIAL BACKEND
Aplicación principal Django
bares

Responsabilidades:

gestión bares
filtros
endpoints API

7. ESTRUCTURA INICIAL FRONTEND
Componentes previstos
Home
BarCard
BarList
BarDetail
Navbar
Filters

8. ENDPOINTS INICIALES PREVISTOS
GET /api/bares
GET /api/bares/zona/<zona>
GET /api/bares/categoria/<categoria>
GET /api/bar/<id>

9. MODELO INICIAL DE DATOS
Tabla: bares
Campo	Función
nombre	nombre del bar
descripcion	descripción
categoria	tipo de bar
zona	ubicación
direccion	dirección física
imagen	imagen principal
especialidad	producto destacado

10. OBJETIVO TÉCNICO DEL MVP

El objetivo técnico inicial será:

tener backend funcional
exponer API REST
mostrar bares dinámicamente
aplicar filtros básicos
mantener arquitectura escalable
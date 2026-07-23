# AGENTS.md — MVP Bares de Sevilla

## 1. Contexto del proyecto

Este proyecto tiene como objetivo construir un MVP de una aplicación web para descubrir bares de Sevilla.

La aplicación permitirá encontrar establecimientos mediante:

- zonas
- categorías
- características
- información práctica del establecimiento

El objetivo inicial es validar una idea de negocio mediante un producto funcional, sencillo y mantenible.

La prioridad es terminar una base sólida antes de añadir funcionalidades avanzadas.


---

# 2. Objetivo actual del proyecto

La prioridad actual es completar el MVP.

Orden de prioridades:

1. Backend estable.
2. Modelo de datos correcto.
3. API REST funcional.
4. Frontend funcional.
5. Integración completa.
6. Deploy inicial.


No añadir funcionalidades fuera del MVP hasta completar esta fase.


---

# 3. Arquitectura del sistema

La aplicación utiliza una arquitectura separada por capas.


## Frontend

Tecnología:

- React

Responsabilidades:

- interfaz visual
- experiencia de usuario
- navegación
- filtros visuales
- consumo de API REST


---

## Backend

Tecnologías:

- Python
- Django
- Django REST Framework

Responsabilidades:

- lógica de negocio
- gestión de datos
- API REST
- validaciones


---

## Base de datos

Tecnología:

- MySQL

Responsabilidad:

- almacenamiento persistente de información


---

# 4. Principios de desarrollo

Durante el desarrollo seguir estas reglas:

- Priorizar simplicidad antes que complejidad.
- Evitar sobreingeniería.
- Mantener código limpio y mantenible.
- Respetar separación de responsabilidades.
- Crear únicamente funcionalidades necesarias.
- Documentar cambios importantes.


---

# 5. Restricciones importantes

No realizar antes de finalizar el MVP:

- IA avanzada.
- Sistemas multiagente.
- Automatizaciones complejas.
- Arquitecturas innecesarias.
- Optimización prematura.


No utilizar:

- SQLite como base de datos final.
- Mezcla entre frontend y backend.
- Código sin revisar.


---

# 6. Metodología de trabajo

El proyecto utiliza metodología Agile.

Elementos:

- Sprints.
- Backlog.
- Daily Log.
- Sprint Review.
- Retrospectivas.


Cada sprint debe tener:

- objetivo definido;
- tareas concretas;
- resultado funcional.


El estado del proyecto debe mantenerse actualizado en el Agile Daily Log.


---

# 7. Reglas para modificar código

Antes de realizar cambios importantes:

1. Analizar la estructura existente.
2. Revisar documentación relacionada.
3. Explicar la solución propuesta.
4. Implementar el cambio.
5. Validar funcionamiento.


Cambios específicos:


## Django Models

Siempre:

- modificar models.py;
- ejecutar makemigrations;
- ejecutar migrate;
- comprobar base de datos.


## API REST

Actualizar:

- serializers;
- views;
- endpoints;
- documentación.


## Nuevas funcionalidades

Actualizar:

- Daily Log.
- Documentación correspondiente.
- Changelog cuando exista una nueva versión.


---

# 8. Seguridad

Aplicar buenas prácticas:

- Variables sensibles en archivos .env.
- No subir claves privadas a GitHub.
- Validar datos recibidos.
- Preparar futura autenticación.
- No almacenar información sensible sin protección.


---

# 9. Uso de Inteligencia Artificial

La IA funciona como asistente técnico.

Puede ayudar en:

- análisis;
- arquitectura;
- explicación de código;
- generación de código;
- documentación.


Flujo recomendado:

1. Comprender problema.
2. Diseñar solución.
3. Revisar propuesta.
4. Implementar.
5. Probar.
6. Documentar.


La decisión final siempre pertenece al desarrollador.


---

# 10. Uso futuro de agentes IA

Los agentes, MCP y Skills podrán incorporarse en fases posteriores.


Posibles usos:

- automatización de tareas;
- generación de contenido;
- análisis de datos;
- recomendaciones inteligentes;
- mantenimiento.


No forman parte del MVP actual.


---

# 11. Estilo de trabajo

Mantener:

- código limpio;
- documentación profesional;
- Markdown claro;
- nombres descriptivos.


Evitar:

- contenido innecesario;
- duplicidad de documentación;
- soluciones complejas sin necesidad.
# Sistema Experto de Recetas de Cocina (Prolog Chef SE)

> **Unidad de Aprendizaje:** Paradigmas de Programación  
> **Escuela Superior de Cómputo (ESCOM) - Instituto Politécnico Nacional**  
> **Paradigma:** Programación Lógica | **Lenguaje:** SWI-Prolog + Python (Flask)

---

## Enlace a la Aplicación Pública
**URL de Producción:** [https://recetas-5wih.onrender.com/](https://recetas-5wih.onrender.com/) 
*(Desplegado en producción sobre un contenedor Docker con SWI-Prolog real)*

---

## Descripción del Proyecto
Este proyecto consiste en un **Sistema Experto interactivo** diseñado para resolver el problema cotidiano de la selección de recetas de cocina a partir de los ingredientes disponibles en el hogar y restricciones alimentarias del usuario (como dietas vegetarianas o sin lácteos).

El motor de razonamiento lógico está verdaderamente implementado en **SWI-Prolog** mediante un conjunto de hechos, relaciones y reglas de inferencia no triviales, evaluando sustitutos de ingredientes y exclusiones por seguridad alimentaria.

---

## Arquitectura del Sistema

El proyecto sigue una arquitectura desacoplada cliente-servidor:
[ Usuario / Navegador Web ]
│
▼  (Petición HTTP POST JSON)
[ Frontend Web: HTML5 + Tailwind CSS + JavaScript ]
│
▼  (Comunicación en tiempo real)
[ Servicio Web / API: Python (Flask) ]
│
▼  (Invocación vía Subprocess / CLI)
[ Motor de Inferencia Lógico: SWI-Prolog (recetas.pl) ]

1. **Frontend:** Interfaz web intuitiva desarrollada con HTML5, Tailwind CSS y JavaScript para capturar la selección del usuario.
2. **Backend (API REST):** Servidor Python con Flask que traduce las peticiones web en consultas nativas a Prolog y procesa las respuestas.
3. **Motor Lógico:** SWI-Prolog ejecutando la base de conocimientos `recetas.pl`.

---

## Base de Conocimientos (`recetas.pl`)

La base de conocimientos incluye:
* **+20 Hechos:** Definición de ingredientes base de platillos, hechos de sustitución/equivalencia (`ingrediente_alternativo/2`) y categorías por momento del día (`tipo_receta/2`).
* **10 Reglas Lógicas:**
  1. `es_del_momento/2`: Verificación de categoría/momento del día.
  2. `recomendar_receta/2`: Inferencia de disponibilidad con sustitución automática.
  3. `recomendar_por_categoria/3`: Filtrado combinado por tipo de comida e ingredientes.
  4. `recomendar_desayuno/2`: Regla específica para desayunos.
  5. `recomendar_comida/2`: Regla específica para comidas.
  6. `recomendar_cena/2`: Regla específica para cenas.
  7. `receta_sin_carne/1`: Regla de seguridad alimentaria usando **Negación por Falla (`\+`)**.
  8. `receta_sin_lacteos/1`: Exclusión de lácteos mediante **Negación por Falla (`\+`)**.
  9. `recomendar_vegetariano/2`: Inferencia combinada de dieta vegetariana y disponibilidad.
  10. `contiene_picante/2`: Evaluación directa de ingredientes picantes.

---

## Tecnologías Utilizadas
* **Lenguaje Lógico:** SWI-Prolog (`swipl`)
* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3 (Tailwind CSS), JavaScript (Fetch API)
* **Contenedorización:** Docker (Imagen base `swipl:latest`)
* **Control de Versiones & Despliegue:** Git, GitHub, Render

---

## Instalación y Ejecución Local

### Prerrequisitos
* Tienes que tener instalado [SWI-Prolog](https://www.swi-prolog.org/) y [Python 3](https://www.python.org/).

### Pasos para ejecutar:
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/licamubi2012-lang/recetas.git](https://github.com/licamubi2012-lang/recetas.git)
   cd recetas

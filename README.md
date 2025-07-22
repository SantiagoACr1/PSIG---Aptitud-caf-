# Clasificación de Aptitud para la Producción de Café en el Departamento del Huila

## 📍 Universidad Nacional de Colombia  
**Curso:** Programación SIG
**Integrantes:**
- Cristian Santiago Acuña Ramírez  
- Avdoni Sánchez Reinoso  
*Estudiantes de Maestría en Geomática - Universidad Nacional de Colombia*

---

## 🎯 Objetivo del Proyecto

Este proyecto tiene como propósito identificar y clasificar las áreas con mayor potencial productivo para el cultivo de café en el departamento del Huila, Colombia. Se implementa un flujo de trabajo basado en programación SIG, análisis espacial, y geoprocesamiento de variables edafológicas, logísticas y legales, con el fin de generar una evaluación cartográfica de aptitud agrícola.

---

## 🧭 Metodología General

1. **Selección del área de estudio:**  
   Se delimita el departamento del Huila como zona prioritaria por su relevancia cafetera a nivel nacional.

2. **Clasificación preliminar de aptitud:**  
   Se consideran variables agronómicas clave (pendiente, profundidad, textura, etc.) para categorizar la aptitud en:  
   - A1 (Alta)  
   - A2 (Media)  
   - A3 (Baja)  
   - N1 (No apta)

3. **Análisis logístico complementario:**  
   Se incorporan factores como:  
   - Accesibilidad a red vial  
   - Proximidad a estaciones climáticas  

4. **Exclusión normativa:**  
   Se excluyen áreas con restricciones legales o ambientales (áreas protegidas, zonas de conservación, etc.).

5. **Síntesis cartográfica:**  
   Generación del mapa final de aptitud ajustada y visualización de resultados.

---

## 🧩 Estructura del Repositorio

```
📁 /notebooks				# Flujo principal y análisis de datos (contiene cuaderno compilado y divido por tratamiento de datos)
    	└── data_preparation.ipynb      
📁 /results				# Salidas gráficas
	└── maps
	└── charts           		
📁 /src                             	# Scripts auxiliares
📁 /docs 				# Referencias
📁 /datebase				# Archivos en formato .shp, .gbd, .csv, .xlsx como insumo para los cuadernos
📄 README.md                         	# Documentación general
```

---

## ⚙️ Requisitos del Entorno

Este proyecto fue desarrollado en JupyterLab. Se requieren las siguientes librerías:

```bash
pip install geopandas rasterio rasterstats matplotlib pandas contextily geemap earthengine-api
```

Además, es necesaria la autenticación con Google Earth Engine:

```bash
earthengine authenticate
```

---


## 🗺️ Resultados

- Clasificación de aptitud del suelo según pendiente, profundidad, drenaje y textura.
- Análisis zonales por polígono de acuerdo con pendiente, temperatura y precipitación.
- Capas ajustadas por logística y restricciones legales.
- Salida cartográfica de aptitud de producción de café.

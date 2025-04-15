# AutoCleaner

Script simple en Python para automatizar la limpieza de archivos **temporales** o **antiguos** en una carpeta específica.

---

## ¿Qué hace?

- Escanea una carpeta que tú elijas
- Elimina archivos con extensiones como `.tmp`, `.log`, `.bak`, etc.
- Borra archivos que no se hayan usado en los últimos X días
- Respeta una lista blanca de archivos que nunca deben borrarse
- Muestra por consola los archivos eliminados

---

## Requisitos

- Python 3 instalado

---

## ¿Cómo usar?

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/AutoCleaner.git
   cd AutoCleaner

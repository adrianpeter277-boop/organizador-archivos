# 🗂️ Organizador Automático de Archivos

Un script en Python que organiza automáticamente los archivos de una carpeta moviéndolos a subcarpetas según su tipo.

---

## 📋 Descripción

¿Tu carpeta de Descargas es un caos? Este script la ordena automáticamente en segundos, clasificando cada archivo en su carpeta correspondiente según su extensión.

---

## 🚀 Uso

```bash
python organizador.py
```

El script te pedirá la ruta de la carpeta que quieres organizar:

```
¿Qué carpeta quieres organizar? /home/usuario/Descargas
Movido: foto.jpg → Imágenes/
Movido: documento.pdf → PDFs/
Movido: cancion.mp3 → Música/
¡Listo! Carpeta organizada.
```

---

## 📁 Categorías

| Carpeta      | Extensiones                          |
|--------------|--------------------------------------|
| Imágenes     | .jpg, .jpeg, .png, .gif, .svg        |
| Videos       | .mp4, .mov, .avi, .mkv               |
| PDFs         | .pdf                                 |
| Música       | .mp3, .wav, .flac                    |
| Documentos   | .doc, .docx, .txt, .xlsx             |
| Otros        | Todo lo que no encaje arriba         |

---

## 🛠️ Requisitos

- Python 3.x
- No necesita librerías externas (usa `os` y `shutil` que vienen con Python)

---

## 📂 Estructura del proyecto

```
organizador-archivos/
│
├── organizador.py    # Script principal
└── README.md         # Este archivo
```

---

## 💡 Posibles mejoras futuras

- [ ] Añadir más tipos de archivo
- [ ] Registro de archivos movidos en un `.log`
- [ ] Soporte para deshacer la organización
- [ ] Interfaz gráfica

---

## 👤 Autor

Hecho con 🐍 Python por [tu nombre]

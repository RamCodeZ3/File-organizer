# 🗂️ File Organizer

**File Organizer** es un pequeño programa de escritorio desarrollado en **Python** con **CustomTkinter** que te permite **organizar tus archivos automáticamente por tipo de formato** (imágenes, documentos, videos, etc.) dentro de carpetas separadas.  
Ideal para mantener tu carpeta de *Descargas* o *Escritorio* limpia y ordenada en segundos.

---

## 🚀 Características

- ✅ Interfaz gráfica moderna con **CustomTkinter**.  
- ✅ Selección fácil de carpeta de origen y destino.  
- ✅ Organización automática de archivos según su extensión.  
- ✅ Creación automática de carpetas por tipo (ej: `PNG`, `PDF`, `MP4`, etc.).  
- ✅ Evita mover carpetas o archivos del sistema.  
- ✅ Manejo de errores y mensajes claros al usuario.  

---

## 🧠 ¿Cómo funciona?

El programa analiza todos los archivos dentro de la carpeta seleccionada como **origen**.  
Luego, según su tipo (`.png`, `.pdf`, `.mp3`, etc.), los mueve a subcarpetas dentro de la carpeta **destino**.  
Ejemplo:

```
📂 Descargas
 ┣ 📜 documento.pdf
 ┣ 🖼️ imagen.png
 ┣ 🎵 cancion.mp3
 ┗ 📹 video.mp4
```

Después de ejecutar File Organizer 👇  

```
📂 Archivos Ordenados
 ┣ 📂 PDF
 ┃ ┗ documento.pdf
 ┣ 📂 PNG
 ┃ ┗ imagen.png
 ┣ 📂 MP3
 ┃ ┗ cancion.mp3
 ┗ 📂 MP4
    ┗ video.mp4
```

---

## 🧩 Estructura del proyecto  

📦 **File Organizer**  
┣ 📂 env  
┣ 📂 src  
┃ ┣ 📂 UI  
┃ ┃ ┗ 📜 app.py — Interfaz gráfica (CustomTkinter)  
┃ ┣ 📂 utils  
┃ ┃ ┗ 📜 organize_file.py — Lógica de organización  
┃ ┗ 📜 main.py — Punto de entrada principal  
┣ 📜 .gitignore  
┣ 📜 LICENSE  
┣ 📜 README.md  
┗ 📜 requirements.txt  

---

## 🛠️ Instalación  

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/file-organizer.git
   cd file-organizer
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # En Windows
   source venv/bin/activate   # En Linux/Mac
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el programa:**
   ```bash
   python src/main.py
   ```

---

## ⚙️ Tecnologías utilizadas  

- 🐍 **Python 3.x**  
- 🎨 **CustomTkinter** (Interfaz moderna)  
- 📁 **os / shutil / pathlib** (Manejo de archivos y rutas)  
- 💡 **Tkinter filedialog** (Selección de carpetas)

---

## 💬 Ejemplo de uso  

1️⃣ Abre el programa.  
2️⃣ Selecciona la carpeta **de origen** (por ejemplo, Descargas).  
3️⃣ Selecciona la carpeta **de destino**.  
4️⃣ Haz clic en **Organizar**.  
5️⃣ ¡Listo! Tus archivos estarán ordenados automáticamente.

---

## 🧾 Licencia  
Este proyecto está bajo la licencia **MIT**.

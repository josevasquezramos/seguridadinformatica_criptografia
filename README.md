<p align="center"><a href="https://www.uns.edu.pe" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Universidad_Nacional_del_Santa_Logo.png" width="250" alt="UNS Logo"></a></p>

# Seguridad Informática - Criptografía

Este proyecto es una aplicación web educativa desarrollada como parte del curso de **Seguridad Informática** por estudiantes del 9no ciclo de **Ingeniería de Sistemas e Informática** de la **Universidad Nacional del Santa**.

El sistema está diseñado para explicar conceptos clave de criptografía, demostrando su funcionamiento mediante algoritmos interactivos implementados en Python.

## 🚀 Instalación

Sigue estos pasos para correr el proyecto en tu máquina local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/josevasquezramos/seguridadinformatica_criptografia.git
cd seguridadinformatica_criptografia
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

En Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python criptografia/app.py
```

## 🧠 Temas de Criptografía
A continuación se describen brevemente los temas cubiertos en la aplicación:

### 🔁 Sistemas de Cifra en Flujo
Utilizan una clave y un generador pseudoaleatorio para cifrar bit a bit o carácter por carácter. Suelen ser rápidos y se usan en aplicaciones en tiempo real, como transmisiones de voz y video.

### 🧱 Cifrado Simétrico en Bloque
Cifra datos en bloques de tamaño fijo (ej. 64 o 128 bits) usando la misma clave para cifrar y descifrar. Ejemplos: AES, DES. Requiere manejo cuidadoso de claves y modos de operación (ECB, CBC, etc.).

### 🎒 Cifrado Asimétrico con Mochilas
Basado en el problema de la mochila (knapsack problem). Aunque fue una de las primeras propuestas de cifrado asimétrico, algunos esquemas fueron rotos. Se estudia por su valor histórico y educativo.

### ⬆️ Cifrado Asimétrico Exponencial
Se basa en operaciones matemáticas difíciles de invertir, como la exponenciación modular. El ejemplo más famoso es RSA, usado para cifrado y firma digital.

### 🧬 Funciones Hash en Criptografía
Transforman datos de entrada de cualquier tamaño en una salida de tamaño fijo (hash). Son deterministas, rápidas y resistentes a colisiones. Usadas para verificar integridad y en firmas digitales.

### 🔐 Autenticación y Firma Digital
Verifican la identidad del emisor y la integridad del mensaje. Las firmas digitales combinan funciones hash con cifrado asimétrico para proporcionar no repudio.

### 📄 Certificados Digitales
Emitidos por una autoridad de certificación (CA), vinculan claves públicas con identidades. Usados en HTTPS y en sistemas de confianza digital.

### ⚛️ Criptografía Cuántica
Explora el uso de principios de la mecánica cuántica para asegurar la comunicación. Promete seguridad incluso ante ataques de computadoras cuánticas, usando técnicas como distribución cuántica de claves (QKD).

### ⛓️ Blockchain
Tecnología distribuida y segura que permite almacenar información de forma inmutable. Usa funciones hash, firmas digitales y consenso para mantener una cadena de bloques sin necesidad de confianza centralizada.

---

### 👥 Integrantes
-	ALCANTARA ZUÑIGA Alex Rodolfo
-	PANTA PISCOCHE Jose Diego
-	RAMOS ENCARNACION Nilton
-	TREJO OBREGON Rodrigo Emilio
-	VASQUEZ RAMOS Jose Manuel

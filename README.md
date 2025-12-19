El propósito de este proyecto es combinar pruebas de interfaz web (ui) utilizando Selenium WebDrive con Servicios Rest mediante una libreria Request ejecutandose bajo el framework Pytest. Los entornos utilizados para dicho proyecto son SauceDemo y DummyJSON. 

***El objetivo principal es proporcionar un entorno completo para:***

* Automatizar pruebas UI utilizando Selenium.
* Ejecutar pruebas de API utilizando Requests.
* Practicar integración de pruebas UI + API.
* Implementar buenas prácticas con Pytest (fixtures, modularización, asserts).
* Generar reportes de ejecución y logs de evidencia.

***Tecnologías Utilizadas:***

* **Python 3.14.0** – Lenguaje principal.
* **Pytest** – Framework para la ejecución de pruebas.
* **Selenium WebDriver** – Automatización de interfaces web.
* **Requests** – Cliente HTTP para pruebas de API (DummyJSON).

***Estructura del Proyecto***

<img width="150" height="316" alt="{BE458707-F65B-44D2-AF4A-37B2B5E5877D}" src="https://github.com/user-attachments/assets/846870c4-5647-438b-8fb8-5ec19e7352d8" />

***Instalar dependencias:***

*Dentro del proyecto ingresar la siguiente linea de código:*

pip install -r requirements.txt

***Ejecución de pruebas:***

*Todas las pruebas:*

pytest -v

*Solo pruebas UI:*

pytest tests/web -v

*Solo pruebas API:*

pytest tests/api -v

***Interpretación de los Reportes Generados***

*Reporte HTML (por pytest-html)*

Se genera un archivo en:

reports/reporte.html

Incluye:

* Estado de cada prueba (PASSED / FAILED / SKIPPED)
* Capturas de pantalla (UI)
* Logs
* Mensajes de error con stacktrace

 Screenshots

Para pruebas UI fallidas, Selenium guarda capturas en:

screenshots/

Esto permite identificar visualmente el estado del navegador en el momento del error.

*Ejecución de Pruebas UI*

Las pruebas UI utilizan Selenium con WebDriver para abrir la página de SauceDemo, realizar login, agregar productos y completar un proceso de compra.

Verifican:

* Autenticación
* Navegación correcta
* Interacción con elementos
* Validación de flujos end-to-end

*Ejecución de Pruebas API*

Se validan:

* Códigos de estado (200, 201, 400, 204)
* Estructura del JSON
* Contenido de la respuesta
* Requests GET, POST, DELETE


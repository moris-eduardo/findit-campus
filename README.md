# FindIt Campus

Backend académico para una plataforma de objetos perdidos dentro de un campus universitario.

El proyecto modela usuarios, zonas, objetos y reclamaciones, con el objetivo de soportar un flujo claro desde el registro de un objeto hasta su entrega.

## Tecnologías

- Python y Django
- MySQL
- Django REST Framework
- JWT y CORS
- Cloudinary para imágenes

## Aportación principal

Mi contribución se concentró en el modelado y la configuración inicial del backend:

- Modelo de usuario con roles y correo institucional.
- Modelos y migraciones para zonas del campus, objetos y reclamaciones.
- Restricciones de unicidad, UUID y estados de seguimiento.
- Configuración de MySQL, JWT, CORS y almacenamiento de imágenes.

## Ejecutar localmente

1. Crea y activa un entorno virtual de Python.
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Copia `.env.example` como `.env` y completa la configuración local.
4. Configura una instancia local de MySQL y ejecuta las migraciones de Django.

```bash
python manage.py migrate
python manage.py runserver
```

## Estado

Proyecto académico en desarrollo. La interfaz y las rutas completas de la API no están incluidas todavía.

## Licencia

Consulta [LICENSE](LICENSE).

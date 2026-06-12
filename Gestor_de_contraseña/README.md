# Gestor de Contraseñas

Gestor de Contraseñas es una aplicación de consola en Python para almacenar y administrar credenciales básicas de servicios.

## Qué hace

- Agrega contraseñas para servicios junto a usuario/correo y contraseña.
- Muestra todas las contraseñas guardadas.
- Busca contraseñas por nombre de servicio.
- Elimina contraseñas existentes.
- Guarda los datos en un archivo JSON local.

## Estructura del proyecto

- `src/main.py`: menú principal e interacción con el usuario.
- `src/gestor_contraseña.py`: funciones para cargar, guardar y administrar contraseñas.
- `data/contraseña.json`: archivo donde se almacenan las contraseñas.

## Requisitos

- Python 3.x

## Cómo usar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```bash
python3 src/main.py
```

3. Sigue el menú:

- `1` Agregar contraseña
- `2` Mostrar contraseñas
- `3` Buscar contraseña
- `4` Eliminar contraseña
- `5` Salir

## Detalles importantes

- Las contraseñas se guardan en texto claro en `data/contraseña.json`.
- Esta aplicación no es una solución de almacenamiento seguro; se recomienda usarla solo para pruebas o como base para mejorar la seguridad.

## Mejoras sugeridas

- Cifrar los datos almacenados.
- Añadir una contraseña maestra para proteger el acceso.
- Validar mejor la entrada del usuario.
- Implementar una interfaz gráfica o web.

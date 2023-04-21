# BOT-ULTRA-VISITAS-YOUTUBE

# Actualizador automático de navegadores para YouTube

Este código en Python utiliza Selenium para abrir múltiples navegadores y actualizar automáticamente una página de YouTube en cada uno de ellos. 

## Configuración

En la sección de configuración, puedes especificar:

- `NUM_NAVEGADORES`: el número de navegadores que deseas abrir.
- `URL`: la URL de la página de YouTube que deseas actualizar.
- `TIEMPO_VISTA`: el tiempo que quieres que cada navegador permanezca en la página antes de actualizarla.

## Cómo funciona

Una vez que se han abierto los navegadores, el programa entra en un ciclo infinito que sigue los siguientes pasos:

1. Selecciona un navegador aleatorio de la lista.
2. Actualiza la página en el navegador seleccionado.
3. Imprime un mensaje indicando qué navegador se ha actualizado.
4. Espera un tiempo aleatorio antes de continuar con la próxima actualización.

El programa continúa este ciclo de forma indefinida, actualizando la página de YouTube en diferentes navegadores de forma automática y aleatoria.

## Personalización adicional

Si deseas personalizar aún más el programa, hay algunas opciones adicionales que puedes utilizar:

- Puedes agregar un proxy para cada navegador para evitar ser detectado como un robot. Simplemente descomenta las líneas relevantes en el código.
- Puedes modificar los valores de `TIEMPO_VISTA` para hacer que cada navegador permanezca más o menos tiempo en la página antes de actualizarla.

¡Diviértete con tu nuevo actualizador automático de navegadores! 

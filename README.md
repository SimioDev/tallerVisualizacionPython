## Taller - Dashboard de Ventas con Matplotlib

Entrega del taller de visualización de datos para la asignatura Diseño Funcional.

## Archivos incluidos

`dashboard_simple.py`: script principal que lee el archivo CSV, genera las cuatro gráficas requeridas y guarda el dashboard como imagen.

`sales_data_2024.csv`: archivo con los 50 registros reales de ventas utilizados (fecha, producto, categoría, región, monto, cantidad, etc.).

`mi_dashboard_ventas.png`: imagen final del dashboard (se genera automáticamente al ejecutar el script).

## Cómo ejecutar

Primero se instalan las dependencias necesarias (solo la primera vez):

```bash
pip3 install matplotlib pandas numpy
``` 

Luego pues ejecuta el script:

```bash
python3 dashboard_simple.py
``` 

El programa abre la ventana con el dashboard y guarda la imagen mi_dashboard_ventas.png en la misma carpeta.


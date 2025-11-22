#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ============================================================================
# PASO 1: CARGAR LOS DATOS
# ============================================================================
print("=" * 60)
print("PASO 1: CARGANDO DATOS")
print("=" * 60)

# Cargar el archivo CSV real
df = pd.read_csv('sales_data_2024.csv')

print("Datos cargados exitosamente")
print(f"   Total de registros: {len(df)}")
print(f"   Columnas: {df.columns.tolist()}")

# ============================================================================
# PASO 2: PREPARAR LA FIGURA PRINCIPAL
# ============================================================================
print("\n" + "=" * 60)
print("PASO 2: CREANDO DASHBOARD")
print("=" * 60)

# Figura más grande y profesional
fig = plt.figure(figsize=(16, 10))
fig.suptitle('DASHBOARD DE VENTAS 2024 - ANÁLISIS COMPLETO', 
             fontsize=18, fontweight='bold', color='#C5282F')

# ============================================================================
# PASO 3: CREAR 4 GRÁFICAS BÁSICAS
# ============================================================================

# ------------------------------------
# GRÁFICA 1: Ventas por Producto (Superior Izquierda)
# ------------------------------------
ax1 = plt.subplot(2, 2, 1)

ventas_por_producto = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

x_pos = range(len(ventas_por_producto))
bars1 = ax1.bar(x_pos, ventas_por_producto.values, color='#0077BE', edgecolor='navy', alpha=0.8)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(ventas_por_producto.index, rotation=60, ha='right')
ax1.set_title('Ventas Totales por Producto', fontsize=12, fontweight='bold')
ax1.set_ylabel('Ventas (COP $)', fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Agregar valores encima de las barras
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 100000,
             f'${height:,.0f}', ha='center', va='bottom', fontsize=9)

print("Gráfica 1: Ventas por Producto - Completada")

# ------------------------------------
# GRÁFICA 2: Distribución por Región (Superior Derecha)
# ------------------------------------
ax2 = plt.subplot(2, 2, 2)

ventas_por_region = df.groupby('Region')['Sales'].sum()

colores = ['#C5282F', '#0077BE', '#28A745', '#FFC107', '#6f42c1']
wedges, texts, autotexts = ax2.pie(ventas_por_region.values,
                                   labels=ventas_por_region.index,
                                   colors=colores,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   textprops={'fontsize': 10, 'fontweight': 'bold'})

ax2.set_title('Distribución de Ventas por Región', fontsize=12, fontweight='bold')

print("Gráfica 2: Distribución por Región - Completada")

# ------------------------------------
# GRÁFICA 3: Tendencia de Ventas Diarias (Inferior Izquierda)
# ------------------------------------
ax3 = plt.subplot(2, 2, 3)

# Convertir Date a datetime y agrupar por fecha
df['Date'] = pd.to_datetime(df['Date'])
ventas_diarias = df.groupby('Date')['Sales'].sum()

ax3.plot(ventas_diarias.index, ventas_diarias.values,
         color='#28A745', linewidth=3, marker='o', markersize=6, markerfacecolor='white', markeredgewidth=2)
ax3.fill_between(ventas_diarias.index, ventas_diarias.values, alpha=0.2, color='#28A745')
ax3.set_title('Tendencia de Ventas Diarias (2024)', fontsize=12, fontweight='bold')
ax3.set_xlabel('Fecha', fontweight='bold')
ax3.set_ylabel('Ventas Totales (COP $)', fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='x', rotation=45)

# Formato de fechas más limpio
ax3.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %d'))
ax3.xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=5))

print("Gráfica 3: Tendencia de Ventas - Completada")

# ------------------------------------
# GRÁFICA 4: Top 5 Productos Más Vendidos (Inferior Derecha)
# ------------------------------------
ax4 = plt.subplot(2, 2, 4)

top_5_productos = ventas_por_producto.nlargest(5)

y_pos = range(len(top_5_productos))
bars4 = ax4.barh(y_pos, top_5_productos.values, color='#DC3545', edgecolor='darkred', alpha=0.9)
ax4.set_yticks(y_pos)
ax4.set_yticklabels(top_5_productos.index, fontweight='bold')
ax4.set_title('Top 5 Productos Más Vendidos', fontsize=12, fontweight='bold')
ax4.set_xlabel('Ventas Totales (COP $)', fontweight='bold')
ax4.invert_yaxis()  # El más alto arriba

# Valores al final de las barras
for i, bar in enumerate(bars4):
    width = bar.get_width()
    ax4.text(width + 100000, bar.get_y() + bar.get_height()/2,
             f'${width:,.0f}', va='center', fontweight='bold', fontsize=10)

print("Gráfica 4: Top 5 Productos - Completada")

# ============================================================================
# PASO 4: AJUSTAR EL LAYOUT
# ============================================================================
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ============================================================================
# PASO 5: GUARDAR Y MOSTRAR
# ============================================================================
print("\n" + "=" * 60)
print("PASO 5: GUARDANDO DASHBOARD")
print("=" * 60)

plt.savefig('mi_dashboard_ventas.png', dpi=200, bbox_inches='tight', facecolor='white')
print("Dashboard guardado exitosamente como 'mi_dashboard_ventas.png'")

plt.show(block=True)   # con block=True se comporta normal

print("\n" + "=" * 60)
print("Fin.")
print("=" * 60)

"""
Script mejorado para componente GhPython de Grasshopper

INPUTS en Grasshopper:
    materials: Lista de materiales (Tree Access -> List)
    quantities: Lista de cantidades en m³ (Tree Access -> List) 
    climate: Zona climática ('hot', 'temperate', 'cold') (String)
    run: Botón para ejecutar (Boolean)

OUTPUTS:
    report: Reporte formateado (String)
    circular_score: Score de circularidad 0-100% (Float)
    carbon_total: Carbono total en kgCO₂ (Float)
    cost_total: Costo total en USD (Float)
    recommendations: Recomendaciones (List)
    optimized_materials: Materiales optimizados (List)
"""

import sys
import os
import json

# Configuración automática de paths - MÁS ROBUSTO
python_paths = [
    r"C:\Python39\Lib\site-packages",
    r"C:\Python310\Lib\site-packages", 
    r"C:\Python311\Lib\site-packages",
    r"C:\Users\{}\AppData\Local\Programs\Python\Python39\Lib\site-packages".format(os.getenv('USERNAME')),
    r"C:\Users\{}\AppData\Local\Programs\Python\Python310\Lib\site-packages".format(os.getenv('USERNAME')),
    r"C:\Users\{}\AppData\Local\Programs\Python\Python311\Lib\site-packages".format(os.getenv('USERNAME'))
]

for path in python_paths:
    if os.path.exists(path):
        if path not in sys.path:
            sys.path.append(path)
        break

try:
    from bauhaus_circular import quick_analysis
    BAUHAUS_AVAILABLE = True
except ImportError as e:
    BAUHAUS_AVAILABLE = False
    ERROR_MSG = f"Error importando bauhaus_circular: {str(e)}"

def validate_inputs(materials, quantities, climate):
    """Valida y limpia los inputs de Grasshopper."""
    
    # Convertir de Grasshopper trees a listas planas
    if hasattr(materials, '__iter__') and not isinstance(materials, str):
        materials = list(materials)
    else:
        materials = [materials] if materials else []
    
    if hasattr(quantities, '__iter__') and not isinstance(quantities, str):
        quantities = list(quantities)
    else:
        quantities = [quantities] if quantities else []
    
    # Asegurar que quantities tenga la misma longitud que materials
    if len(quantities) < len(materials):
        quantities = quantities + [1.0] * (len(materials) - len(quantities))
    elif len(quantities) > len(materials):
        quantities = quantities[:len(materials)]
    
    # Validar clima
    valid_climates = ['hot', 'temperate', 'cold']
    if climate not in valid_climates:
        climate = 'temperate'
    
    return materials, quantities, climate

# INICIALIZAR OUTPUTS
report = "Esperando datos..."
circular_score = 0.0
carbon_total = 0.0
cost_total = 0.0
recommendations = []
optimized_materials = []

# PROCESAR SI HAY DATOS Y RUN ES TRUE
if run and materials and quantities:
    
    if not BAUHAUS_AVAILABLE:
        report = f"❌ ERROR: No se pudo importar bauhaus_circular\n\nRutas probadas:\n" + "\n
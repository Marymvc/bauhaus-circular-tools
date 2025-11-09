"""
Ejemplo completo de uso de Bauhaus Circular
Muestra todas las funcionalidades principales

Autora: Mary Magali Villca Cruz
Email: arqmaryvillca@gmail.com
"""

from bauhaus_circular import MaterialAnalyzer, CarbonCalculator, DesignOptimizer, ClimateAnalyzer

def ejemplo_completo():
    """Ejemplo completo que muestra todas las capacidades."""
    
    print("=" * 70)
    print("🏛️  BAUHAUS CIRCULAR - EJEMPLO COMPLETO")
    print("=" * 70)
    
    # 1. ANÁLISIS DE MATERIALES
    print("\n1. 📊 ANÁLISIS DE MATERIALES")
    print("-" * 40)
    
    analyzer = MaterialAnalyzer()
    materiales = ['wood', 'glass', 'recycled_steel', 'low_carbon_concrete']
    cantidades = [45.0, 12.0, 28.0, 35.0]
    
    resultado_materiales = analyzer.analyze_materials(materiales)
    
    print(f"📦 Materiales analizados: {', '.join(materiales)}")
    print(f"♻️  Score circularidad: {resultado_materiales['circular_score']:.1f}%")
    print(f"🏛️  Compliant Bauhaus: {'✅' if resultado_materiales['bauhaus_compliant'] else '❌'}")
    
    # Alternativas para concreto bajo carbono
    alternativas = analyzer.suggest_alternatives('low_carbon_concrete')
    if alternativas:
        print(f"\n🔄 Alternativas para 'low_carbon_concrete':")
        for alt in alternativas[:2]:
            print(f"   • {alt['name']}: +{alt['circular_score']:.1f}% circularidad")
    
    # 2. CÁLCULO DE CARBONO
    print("\n2. 🌱 CÁLCULO DE HUELLA DE CARBONO")
    print("-" * 40)
    
    calculator = CarbonCalculator()
    resultado_carbono = calculator.calculate_embodied_carbon(
        dict(zip(materiales, cantidades))
    )
    
    print(f"📊 Carbono total: {resultado_carbono['total_carbon']:,.0f} kgCO₂e")
    print(f"📉 Ahorro vs convencional: {resultado_carbono['carbon_savings_percent']:.1f}%")
    print(f"🏆 Desempeño: {resultado_carbono['performance_rating']}")
    
    # Comparación de materiales
    comparacion = calculator.compare_materials('wood', 'low_carbon_concrete', 10.0)
    print(f"\n🔍 Comparación (10 m³):")
    print(f"   • Madera: {comparacion['material_a']['carbon_kg_co2']:.0f} kgCO₂")
    print(f"   • Concreto bajo C: {comparacion['material_b']['carbon_kg_co2']:.0f} kgCO₂")
    print(f"   • Mejor opción: {comparacion['better_choice']}")
    
    # 3. ANÁLISIS CLIMÁTICO
    print("\n3. 🌤️ ANÁLISIS CLIMÁTICO")
    print("-" * 40)
    
    climate_analyzer = ClimateAnalyzer()
    resumen_clima = climate_analyzer.get_climate_summary()
    
    print(f"📍 Zona climática: {resumen_clima['climate_zone']}")
    print(f"☀️  Radiación solar: {resumen_clima['solar_radiation']['global_horizontal_kwh_m2']} kWh/m²")
    print(f"❄️  Grados-día calefacción: {resumen_clima['degree_days']['heating_degree_days']:.0f}")
    print(f"🔥 Grados-día refrigeración: {resumen_clima['degree_days']['cooling_degree_days']:.0f}")
    
    recomendaciones_clima = climate_analyzer.generate_design_recommendations()
    print(f"\n🎯 Estrategia principal: {recomendaciones_clima['primary_strategy']}")
    print(f"🏗️  Materiales recomendados: {', '.join(recomendaciones_clima['materials_priority'])}")
    
    # 4. OPTIMIZACIÓN COMPLETA
    print("\n4. 🎨 OPTIMIZACIÓN DE DISEÑO COMPLETA")
    print("-" * 40)
    
    optimizer = DesignOptimizer(analyzer, calculator)
    resultado_optimizacion = optimizer.optimize_design(
        materiales, cantidades, 'temperate', budget_limit=80000
    )
    
    diseño_actual = resultado_optimizacion['current_design']
    alternativa = resultado_optimizacion['optimized_alternative']
    
    print("📐 DISEÑO ACTUAL:")
    print(f"   • Circularidad: {diseño_actual['circularity_score']:.1f}%")
    print(f"   • Carbono: {diseño_actual['carbon_footprint_kg_co2']:,.0f} kgCO₂")
    print(f"   • Costo: ${diseño_actual['total_cost_usd']:,.0f}")
    print(f"   • Adecuación climática: {diseño_actual['climate_fit_score']}/100")
    
    print("\n🔄 ALTERNATIVA OPTIMIZADA:")
    print(f"   • Materiales: {', '.join(alternativa['materials'])}")
    print(f"   • Circularidad: {alternativa['circularity_score']:.1f}%")
    print(f"   • Mejora circularidad: +{alternativa['improvements']['circularity_improvement']:.1f}%")
    print(f"   • Reducción carbono: {alternativa['improvements']['carbon_reduction_percent']:.1f}%")
    
    # 5. RECOMENDACIONES
    print("\n5. 💡 RECOMENDACIONES PRIORIZADAS")
    print("-" * 40)
    
    for i, rec in enumerate(resultado_optimizacion['recommendations'][:3], 1):
        print(f"{i}. [{rec['type'].upper()}] {rec['title']}")
        print(f"   📝 {rec['description']}")
        print(f"   🎯 {rec['action']}")
        if 'estimated_improvement' in rec:
            print(f"   📈 {rec['estimated_improvement']}")
        print()
    
    # 6. RESUMEN EJECUTIVO
    print("\n6. 📄 RESUMEN EJECUTIVO")
    print("-" * 40)
    print(resultado_optimizacion['summary'])
    
    print("\n" + "=" * 70)
    print("✅ ANÁLISIS COMPLETADO - DISEÑO CIRCULAR OPTIMIZADO")
    print("=" * 70)

def ejemplo_rapido():
    """Ejemplo rápido usando la función quick_analysis."""
    
    print("\n⚡ EJEMPLO RÁPIDO CON quick_analysis")
    print("-" * 40)
    
    from bauhaus_circular import quick_analysis
    
    materiales = ['wood', 'glass']
    cantidades = [30.0, 15.0]
    
    resultado = quick_analysis(materiales, cantidades, 'temperate')
    
    diseño = resultado['current_design']
    print(f"♻️  Circularidad: {diseño['circularity_score']:.1f}%")
    print(f"🌱 Carbono: {diseño['carbon_footprint_kg_co2']:,.0f} kgCO₂")
    print(f"💵 Costo: ${diseño['total_cost_usd']:,.0f}")
    print(f"🏛️  Bauhaus: {'✅' if diseño['bauhaus_compliant'] else '❌'}")
    
    if resultado['recommendations']:
        print(f"💡 Recomendación principal: {resultado['recommendations'][0]['title']}")

if __name__ == "__main__":
    ejemplo_completo()
    ejemplo_rapido()
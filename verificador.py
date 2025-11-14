"""
SISTEMA DE VERIFICACIÓN AUTOMÁTICA DE EJERCICIOS
Ejecuta este archivo para verificar tus soluciones.
"""

import hashlib
import csv
import os

# Palabras encriptadas de la frase secreta (base64 + XOR)
PALABRAS_ENCRIPTADAS = [
    "T3Blbg==",
    "dGhl",
    "cG9k",
    "YmF5",
    "ZG9vcnMs",
    "SGFs"
]

# Clave de encriptación (no modificar)
_KEY = 0x00

def _xor_decode(encoded_str):
    """Decodifica una cadena XOR + base64"""
    import base64
    decoded = base64.b64decode(encoded_str)
    if _KEY == 0x00:
        return decoded.decode('utf-8')
    return ''.join(chr(byte ^ _KEY) for byte in decoded)

def obtener_palabra_secreta(indice):
    """Obtiene la palabra secreta correspondiente al índice si está disponible"""
    if indice < len(PALABRAS_ENCRIPTADAS):
        try:
            return _xor_decode(PALABRAS_ENCRIPTADAS[indice])
        except:
            return "???"
    return "???"

def verificar_ejercicio1():
    """Verifica ejercicio 1: Análisis de números"""
    try:
        from ejercicio1 import analizar_numeros
        
        # Prueba 1
        resultado = analizar_numeros([1, 2, 3, 4, 5, 6])
        if (resultado.get("pares") == [2, 4, 6] and
            resultado.get("impares") == [1, 3, 5] and
            resultado.get("suma_total") == 21 and
            resultado.get("promedio") == 3.5):
            
            # Prueba 2
            resultado2 = analizar_numeros([10, 15, 20, 25])
            if (resultado2.get("pares") == [10, 20] and
                resultado2.get("impares") == [15, 25] and
                resultado2.get("suma_total") == 70 and
                resultado2.get("promedio") == 17.5):
                return True
        return False
    except Exception as e:
        print(f"Error en ejercicio 1: {e}")
        return False

def verificar_ejercicio2():
    """Verifica ejercicio 2: Filtrar nombres"""
    try:
        from ejercicio2 import filtrar_nombres
        
        # Prueba 1
        resultado = filtrar_nombres(["Ana", "Roberto", "Luis", "Maria"], 5)
        if resultado == ["ROBERTO", "MARIA"]:
            # Prueba 2
            resultado2 = filtrar_nombres(["Pedro", "Juan", "Alejandro"], 6)
            if resultado2 == ["ALEJANDRO"]:
                return True
        return False
    except Exception as e:
        print(f"Error en ejercicio 2: {e}")
        return False

def verificar_ejercicio3():
    """Verifica ejercicio 3: Contador de palabras"""
    try:
        from ejercicio3 import contar_palabras
        
        # Prueba 1
        resultado = contar_palabras("Hola mundo hola Python")
        if resultado == {"hola": 2, "mundo": 1, "python": 1}:
            # Prueba 2
            resultado2 = contar_palabras("Python es Python")
            if resultado2 == {"python": 2, "es": 1}:
                return True
        return False
    except Exception as e:
        print(f"Error en ejercicio 3: {e}")
        return False

def verificar_ejercicio4():
    """Verifica ejercicio 4: Procesador de calificaciones"""
    try:
        from ejercicio4 import procesar_calificaciones
        
        # Prueba 1
        resultado = procesar_calificaciones({
            "Ana": [85, 90, 88],
            "Luis": [70, 75, 72],
            "Maria": [95, 92, 98]
        })
        if (round(resultado.get("Ana", 0), 2) == 87.67 and
            round(resultado.get("Luis", 0), 2) == 72.33 and
            round(resultado.get("Maria", 0), 2) == 95.0 and
            resultado.get("mejor_estudiante") == "Maria"):
            return True
        return False
    except Exception as e:
        print(f"Error en ejercicio 4: {e}")
        return False

def verificar_ejercicio5():
    """Verifica ejercicio 5: Manipulador de listas"""
    try:
        from ejercicio5 import manipular_lista
        
        # Prueba 1
        resultado = manipular_lista([5, 15, 8, 23, 12, 30, 7, 18, 25])
        if resultado == [60, 50, 46, 36, 30]:
            # Prueba 2
            resultado2 = manipular_lista([3, 10, 5, 20, 8])
            if resultado2 == [40, 20]:
                return True
        return False
    except Exception as e:
        print(f"Error en ejercicio 5: {e}")
        return False

def verificar_ejercicio6():
    """Verifica ejercicio 6: Generador de reporte CSV"""
    try:
        # Crear archivo de prueba
        with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["producto", "cantidad", "precio"])
            writer.writerow(["Laptop", 5, 15000])
            writer.writerow(["Mouse", 20, 250])
            writer.writerow(["Teclado", 15, 800])
        
        from ejercicio6 import generar_reporte
        
        resultado = generar_reporte()
        if (resultado.get("Laptop") == 75000 and
            resultado.get("Mouse") == 5000 and
            resultado.get("Teclado") == 12000 and
            resultado.get("total_general") == 92000):
            
            # Limpiar archivo de prueba
            if os.path.exists("ventas.csv"):
                os.remove("ventas.csv")
            return True
        
        # Limpiar archivo de prueba en caso de fallo
        if os.path.exists("ventas.csv"):
            os.remove("ventas.csv")
        return False
    except Exception as e:
        print(f"Error en ejercicio 6: {e}")
        if os.path.exists("ventas.csv"):
            os.remove("ventas.csv")
        return False

def main():
    print("=" * 60)
    print("SISTEMA DE VERIFICACIÓN DE EJERCICIOS")
    print("=" * 60)
    print()
    
    ejercicios = [
        ("Ejercicio 1: Análisis de números", verificar_ejercicio1),
        ("Ejercicio 2: Filtrar nombres", verificar_ejercicio2),
        ("Ejercicio 3: Contador de palabras", verificar_ejercicio3),
        ("Ejercicio 4: Procesador de calificaciones", verificar_ejercicio4),
        ("Ejercicio 5: Manipulador de listas", verificar_ejercicio5),
        ("Ejercicio 6: Generador de reporte CSV", verificar_ejercicio6)
    ]
    
    resultados = []
    frase_revelada = []
    
    for i, (nombre, verificador) in enumerate(ejercicios):
        try:
            aprobado = verificador()
            resultados.append(aprobado)
            
            if aprobado:
                print(f"✓ {nombre}: APROBADO")
                # Obtener palabra secreta hasheada
                frase_revelada.append(obtener_palabra_secreta(i))
            else:
                print(f"✗ {nombre}: FALLIDO")
                frase_revelada.append("???")
        except Exception as e:
            print(f"✗ {nombre}: ERROR - {e}")
            resultados.append(False)
            frase_revelada.append("???")
    
    print()
    print("=" * 60)
    total_aprobados = sum(resultados)
    print(f"RESULTADO: {total_aprobados}/6 ejercicios aprobados")
    print("=" * 60)
    print()
    
    # Revelar frase secreta
    print("FRASE SECRETA:")
    print(" ".join(frase_revelada))
    print()
    
    if total_aprobados == 6:
        print("🎉 ¡Felicidades! Has completado todos los ejercicios.")
        print("Has desbloqueado la frase secreta completa.")
    elif total_aprobados >= 4:
        print("¡Buen trabajo! Estás cerca de completar todos los ejercicios.")
    elif total_aprobados >= 2:
        print("Vas por buen camino. Revisa los ejercicios fallidos.")
    else:
        print("Sigue intentando. Revisa los conceptos de la clase.")

if __name__ == "__main__":
    main()
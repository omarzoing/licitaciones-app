"""
Generador de datos realistas para empresas constructoras en Guadalajara, Jalisco
"""

import random
import string
from datetime import datetime

class EmpresaGenerator:
    """Genera datos ficticios pero realistas de empresas constructoras"""
    
    # Palabras para nombres de constructoras
    PREFIJOS = [
        "Constructora", "Edificaciones", "Desarrollos", "Proyectos",
        "Construcciones", "Grupo", "Ingeniería", "Obras"
    ]
    
    NOMBRES = [
        "Atlas", "Minerva", "Coloso", "Omega", "Delta", "Sigma",
        "Horizon", "Summit", "Vertex", "Apex", "Zenith", "Prime",
        "Nova", "Stellar", "Cosmos", "Orion", "Phoenix", "Titan",
        "Imperial", "Royal", "Elite", "Premier", "Superior", "Master",
        "Continental", "Universal", "Global", "Metropolitan", "Urban"
    ]
    
    SUFIJOS = [
        "y Asociados", "del Bajío", "de Occidente", "Tapatía",
        "Jalisco", "GDL", "del Pacífico", "Occidental"
    ]
    
    # Calles reales de Guadalajara
    CALLES = [
        "Av. López Mateos", "Av. Américas", "Av. Patria", "Av. Vallarta",
        "Av. Circunvalación", "Av. Inglaterra", "Av. Niños Héroes",
        "Av. Federalismo", "Av. Alcalde", "Calzada Independencia",
        "Av. Mariano Otero", "Av. Lázaro Cárdenas", "Av. Chapultepec",
        "Av. Rubén Darío", "Av. Washington"
    ]
    
    # Colonias reales de Guadalajara
    COLONIAS = [
        "Providencia", "Chapalita", "Americana", "Lafayette",
        "Jardines del Bosque", "Ciudad del Sol", "Jardines de la Patria",
        "Lomas de Guevara", "Monraz", "Circunvalación Américas",
        "Santa Teresita", "Jardines Vallarta", "Arcos Vallarta",
        "Seattle", "Prados Providencia", "Balcones del Sol"
    ]
    
    @staticmethod
    def generar_nombre_empresa():
        """Genera un nombre profesional de constructora"""
        tipo = random.randint(1, 4)
        
        if tipo == 1:
            # Tipo: Constructora + Nombre
            return f"{random.choice(EmpresaGenerator.PREFIJOS)} {random.choice(EmpresaGenerator.NOMBRES)}"
        elif tipo == 2:
            # Tipo: Nombre + Sufijo
            return f"{random.choice(EmpresaGenerator.NOMBRES)} {random.choice(EmpresaGenerator.SUFIJOS)}"
        elif tipo == 3:
            # Tipo: Prefijo + Nombre + Sufijo
            return f"{random.choice(EmpresaGenerator.PREFIJOS)} {random.choice(EmpresaGenerator.NOMBRES)} {random.choice(EmpresaGenerator.SUFIJOS)}"
        else:
            # Tipo: Solo nombre
            return random.choice(EmpresaGenerator.NOMBRES)
    
    @staticmethod
    def generar_direccion():
        """Genera una dirección realista en Guadalajara"""
        calle = random.choice(EmpresaGenerator.CALLES)
        numero = random.randint(100, 9999)
        letra = random.choice(['', '-A', '-B', ' Local 1', ' Local 2', ' Piso 2'])
        colonia = random.choice(EmpresaGenerator.COLONIAS)
        cp = random.randint(44100, 44990)
        
        return {
            'calle': f"{calle} {numero}{letra}",
            'colonia': colonia,
            'cp': cp,
            'ciudad': 'Zapopan, Jalisco' if random.random() > 0.5 else 'Guadalajara, Jalisco',
            'completa': f"{calle} {numero}{letra}, {colonia}, C.P. {cp}"
        }
    
    @staticmethod
    def generar_telefono():
        """Genera un teléfono con formato de Guadalajara (33)"""
        # Formato: 33-XXXX-XXXX
        parte1 = random.randint(1000, 9999)
        parte2 = random.randint(1000, 9999)
        return f"33-{parte1}-{parte2}"
    
    @staticmethod
    def generar_email(nombre_empresa):
        """Genera un email corporativo basado en el nombre de la empresa"""
        # Limpiar nombre de empresa
        nombre_limpio = nombre_empresa.lower()
        nombre_limpio = nombre_limpio.replace('constructora', '').replace('construcciones', '')
        nombre_limpio = nombre_limpio.replace('edificaciones', '').replace('desarrollos', '')
        nombre_limpio = nombre_limpio.replace('proyectos', '').replace('grupo', '')
        nombre_limpio = nombre_limpio.replace('ingeniería', '').replace('obras', '')
        nombre_limpio = nombre_limpio.replace('y asociados', '').replace('del bajío', '')
        nombre_limpio = nombre_limpio.replace('de occidente', '').replace('tapatía', '')
        nombre_limpio = nombre_limpio.replace('del pacífico', '').replace('occidental', '')
        nombre_limpio = nombre_limpio.strip().replace(' ', '')
        
        # Eliminar acentos
        nombre_limpio = nombre_limpio.replace('á', 'a').replace('é', 'e').replace('í', 'i')
        nombre_limpio = nombre_limpio.replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')
        
        dominios = [
            'contacto', 'info', 'ventas', 'proyectos', 'cotizaciones'
        ]
        
        usuario = random.choice(dominios)
        return f"{usuario}@{nombre_limpio}.com.mx"
    
    @staticmethod
    def generar_rfc(nombre_empresa, año_fundacion):
        """Genera un RFC con formato mexicano válido"""
        # Tomar primeras 3-4 letras del nombre
        nombre_limpio = nombre_empresa.upper()
        nombre_limpio = nombre_limpio.replace('CONSTRUCTORA', '').replace('CONSTRUCCIONES', '')
        nombre_limpio = nombre_limpio.replace('EDIFICACIONES', '').replace('DESARROLLOS', '')
        nombre_limpio = nombre_limpio.strip()
        
        # Obtener iniciales (3 o 4 letras)
        palabras = nombre_limpio.split()
        if len(palabras) >= 2:
            iniciales = palabras[0][:2] + palabras[1][0]
        else:
            iniciales = palabras[0][:3]
        
        iniciales = iniciales[:4].ljust(3, 'X')
        
        # Fecha: AAMMDD
        año = str(año_fundacion)[2:]  # Últimos 2 dígitos
        mes = f"{random.randint(1, 12):02d}"
        dia = f"{random.randint(1, 28):02d}"
        
        # Homoclave: 3 caracteres alfanuméricos
        homoclave = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        
        return f"{iniciales}{año}{mes}{dia}{homoclave}"
    
    @staticmethod
    def generar_año_fundacion():
        """Genera un año de fundación entre 2000 y 2019"""
        return random.randint(2000, 2019)
    
    @staticmethod
    def generar_empresa_completa():
        """Genera todos los datos de una empresa constructora"""
        nombre = EmpresaGenerator.generar_nombre_empresa()
        año = EmpresaGenerator.generar_año_fundacion()
        direccion = EmpresaGenerator.generar_direccion()
        
        return {
            'nombre': nombre,
            'nombre_completo': f"{nombre} S.A. de C.V.",
            'direccion': direccion,
            'telefono': EmpresaGenerator.generar_telefono(),
            'email': EmpresaGenerator.generar_email(nombre),
            'rfc': EmpresaGenerator.generar_rfc(nombre, año),
            'año_fundacion': año
        }


if __name__ == "__main__":
    # Prueba del generador
    print("=== PRUEBA DE GENERADOR DE EMPRESAS ===\n")
    for i in range(5):
        empresa = EmpresaGenerator.generar_empresa_completa()
        print(f"Empresa {i+1}:")
        print(f"  Nombre: {empresa['nombre_completo']}")
        print(f"  Dirección: {empresa['direccion']['completa']}")
        print(f"  Ciudad: {empresa['direccion']['ciudad']}")
        print(f"  Teléfono: {empresa['telefono']}")
        print(f"  Email: {empresa['email']}")
        print(f"  RFC: {empresa['rfc']}")
        print(f"  Año: {empresa['año_fundacion']}")
        print()

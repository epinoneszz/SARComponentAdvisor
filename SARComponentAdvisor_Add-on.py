#Información que se muestra en el menu de preferencias del Add-on
bl_info = {
    "name": "SAR Component Advisor",
    "author": "Valentina Apablaza Murúa <valentina.apablaza@usm.cl>",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "category": "Mesh",
    "location": "View3D > UI",
    "description": "It is a parametric tool to suppor decision making when planing the installation of a SAR system.",
    "warning": "In development",
    "doc_url": "",
    "tracker_url": "",
}

####Inicialmente se importan bibliotecas necesarias
import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty

############################################## LISTA DE COMPONENTES #################################################

Espacio_diseño = [['Sync speed', 0.5, 1.0],
                  ['Brightness', 0.5, 2.0],
                  ['Sharpness', 0.4, 2.0],
                  ['Number of people', 0.8, 2.0],
                  ['Proximity of the projector',0.3,1.0],
                  ['Movement of the mixed prototype', 0.2, 2.0],
                  ['Interaction with the digital model',0.0,1.0],
                  ['Augmented object placement',0.5,1.0]]

Espacio_diseño_act = [['Sync speed', 0.5, 1.0],
                  ['Brightness', 0.5, 2.0],
                  ['Sharpness', 0.4, 2.0],
                  ['Number of people', 0.8, 2.0],
                  ['Proximity of the projector',0.3,1.0],
                  ['Movement of the mixed prototype', 0.2, 2.0],
                  ['Interaction with the digital model',0.0,1.0],
                  ['Augmented object placement',0.5,1.0]]

veloc_sinc = ['Projector technology',0.5,1.0]

Brightness = ['Projector brightness',0.2,0.4,0.6,0.8,1.0]

Sharpness = ['Projector resolution',0.2,0.3,0.5,0.7,0.8,1.0]

proximidad_p =['Projector position',0.3,0.7,1.0]

cant_p = [['Viewing angle',0.5,1.0],['Number of projectors',0.3,0.5,0.8,1.0]]

mov_pm = ['Tracking type',0.2,0.3,0.5,0.7,0.8,1.0]

imd =['Type of interactive device',0.0,1.0]

variedad_conf =['Number of configurations in space',0.0,1.0]

veloc_sinc_def =['']

Brightness_def = ['']

Sharpness_def = ['']

proximidad_p_def = ['']

cant_p_def = ['','']

mov_pm_def = ['','']

imd_def = ['']

variedad_conf_def = ['']

diseño_final = ['','','','','','','','','','']

tipos_tiros = []

angulo = ['']

vertice_1 = []

ubic_proyector = []

tiro =[]

pos_pm =[]

lumens_fin = []


propuesta_final = []

propuesta_final_2 = []

propuesta_final_3 = []


# Lista para guardar las colecciones ocultas y su estado original
colecciones_ocultas = []

#INFORMACIÓN SOBRE PROYECTORES
#- Nueva base de datos

# Forma general previa: [MODELO, MARCA, TECNOLOGÍA, RESOLUCIÓN,LUMENS,THROW DISTANCE,THROW RATIO,ZOOM,TIPO TIRO,FUENTE DE LUZ,VIDA UTIL,VELOCIDAD SINCRONIZACION,PRECIO DOLAR, PRECIO CLP,TIPO TECNOLOGÍA,CATEGORÍA LUMENS,RESOLUCIÓN]

# Nueva forma general: [MODELO, MARCA, TECNOLOGÍA, RESOLUCIÓN,LUMENS,NITS,TIPO HABITACIÓN,THROW RATIO,TIPO TIRO,FUENTE DE LUZ,VIDA UTIL,VELOCIDAD SINCRONIZACION,PRECIO DOLAR, PRECIO CLP,- TIPO TECNOLOGÍA,CATEGORÍA NITS,-RESOLUCIÓN]

Proyector_1 = ["Epson Home Cinema 5050UB (Telephoto)","Epson","3LCD de Epson","4K (1,920x1,080 x2)",2600,"300-600 Nits","Bright room", 2.84, "Long Throw","Lampara",4000,60,3390.66,2732872,'LCD technology','4K Ultra HD']
Proyector_2 = ["Epson Home Cinema 5050UB (Wide Angle)","Epson","3LCD de Epson","4K (1,920x1,080 x2)",2600,"300-600 Nits","Bright room", 1.35,"Long Throw","Lampara",4000,60,3390.66,2732872,'LCD technology','4K Ultra HD']
Proyector_3 = ["Epson Home Cinema LS11000 (Telephoto)","Epson","3LCD de Epson","4K (1080p x 4)",2500,"300-600 Nits","Bright room",2.84,"Long Throw","Laser",20000,120,3999.99,3223992,'LCD technology','4K Ultra HD']
Proyector_4 = ["Epson Home Cinema LS11000 (Wide Angle)","Epson","3LCD de Epson","4K (1080p x 4)",2500,"300-600 Nits","Bright room",1.35,"Long Throw","Laser",20000,120,3999.99,3223992,'LCD technology','4K Ultra HD']
Proyector_5 = ["Sony VPL-VW325ES (Telephoto)","Sony","LCoS (SXRD)","4096x2.160",1500,'200 Nits',"Lit room",2.83,"Long Throw","Lampara",6000,"50/60",4999,4029194,'LCD technology','4K Ultra HD']
Proyector_6 = ["Sony VPL-VW325ES (Wide Angle)","Sony","LCoS (SXRD)","4096x2,160",1500,'200 Nits',"Lit room",1.38,"Long Throw","Lampara",6000,"50/60",4999, 4029194,'LCD technology','4K Ultra HD']
Proyector_7 = ["Optoma UHZ50 (Telephoto)","Optoma","DLP","3840x2160",3000,"+ 600 Nits","Outdoors",1.59,"Long Throw","Laser",	30000,"240",2798.00,2255188,'DLP technology','4K Ultra HD']
Proyector_8 = ["Optoma UHZ50 (Wide Angle)","Optoma","DLP","3840x2160",3000,"+ 600 Nits","Outdoors",1.21,"Long Throw","Laser",30000,"240",2798.00,2255188,'DLP technology','4K Ultra HD'] 
Proyector_9 = ["Optoma UHD35 (Telephoto)","Optoma","DLP","3840x2160",3600,"+ 600 Nits","Outdoors",1.66,"Long Throw","Lampara",10000,	240,789.75,636539,'DLP technology','4K Ultra HD']
Proyector_10 =["Optoma UHD35 (Wide Angle)","Optoma","DLP","3840x2160",3600,"+ 600 Nits",	"Outdoors",	1.50,"Long Throw","Lampara",10000,240,789.75,636.539,'DLP technology','4K Ultra HD']
Proyector_11 = ["BenQ HT3550i (Telephoto)",	"BenQ","DLP","3840x2160",2000,"300-600 Nits","Bright room",1.47,"Long Throw",	"Lampara",4000,	60,1799.00, 1449994,'DLP technology','4K Ultra HD']
Proyector_12 = ["BenQ HT3550i (Wide Angle)","BenQ","DLP","3840x2160",2000,"300-600 Nits","Bright room",1.13,"Long Throw",	"Lampara",4000,	60,1799.00, 1449994,'DLP technology','4K Ultra HD']
Proyector_13 = ["Anker Nebula Cosmos Laser 4K","Anker","DLP","3840x2160",1840,'100 Nits',"Dim room",1.27,"Long Throw","Laser",	25000,60,1999.99,1611992,'DLP technology','4K Ultra HD']
Proyector_14 = ["LG CineBeam HU810PW (Telephoto)","LG","DLP","3840x2160",2700,"300-600 Nits","Bright room",2.08,"Long Throw",	"Laser",30000,"50/60",2100.99, 1693398,'DLP technology','4K Ultra HD']
Proyector_15 = ["LG CineBeam HU810PW (Wide Angle)","LG","DLP","3840x2160",2700,"300-600 Nits","Bright room",1.30,"Long Throw",	"Laser",30000,"50/60",2100.99, 1693398,'DLP technology','4K Ultra HD']
Proyector_16 = ["Epson Home Cinema 2250 (Telephoto)","Epson","LCD",	"1920x1080",2700,"300-600 Nits","Bright room",2.17,"Long Throw","Lampara",4500,50/60,1298.00, 1046188,'LCD technology','Full HD (1080p)']
Proyector_17 = ["Epson Home Cinema 2250 (Wide Angle)", "Epson","LCD",	"1920x1080",2700,"300-600 Nits","Bright room",1.34,"Long Throw","Lampara",4500,50/60,1298.00, 1046188,'LCD technology','Full HD (1080p)']
Proyector_18 = ["Epson Home Cinema 2350 4K (Telephoto)","Epson","3LCD de Epson","3840x2160",2800,"+ 600 Nits","Outdoors",2.17,	"Long Throw","Lampara",4500,120,1299.99, 1799989,'LCD technology','4K Ultra HD']
Proyector_19 = ["Epson Home Cinema 2350 4K (Wide Angle)","Epson","3LCD de Epson","3840x2160",2800,"+ 600 Nits","Outdoors",1.34,	"Long Throw","Lampara",4500,120,1299.99, 1799989,'LCD technology','4K Ultra HD']
Proyector_20 = ["BenQ HT2050A (Telephoto)","BenQ","DLP","1920x1080",2200,"300-600 Nits","Bright room",1.50,"Long Throw",	"Lampara",7000,60,749.00,603694,'DLP technology','Full HD (1080p)']
Proyector_21 = ["BenQ HT2050A (Wide Angle)","BenQ","DLP","1920x1080",2200,"300-600 Nits","Bright room",1.15,"Long Throw",	"Lampara",7000,60,749.00,603694,'DLP technology','Full HD (1080p)']
Proyector_22 = ["BenQ HT2060 (Telephoto)","BenQ","DLP","1920x1080",2300,"300-600 Nits","Bright room",1.50,"Long Throw","LED",	30000,120,999.00, 805194,'DLP technology','Full HD (1080p)']
Proyector_23 = ["BenQ HT2060 (Wide Angle)","BenQ","DLP","1920x1080",2300,"300-600 Nits","Bright room",1.15,"Long Throw","LED",	30000,120,999.00, 805194,'DLP technology','Full HD (1080p)']
Proyector_24 = ["AAXA P8 Portable",	"AAXA",	"DLP","960x540",225,'50 Nits',"Dark room",1.20,"Long Throw","LED",30000,60,249.00, 200694,'DLP technology','Full HD (1080p)']
Proyector_25 = ["Anker Nebula Mars II Pro","Anker","DLP","1280x720",500,'100 Nits',"Dim room",1.45,"Long Throw","LED",30000,60,550.00, 699990,'DLP technology','WXGA']
Proyector_26 = ["Epson EpiqVision Mini EF12","Epson","3LCD de Epson","1920x1080",1000,'200 Nits',"Lit room",1.00,"Long Throw",	"Laser",20000,240,999.99, 805992,'LCD technology','Full HD (1080p)']
Proyector_27 = ["Xgimi Halo Plus","Xgimi","DLP","1920x1080",900,'100 Nits',"Dim room",1.20,"Long Throw","LED",25000,"50/60", 849.00, 684294,'DLP technology','Full HD (1080p)']
Proyector_28 = ["Vimgo P10","Vimgo","LCD","1920x1,080",300,'50 Nits',"Dark room",1.25,"Long Throw","LED",30000,60,139.99,112832,'LCD technology','Full HD (1080p)']
Proyector_29 = ["BenQ GS50","BenQ","DLP","1920x1,080",500,'100 Nits',"Dim room",1.21,"Long Throw","LED",30000,60,799.00,643994,'DLP technology','Full HD (1080p)']
Proyector_30 = ["Samsung Freestyle","Samsung","DLP","1920 x 1080",550,'100 Nits',"Dim room",1.22,"Long Throw","LED",20000,	"50/60", 799.99, 644792,'DLP technology','Full HD (1080p)']
Proyector_31 = ["Xiaomi Mi Smart Projector 2","Xiaomi",	"DLP","1920 x 1080",500,'100 Nits',"Dim room",	1.20,"Long Throw","LED",	30000,60,992.55, 799999,'DLP technology','Full HD (1080p)'] 
Proyector_32 = ["Epson Home Cinema 880","Epson","3LCD de Epson","1920x1080",3300,"+ 600 Nits","Outdoors",1.21,"Long Throw",	"Lampara",12000,"50/60", 857.06, 690794,'LCD technology','Full HD (1080p)']
Proyector_33 = ["Anker Nebula Solar Portable","Anker","DLP","1920x1080",400,'100 Nits',"Dim room",	1.20,"Long Throw","LED",	30000,60,499.99, 402992,'DLP technology','Full HD (1080p)'] 
Proyector_34 = ["Epson Home Cinema 4010 (Telephoto)","Epson","3LCD de Epson","4K(1920 x 1080 x 2)",2400,"300-600 Nits","Bright room",2.84,"Long Throw","Lampara",5000,"50/60", 1799.99, 1450792,'LCD technology','4K Ultra HD']
Proyector_35 = ["Epson Home Cinema 4010 (Wide Angle)","Epson","3LCD de Epson","4K(1920 x 1080 x 2)",2400,"300-600 Nits","Bright room",1.35,"Long Throw","Lampara",5000,"50/60", 1799.99, 1450792,'LCD technology','4K Ultra HD']
Proyector_36 = ["Epson Home Cinema 3800 (Telephoto)","Epson","3LCD de Epson","4K(1920 x 1080 x 2)",3000,"+ 600 Nits",	"Outdoors",2.15,"Long Throw","Lampara", 5000,	"50/60", 1699.99, 1370192,'LCD technology','4K Ultra HD']
Proyector_37 = ["Epson Home Cinema 3800 (Wide Angle)","Epson","3LCD de Epson","4K(1920 x 1080 x 2)",3000,"+ 600 Nits",	"Outdoors",1.32,"Long Throw","Lampara", 5000,	"50/60", 1699.99, 1370192,'LCD technology','4K Ultra HD']
Proyector_38 = ["BenQ HT5550 (Telephoto)","BenQ","DLP",	"4K UHD (3840x2160)",1800,'200 Nits',"Lit room",2.18,"Long Throw",	"Lampara",15000,"50/60", 2699.00, 2175394,'DLP technology','4K Ultra HD']
Proyector_39 = ["BenQ HT5550 (Wide Angle)","BenQ","DLP","4K UHD (3840x2160)",1800,'200 Nits',"Lit room",1.36,"Long Throw",	"Lampara",15000,"50/60", 2699.00, 2175394,'DLP technology','4K Ultra HD']
Proyector_40 = ["BenQ HT2150ST (Telephoto)","BenQ","DLP","1920x1080",2200,"300-600 Nits","Bright room",0.83,"Short throw",	"Lampara", 7000,"50/60", 899.00, 724594,'DLP technology','Full HD (1080p)']
Proyector_41 = ["BenQ HT2150ST (Wide Angle)","BenQ","DLP","1920x1080",2200,"300-600 Nits","Bright room",0.69,"Short throw",	"Lampara", 7000,"50/60", 899.00, 724594,'DLP technology','Full HD (1080p)']
Proyector_42 = ["Epson EF-100B Projector","Epson","3LCD de Epson","1280 x 800",2000,"300-600 Nits","Bright room",1.06,"Long Throw","Laser",20000,"50/60", 1178.65, 949990.00,'LCD technology','WXGA']
Proyector_43 = ["BenQ MX536 (Telephoto)","BenQ","DLP","1024x768",4000,"+ 600 Nits","Outdoors",2.33,"Long Throw","Lampara",	20000,"50/60", 528.94, 426325.64,'DLP technology','XGA']
Proyector_44 = ["BenQ MX536 (Wide Angle)","BenQ","DLP","1024x768",4000,"+ 600 Nits","Outdoors",1.94,"Long Throw","Lampara",	20000,"50/60", 528.94, 426325.64,'DLP technology','XGA']
Proyector_45 = ["BenQ MX631ST (Telephoto)","BenQ","DLP","1024x768",3200,"+ 600 Nits","Outdoors",1.08,"Short throw","Lampara", 	10000,"50/60",907.56, 731490,'DLP technology','XGA'] 
Proyector_46 = ["BenQ MX631ST (Wide Angle)","BenQ","DLP","1024x768",3200,"+ 600 Nits","Outdoors",0.90,"Short throw","Lampara", 	10000,"50/60",907.56, 731490,'DLP technology','XGA'] 
Proyector_47 = ["BenQ LH820ST","BenQ",	"DLP","1920 x 1080",3600,"+ 600 Nits","Outdoors",0.50,"Short throw","Laser",30000,60,	1899.00,1530594,'DLP technology','Full HD (1080p)'] 
Proyector_48 = ["Epson EpiqVision Ultra LS800B","Epson","3LCD de Epson","3840x2160",4000,"+ 600 Nits","Outdoors",0.16,"Ultra short throw","Laser",20000,60,3499.00,2820194,'LCD technology','4K Ultra HD']
Proyector_49 = ["BenQ V7050i","BenQ","DLP","3840x2160",2500,"300-600 Nits","Bright room",0.23,"Ultra short throw","Laser",2000,60,2849.00,2296294,'DLP technology','4K Ultra HD']
Proyector_50 = ["Samsung Premiere LSP9T","Samsung","DLP","3840x2160",2800,"300-600 Nits","Bright room",0.19,"Ultra short throw",	"Laser",20000,60,6164.00,4968184,'DLP technology','4K Ultra HD']
Proyector_51 = ["PA503S (Telephoto)","ViewSonic","DLP","800x600",3800,"+ 600 Nits","Outdoors",2.15,"Long Throw","Lampara", 	15000,	"50/60",387.90, 312647.40,'DLP technology','SVGA']
Proyector_52 = ["PA503S (Wide Angle)","ViewSonic","DLP","800x600",3800,"+ 600 Nits","Outdoors",1.96,"Long Throw","Lampara", 	15000,	"50/60",387.90, 312647.40,'DLP technology','SVGA']
Proyector_53 = ["Epson PowerLite L630U (Telephoto)","Epson","3LCD de Epson","1920x1200",6200,"+ 600 Nits","Outdoors",2.20,"Long Throw","Laser",20000,"50/60",4799.98,4091250,'LCD technology','WUXGA']
Proyector_54 = ["Epson PowerLite L630U (Wide Angle)","Epson","3LCD de Epson","1920x1200",6200,"+ 600 Nits","Outdoors",1.35,"Long Throw","Laser",20000,"50/60",4799.98,4091250,'LCD technology','WUXGA']


#INFORMACIÓN SOBRE SISTEMAS DE TRACKING

sist_t_0 = ["Facial Markers - 3 mm(50 Units)",110.00,88660, "Markers"]
sist_t_1 = ["V120:Duo",2999.00, 2417194,'All-in-one system']
sist_t_2 = ["V120:Trio", 3999.00, 3223194,'All-in-one system']
sist_t_3 = ["Cámara Flex 3 (4 Units)",5117.00,4124302,'Multi - camera system']
sist_t_4 = ["Cámara Flex 13 (4 Units)",6877.00,5542862,'Multi - camera system']
sist_t_5 = ["Cámara Primex 13 (4 Units)",12263.00,9883978,'Multi - camera system']
sist_t_6 = ["Cámara Primex 22 (4 Units)",18884.00,15220504,'Multi - camera system']


#INFORMACIÓN SOBRE PANTALLAS TÁCTILES

tactil_1 = ["IPAD APPLE 7GEN ORO (10.2 pulg, 32 GB, WIFI)", 457.55, 389990]
tactil_2 = ["Tablet Samsung Galaxy Tab S6 Lite de 10.4 pulg",506.86, 432020]


############################################## LISTA DE FUNCIONES #################################################

### Eliminar las lista del texto -------------------------------------------------------------------------------------------------

def eliminar_lista_por_texto(lista, texto_a_buscar):
    for sublista in lista:
        if sublista[0] == texto_a_buscar:
            lista.remove(sublista)

### Duplicar colecciones  -------------------------------------------------------------------------------------------------

def duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino):
    # Obtener la referencia a la colección original
    coleccion_original = bpy.data.collections.get(nombre_coleccion_original)

    # Verificar que la colección original exista
    if coleccion_original is None:
        print("Error: The original collection doesn't exist")
        return

    # Crear una nueva colección y asignarle los objetos de la colección original
    coleccion_duplicada = bpy.data.collections.new(nombre_coleccion_destino)
    for objeto in coleccion_original.objects:
        coleccion_duplicada.objects.link(objeto.copy())

    # Agregar la colección duplicada a la escena
    bpy.context.scene.collection.children.link(coleccion_duplicada)

### Ocultar colecciones  ---------------------------------------------------------------------------------------------------------

def ocultar_coleccion(nombre_coleccion):
    # Obtener la referencia a la colección
    coleccion = bpy.data.collections.get(nombre_coleccion)

    # Verificar que la colección exista
    if coleccion is None:
        print("Error: The collection does not exist.")
        return

    # Ocultar la colección
    coleccion.hide_viewport = True

### Reposición de un objeto de la colección  ------------------------------------------------------------------------------------

def reposicionar_objeto(nombre_objeto, nueva_posicion):
    # Obtener la referencia al objeto
    objeto = bpy.data.objects.get(nombre_objeto)

    # Verificar que el objeto exista
    if objeto is None:
        print(f"Error: The object '{nombre_objeto}' does not exist.")
        return

    # Cambiar la posición del objeto
    objeto.location = nueva_posicion

### Eliminar una colección -------------------------------------------------------------------------------------------------------

def eliminar_coleccion(nombre_coleccion):
    # Obtener la referencia a la colección
    coleccion = bpy.data.collections.get(nombre_coleccion)

    # Verificar que la colección exista
    if coleccion is None:
        #print(f"Error: La colección '{nombre_coleccion}' no existe.")
        return

    # Remover la colección de la escena
    bpy.context.scene.collection.children.unlink(coleccion)

    # Eliminar definitivamente la colección
    bpy.data.collections.remove(coleccion)


############################################## LISTA DE OPERADORES #################################################

#Operador para generar el soporte del PM --------------------------------------------------------------------------------------

class CreateTableOperator(bpy.types.Operator):
    bl_idname = "object.create_table"
    bl_label = "Generate support"
    bl_description = "A support for the mixed prototype is generated"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Crear el primer cilindro
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.75)
        obj1 = bpy.context.object

        # Crear el segundo cilindro
        bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=0.1)
        obj2 = bpy.context.object

        # Posicionar los cilindros
        obj1.location.z = 0.375
        obj2.location.z = 0.825

        return {'FINISHED'}


### OPERADOR PARA CREAR LA SALA CON SUS DIMENSIONES PERSONALIZADAS ------------------------------------------------------------

class CreateCubeOperator(bpy.types.Operator):
    bl_idname = "object.create_cube"
    bl_label = "Enter the dimensions of the space:"
    bl_description = "Enter the dimensions of the space in meters where the mixed prototyping system will be installed"
    bl_options = {'REGISTER', 'UNDO'}

    length: bpy.props.FloatProperty(
        name="Length [m]",
        description="Room length [m]",
        default=3,
        min=2,
        soft_max=20
    )

    width: bpy.props.FloatProperty(
        name="Width [m]",
        description="Room width [m]",
        default=3,
        min=2,
        soft_max=20
    )

    height: bpy.props.FloatProperty(
        name="Height [m]",
        description="Room height [m]",
        default=2,
        min=2,
        soft_max=5
    )
    # Agregamos un atributo de clase para guardar las dimensiones del objeto creado
    created_dimensionsCube = None

    def execute(self, context):
        # Convertir las dimensiones a metros
        length_m = self.length
        width_m = self.width
        height_m = self.height

        # Buscar si el objeto "Cube" ya existe en la colección de objetos de Blender
        cube_obj = bpy.data.objects.get("Cube")

        if cube_obj:
            # Modificar las dimensiones del Cube existente actualizando los vértices
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)


            # Acceder a las coordenadas de vértices y actualizarlas utilizando foreach_set()
            num_vertices = len(vertices)
            mesh = cube_obj.data
            mesh.vertices.foreach_set("co", [v for vert in vertices for v in vert])

        else:
            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

        # Guardamos las dimensiones del objeto creado en el atributo de clase
        CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)

        #Limpiar tipos_tiros
        tipos_tiros.clear()
        

        #Modificar lista tipos_tiros
        if (length_m/2) <= 1:
            if width_m/2 <= 1:
                tipos_tiros.append("Ultra short throw type")
    
            elif (width_m/2) <= 2:
                tipos_tiros.append("Ultra short throw type")
                tipos_tiros.append("Short throw type")
            else:
                tipos_tiros.append("Ultra short throw type")
                tipos_tiros.append("Short throw type")
                tipos_tiros.append("Long throw type")

        elif (length_m/2) <= 2:
            if width_m/2 <=2:
                tipos_tiros.append("Ultra short throw type")
                tipos_tiros.append("Short throw type")
            else:
                tipos_tiros.append("Ultra short throw type")
                tipos_tiros.append("Short throw type")
                tipos_tiros.append("Long throw type")

        else:
            tipos_tiros.append("Ultra short throw type")
            tipos_tiros.append("Short throw type")
            tipos_tiros.append("Long throw type")

        return {'FINISHED'}

### OPERADOR PARA CREAR EL PM CON SUS DIMENSIONES PERSONALIZADAS --------------------------------------------------------------

class OBJECT_OT_create_parallelepiped(bpy.types.Operator):
    bl_idname = "object.create_parallelepiped"
    bl_label = "Enter the dimensions of the interactive area"
    bl_description = "Enter the dimensions of the interactive area in meters"
    bl_options = {'REGISTER', 'UNDO'}

    length: bpy.props.FloatProperty(
        name="Length [m]",
        description="Length of interaction area [m]",
        default=0.3,
        min=0.1,
        soft_max=1.0
    )

    width: bpy.props.FloatProperty(
        name="Width [m]",
        description="Width of interaction area [m]",
        default=0.4,
        min=0.1,
        soft_max=1.0
    )

    height: bpy.props.FloatProperty(
        name="Height [m]",
        description="Height of interaction area [m]",
        default=0.5,
        min=0.1,
        soft_max=1.0
    )

    include_support: bpy.props.BoolProperty(
        name="Include support",
        description="Enable to include the support for the mixed prototype",
        default=True,
    )

    # Agregamos un atributo de clase para guardar las dimensiones del objeto creado
    created_dimensionsPM = None

    def execute(self, context):
        # Convertir las dimensiones a metros
        length_m = self.length
        width_m = self.width
        height_m = self.height
        include_support = self.include_support

        # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
        parallelepiped_obj = bpy.data.objects.get("Parallelepiped")

        if parallelepiped_obj:
            # Modificar las dimensiones del paralelepípedo existente actualizando los vértices
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            # Obtener la malla del objeto existente
            parallelepiped_mesh = parallelepiped_obj.data

            # Actualizar las coordenadas de los vértices del objeto de malla
            for i, vertex in enumerate(vertices):
                parallelepiped_mesh.vertices[i].co = vertex

            # Actualizar la malla del objeto
            parallelepiped_mesh.update()

        else:
            # Crear los vértices y caras del paralelepípedo como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            # Definir aristas (bordes) usando índices de vértices
            edges = [
                (0, 1), (1, 2), (2, 3), (3, 0),  # Base
                (4, 5), (5, 6), (6, 7), (7, 4),  # Tapa
                (0, 4), (1, 5), (2, 6), (3, 7)   # Conexiones verticales
            ]

            # Crear el objeto malla en Blender con solo aristas
            mesh = bpy.data.meshes.new("Parallelepiped")
            mesh.from_pydata(vertices, edges, [])  # No hay caras, por lo que pasamos una lista vacía para las caras
            mesh.update()

            # Crear el objeto de paralelepípedo en la escena de Blender
            obj = bpy.data.objects.new("Parallelepiped", mesh)
            obj.location = (0.0, 0.0, 0.85)  # 0.85 es la altura de la mesa
            context.collection.objects.link(obj)

            #faces = [
                #(0, 1, 2, 3),    # Cara inferior
                #(4, 7, 6, 5),    # Cara superior
                #(0, 4, 5, 1),    # Cara lateral 1
                #(1, 5, 6, 2),    # Cara lateral 2
                #(2, 6, 7, 3),    # Cara lateral 3
                #(3, 7, 4, 0)     # Cara lateral 4
            #]

            # Crear el objeto malla en Blender
            #mesh = bpy.data.meshes.new("Parallelepiped")
            #mesh.from_pydata(vertices, [], faces)
            #mesh.update()

            # Crear el objeto de paralelepípedo en la escena de Blender
            #obj = bpy.data.objects.new("Parallelepiped", mesh)
            #obj.location = (0.0, 0.0, 0.85)  # 0.85 es la altura de la mesa
            #context.collection.objects.link(obj)

            #material_blanco = bpy.data.materials.new(name="White material")
            #material_blanco.use_nodes = False  # Deshabilitar nodos para el material simple

            # Configurar el color blanco para el material
            #material_blanco.diffuse_color = (0.5, 0.5, 0.5, 1)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

            # Asignar el material al objeto
            #obj.data.materials.append(material_blanco)

            # Realizar una acción adicional si el checkbox está activado
            if include_support:
                bpy.ops.object.create_table()

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            OBJECT_OT_create_parallelepiped.created_dimensionsPM = (length_m, width_m, height_m)
            
            # Evita un bug en el cual el espacio se vuelve negro luego de modificar este parametro
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.select_all(action='DESELECT')

        return {'FINISHED'}


### OPERADOR PARA DEFINIR PR Sync speed (LISTO)(ACTUALIZADO) -------------------------------------------------

class SetNumberOperator(bpy.types.Operator):
    bl_idname = "object.set_number"
    bl_label = "Sync speed"
    bl_description = "It refers to the frequency at which the projector displays new images on the screen or projection surface. A higher Sync speed results in a smoother image transition and a smoother viewing experience."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Level",
        description="It refers to the frequency at which the projector displays new images on the screen or projection surface. A higher Sync speed results in a smoother image transition and a smoother viewing experience. Select the most representative option for your requirement.",
        items=[
            ('MEDIUM', "Medium sync speed", "Option with minimum value"),
            ('HIGH', "High sync speed", "Option with maximum value")
        ],
        default='MEDIUM'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == 'MEDIUM':
            number = veloc_sinc[1]
            insumo = 'LCD technology'
        elif self.options == 'HIGH':
            number = veloc_sinc[2]
            insumo = 'DLP technology'
        else:
            return {'CANCELLED'}

        # Limpiar la lista antes de agregar el nuevo valor
        veloc_sinc_def.clear()

        # Agregar el último valor a la lista
        veloc_sinc_def.append(insumo)

        texto_a_eliminar = "Sync speed"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}


### OPERADOR PARA DEFINIR PR Brightness (ACTUALIZADO) -------------------------------------------------------------------------------

class SetNumberOperator2(bpy.types.Operator):
    bl_idname = "object.set_number2"
    bl_label = "Ambient lighting"
    bl_description = "Refers to the level of ambient lighting present in the mixed prototyping room."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Ambient lighting",
        description="It refers to the brightness that the projector delivers, which needs more or less lighting depending on the control you have over the ambient light in the room. Select the most representative option for your requirement.",
        items=[
            ('1', "Dark room", "A room at night with all lights turned off"),
            ('2', "Dim room", "A room with soft lightning at night"),
            ('3', "Lit room", "A room with no daylight (Home Teather)"),
            ('4', "Bright room", "A room with windows and indirect daylight"),
            ('5', "Outdoors", "Indirect sunlight"),
        ],
        default='3'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == '1':
            number2 = Brightness[1]
            insumo2 = '50 Nits'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            #Calculo de nits a lumens app
            lumens = 50 * (length2_m * width2_m) * 3.426 #1 Nit = 3,426 Lúmenes.
            lumens_fin.clear()
            lumens_fin.append(lumens)

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_cube_obj = bpy.data.objects.get("Cube")

            if custom_cube_obj:
                bpy.data.objects.remove(custom_cube_obj)

            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)

        elif self.options == '2':
            number2 = Brightness[2]
            insumo2 = '100 Nits'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            #Calculo de nits a lumens app
            lumens = 100 * (length2_m * width2_m) * 3.426 #1 Nit = 3,426 Lúmenes.
            lumens_fin.clear()
            lumens_fin.append(lumens)
            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_cube_obj = bpy.data.objects.get("Cube")

            if custom_cube_obj:
                bpy.data.objects.remove(custom_cube_obj)

            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)

        elif self.options == '3':
            number2 = Brightness[3]
            insumo2 = '200 Nits'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            #Calculo de nits a lumens app
            lumens = 200 * (length2_m * width2_m) * 3.426 #1 Nit = 3,426 Lúmenes.
            lumens_fin.clear()
            lumens_fin.append(lumens)

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_cube_obj = bpy.data.objects.get("Cube")

            if custom_cube_obj:
                bpy.data.objects.remove(custom_cube_obj)

            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)

        elif self.options =='4':
            number2 = Brightness[4]
            insumo2 = '300 - 600 Nits'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            #Calculo de nits a lumens app
            lumens = ((300+600)/2) * (length2_m * width2_m) * 3.426 #1 Nit = 3,426 Lúmenes.
            lumens_fin.clear()
            lumens_fin.append(lumens)

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_cube_obj = bpy.data.objects.get("Cube")

            if custom_cube_obj:
                bpy.data.objects.remove(custom_cube_obj)

            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)


        elif self.options =='5':
            number2 = Brightness[4]
            insumo2 = '+ 600 Nits'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            #Calculo de nits a lumens app
            lumens = 600 * (length2_m * width2_m) * 3.426 #1 Nit = 3,426 Lúmenes.
            lumens_fin.clear()
            lumens_fin.append(lumens)

            #Eliminar las paredes del cubo y solo dejar plano de base

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_cube_obj = bpy.data.objects.get("Cube")

            if custom_cube_obj:
                bpy.data.objects.remove(custom_cube_obj)

            # Crear los vértices y caras del Cube como lo hacías anteriormente
            vertices = [
                (-length_m / 2, -width_m / 2, 0),     # Vértice 0
                (-length_m / 2, width_m / 2, 0),      # Vértice 1
                (length_m / 2, width_m / 2, 0),       # Vértice 2
                (length_m / 2, -width_m / 2, 0),      # Vértice 3
                (-length_m / 2, -width_m / 2, height_m),   # Vértice 4
                (-length_m / 2, width_m / 2, height_m),    # Vértice 5
                (length_m / 2, width_m / 2, height_m),     # Vértice 6
                (length_m / 2, -width_m / 2, height_m)     # Vértice 7
            ]

            faces = [
                (0, 1, 2, 3),    # Cara inferior
            ]
            
            #Limpiar lista vertice 1
            vertice_1.clear()
            
            # Guardar las coordenadas del vértice 1 en el contexto
            vertice_1.append(-length_m / 2)
            vertice_1.append(width_m / 2)
            vertice_1.append(0)

            # Crear el objeto de malla en Blender
            mesh = bpy.data.meshes.new("Cube")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Cube", mesh)
            context.collection.objects.link(obj)

            # Guardamos las dimensiones del objeto creado en el atributo de clase
            CreateCubeOperator.created_dimensionsCube = (length_m, width_m, height_m)

        else:
            return {'CANCELLED'}


        # Limpiar la lista antes de agregar el nuevo valor
        Brightness_def.clear()

        # Agregar el último valor a la lista
        Brightness_def.append(insumo2)

        texto_a_eliminar = "Brightness"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Brightness_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}

### OPERADOR PARA DEFINIR PR Sharpness (ACTUALIZADO) ### -------------------------------------------------------------------------

class SetNumberOperator3(bpy.types.Operator):
    bl_idname = "object.set_number3"
    bl_label = "Projection sharpness"
    bl_description = "It refers to the definition of the image projected on the projection surface."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Sharpness level",
        description="It refers to the definition of the image projected on the projection surface. Select the most representative option for your requirement.",
        items=[
            ('1', "Low sharpness", "Corresponds to a resolution of 800x600 px"),
            ('2', "Medium-Low sharpness", "Corresponds to a resolution of 1024x768 px"),
            ('3', "Medium sharpness", "Corresponds to a resolution of 1280x800 px"),
            ('4', "Medium-High sharpness", "Corresponds to a resolution of 1920x1080 px"),
            ('5', "High sharpness", "Corresponds to a resolution of 1920x1200 px"),
            ('6', "Maximum sharpness", "Corresponds to a resolution of 3840x2160 px"),
        ],
        default='6'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == '1':
            number3 = Sharpness[1]
            insumo3 = 'SVGA'

        elif self.options == '2':
            number3 = Sharpness[2]
            insumo3 = 'XGA'

        elif self.options == '3':
            number3 = Sharpness[3]
            insumo3 = 'WXGA'

        elif self.options =='4':
            number3 = Sharpness[4]
            insumo3 = 'Full HD (1080p)'

        elif self.options =='5':
            number3 = Sharpness[5]
            insumo3 = 'WUXGA'

        elif self.options =='6':
            number3 = Sharpness[6]
            insumo3 = '4K Ultra HD'

        else:
            return {'CANCELLED'}

        # Limpiar la lista antes de agregar el nuevo valor
        Sharpness_def.clear()

        # Agregar el último valor a la lista
        Sharpness_def.append(insumo3)

        texto_a_eliminar = "Sharpness"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Brightness_def)
        #print(Sharpness_def)
        #print(Espacio_diseño_act)
        
        # Evita un bug en el cual el espacio se vuelve negro luego de modificar este parametro
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.select_all(action='DESELECT')


        return {'FINISHED'}

### OPERADOR PARA DEFINIR PR Proximity of the projector (3 OPCIONES)(ACTUALIZADO) ----------------------------------------------

class CreateCustomParallelepipedOperator3(bpy.types.Operator):
    bl_idname = "object.create_custom_parallelepiped3"
    bl_label = "Spawn projector in space"
    bl_description = "Create a parallelepiped in space that represents the projector in different positions according to its throw type."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Proximity to AO",
        description="It refers to the distance between the projector and the image projected on the mixed prototype. Select to display the projector throw options available according to the previously entered data",
        items=[
            ('Very close', "Very close", "Corresponds to the reference distance of an ultra-Short throw projector"),
            ('Nearby', "Nearby", "Corresponds to the reference distance of a Short throw projector"),
            ('Distant', "Distant", "Corresponds to the reference distance of a long throw projector"),
        ],
        default='Distant'
    )
        
    def execute(self, context):
        # Verificamos si las dimensiones del espacio fueron guardadas previamente
        if CreateCubeOperator.created_dimensionsCube is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

        # Verificamos si las dimensiones del espacio fueron guardadas previamente
        if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

        # Obtener la ubicación del objeto previo seleccionado (paralelepípedo creado anteriormente)
        parallelepiped_obj = bpy.context.active_object

        if parallelepiped_obj and parallelepiped_obj.type == 'MESH':
            # Obtener la ubicación del objeto previo seleccionado
            parallelepiped_location = parallelepiped_obj.location.copy()

            if self.options == 'Very close':
                # Opción A
                parallelepiped_location.y = - width2_m - 0.4 #es - width2 para que quede hacia el lado izquierdo de la habitacion
                insumo = 'Ultra short throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            elif self.options == 'Nearby':
                # Opción B
                parallelepiped_location.y = - width2_m - (0.5 + 0.4) #considerando el largo del proyector
                insumo = 'Short throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            elif self.options == 'Distant':
                # Opción C
                parallelepiped_location.y = - width2_m - (1.0 + 0.4) #considerando el largo del proyector y además se considera un valor menor al real para mantener proyector dentro de la pieza, ya que por defecto la mesa se genera en el centro de la habitación
                insumo = 'Long Throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            else:
                return {'CANCELLED'}

            # Dimensiones del nuevo paralelepípedo(52x45x19cm) EPSONL1000
            new_length_m = 0.4
            new_width_m = 0.4
            new_height_m = 0.1

            # Calcular la posición Z del nuevo objeto (160 cm) 
            if height_m < 2.5:
                new_z_position = 1.6
            else:
                new_z_position = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_parallelepiped3_obj = bpy.data.objects.get("Custom parallelepiped")

            if custom_parallelepiped3_obj:
                bpy.data.objects.remove(custom_parallelepiped3_obj)

            # Crear los vértices del Parallelepiped como se hace originalmente
            
            vertices = [
            (-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
            (-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
            (new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
            (new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
            (-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
            (-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
            (new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
            (new_length_m / 2, -new_width_m / 2, -new_height_m)     # Vértice 7
            
            ]


            # Crear las caras del Parallelepiped
            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (4, 7, 6, 5),    # Cara superior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
                (2, 6, 7, 3),    # Cara lateral 3
                (3, 7, 4, 0)     # Cara lateral 4
                ]

            # Crear el objeto malla en Blender
            mesh = bpy.data.meshes.new("Custom parallelepiped")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Custom parallelepiped", mesh)

            # Crear un nuevo material con el nombre "Green material"
            material_verde = bpy.data.materials.new(name="Green material")
            material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

            # Configurar el color verde para el material
            material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

            # Asignar el material al objeto
            obj.data.materials.append(material_verde)

            obj.location = (parallelepiped_location.x, parallelepiped_location.y, new_z_position)
            context.collection.objects.link(obj)

            # Generar soporte para el proyector

            # Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            support_projector = bpy.data.objects.get("Projector support")

            if support_projector:
                bpy.data.objects.remove(support_projector)

            # Crear el objeto de soporte en la escena de Blender

            #definir su profundidad (si es que la diferencia entre el techo y el proyector es muy poca, se asigna 0.1 como estandar)

            resta = height_m - new_z_position

            if resta > 0.01:
                depth_s = resta
            else:
                depth_s = 0.1
            
            if height_m < 2.5: #2.5 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= depth_s)
                objs = bpy.context.object
                objs.location.z = new_z_position + ((depth_s)/2)
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            elif height_m < 3.35: #2.5 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= depth_s)
                objs = bpy.context.object
                objs.location.z = new_z_position + ((depth_s)/2) #menos su mitad para que quede bien posicionado
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            else: 
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs = bpy.context.object
                objs.location.z = 1.25 #2.5 dividido en 2
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            #Limpiar lista proyector
            ubic_proyector.clear()
            
            #Registrar ubicación del proyector
            ubic_proyector.append(parallelepiped_location.x)
            ubic_proyector.append(parallelepiped_location.y)
            ubic_proyector.append(new_z_position)

            # Limpiar la lista antes de agregar el nuevo valor
            proximidad_p_def.clear()

            # Agregar el último valor a la lista
            proximidad_p_def.append(insumo)

            texto_a_eliminar = "Proximity of the projector"

            eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

            return {'FINISHED'}

        return {'CANCELLED'}

### OPERADOR PARA DEFINIR PR Proximity of the projector (2 OPCIONES)(ACTUALIZADO) ------------------------------------------------

class CreateCustomParallelepipedOperator2(bpy.types.Operator):
    bl_idname = "object.create_custom_parallelepiped2"
    bl_label = "Spawn projector in space"
    bl_description = "Create a parallelepiped in space that represents the projector in different positions according to its throw type."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Proximity to the augmented object",
        description="It refers to the distance between the projector and the image projected on the mixed prototype. Select to display the projector throw options available according to the previously entered data",
        items=[
            ('Very close', "Very close", "Corresponds to the reference distance of an ultra-Short throw projector"),
            ('Nearby', "Nearby", "Corresponds to the reference distance of a Short throw projector"),
        ],
        default='Nearby'
    )
        
    def execute(self, context):
        # Verificamos si las dimensiones del espacio fueron guardadas previamente
        if CreateCubeOperator.created_dimensionsCube is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

        # Verificamos si las dimensiones del espacio fueron guardadas previamente
        if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

        # Obtener la ubicación del objeto previo seleccionado (paralelepípedo creado anteriormente)
        parallelepiped_obj = bpy.context.active_object

        if parallelepiped_obj and parallelepiped_obj.type == 'MESH':
            # Obtener la ubicación del objeto previo seleccionado
            parallelepiped_location = parallelepiped_obj.location.copy()

            if self.options == 'Very close':
                # Opción A
                parallelepiped_location.y = width2_m - 1
                insumo = 'Ultra short throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            elif self.options == 'Nearby':
                # Opción B
                parallelepiped_location.y += width2_m - 1.4
                insumo = 'Short throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            else:
                return {'CANCELLED'}

            # Dimensiones del nuevo paralelepípedo(52x45x19cm) EPSONL1000
            new_length_m = 0.4
            new_width_m = 0.4
            new_height_m = 0.1

            # Calcular la posición Z del nuevo objeto (160 cm)
            if height_m < 2.5:
                new_z_position = 1.6
            else:
                new_z_position = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_parallelepiped2_obj = bpy.data.objects.get("Custom parallelepiped")

            if custom_parallelepiped2_obj:
                bpy.data.objects.remove(custom_parallelepiped2_obj)

            # Crear los vértices del paralelepípedo como se hace originalmente
            
            vertices = [
            (-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
            (-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
            (new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
            (new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
            (-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
            (-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
            (new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
            (new_length_m / 2, -new_width_m / 2, -new_height_m)     # Vértice 7
            
            ]

            # Crear las caras del paralelepípedo
            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (4, 7, 6, 5),    # Cara superior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
                (2, 6, 7, 3),    # Cara lateral 3
                (3, 7, 4, 0)     # Cara lateral 4
                ]

            # Crear el objeto malla en Blender
            mesh = bpy.data.meshes.new("Custom parallelepiped")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Custom parallelepiped", mesh)

            # Crear un nuevo material con el nombre "Green material"
            material_verde = bpy.data.materials.new(name="Green material")
            material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

            # Configurar el color verde para el material
            material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

            # Asignar el material al objeto
            obj.data.materials.append(material_verde)

            obj.location = (parallelepiped_location.x, parallelepiped_location.y, new_z_position)
            context.collection.objects.link(obj)

            #Generar soporte para el proyector

            # Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            support_projector = bpy.data.objects.get("Projector support")

            if support_projector:
                bpy.data.objects.remove(support_projector)

                # Crear el objeto de soporte en la escena de Blender
            if height_m < 3.35: #1.60 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= height_m - new_z_position)
                objs = bpy.context.object
                objs.location.z = new_z_position + ((height_m - new_z_position)/2)
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            else: 
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs = bpy.context.object
                objs.location.z = 1.25 #2.5 dividido en 2
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            #Limpiar lista proyector
            ubic_proyector.clear()
            
            #Registrar ubicación del proyector
            ubic_proyector.append(parallelepiped_location.x)
            ubic_proyector.append(parallelepiped_location.y)
            ubic_proyector.append(new_z_position)

            # Limpiar la lista antes de agregar el nuevo valor
            proximidad_p_def.clear()

            # Agregar el último valor a la lista
            proximidad_p_def.append(insumo)

            texto_a_eliminar = "Proximity of the projector"

            eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

            return {'FINISHED'}

        return {'CANCELLED'}

### OPERADOR PARA DEFINIR PR Proximity of the projector (1 OPCION)(ACTUALIZADO) --------------------------------------------------

class CreateCustomParallelepipedOperator1(bpy.types.Operator):
    bl_idname = "object.create_custom_parallelepiped1"
    bl_label = "Spawn projector in space"
    bl_description = "Create a parallelepiped in space that represents the projector in different positions according to its throw type."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Proximity to the augmented object",
        description="It refers to the distance between the projector and the image projected on the mixed prototype. Select to display the projector throw options available according to the previously entered data",
        items=[
            ('Very close', "Very close", "Corresponds to the reference distance of an ultra-Short throw projector"),
        ],
        default='Very close'
    )
        
    def execute(self, context):
        # Verificamos si las dimensiones del espacio fueron guardadas previamente
        if CreateCubeOperator.created_dimensionsCube is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

        # Verificamos si las dimensiones del PM fueron guardadas previamente
        if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
            return {'CANCELLED'}

        # Obtenemos las dimensiones del objeto previamente creado
        length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

        # Obtener la ubicación del objeto previo seleccionado (paralelepípedo creado anteriormente)
        parallelepiped_obj = bpy.context.active_object

        if parallelepiped_obj and parallelepiped_obj.type == 'MESH':
            # Obtener la ubicación del objeto previo seleccionado
            parallelepiped_location = parallelepiped_obj.location.copy()

            if self.options == 'Very close':
                # Opción A
                parallelepiped_location.y = width2_m - 1
                insumo = 'Ultra short throw'
                tiro.clear()
                tiro.append(parallelepiped_location.y)

            else:
                return {'CANCELLED'}

            # Dimensiones del nuevo paralelepípedo(52x45x19cm) EPSONL1000
            new_length_m = 0.4
            new_width_m = 0.4
            new_height_m = 0.1

            # Calcular la posición Z del nuevo objeto (160 cm)
            if height_m < 2.5:
                new_z_position = 1.6
            else:
                new_z_position = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

            # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
            custom_parallelepiped1_obj = bpy.data.objects.get("Custom parallelepiped")

            if custom_parallelepiped1_obj:
                bpy.data.objects.remove(custom_parallelepiped1_obj)

            # Crear los vértices del Parallelepiped como se hace originalmente
            
            vertices = [
            (-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
            (-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
            (new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
            (new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
            (-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
            (-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
            (new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
            (new_length_m / 2, -new_width_m / 2, -new_height_m)     # Vértice 7
            
            ]


            # Crear las caras del Parallelepiped
            faces = [
                (0, 1, 2, 3),    # Cara inferior
                (4, 7, 6, 5),    # Cara superior
                (0, 4, 5, 1),    # Cara lateral 1
                (1, 5, 6, 2),    # Cara lateral 2
                (2, 6, 7, 3),    # Cara lateral 3
                (3, 7, 4, 0)     # Cara lateral 4
                ]

            # Crear el objeto malla en Blender
            mesh = bpy.data.meshes.new("Custom parallelepiped")
            mesh.from_pydata(vertices, [], faces)
            mesh.update()

            # Crear el objeto de Cube en la escena de Blender
            obj = bpy.data.objects.new("Custom parallelepiped", mesh)

            # Crear un nuevo material con el nombre "Green material"
            material_verde = bpy.data.materials.new(name="Green material")
            material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

            # Configurar el color verde para el material
            material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

            # Asignar el material al objeto
            obj.data.materials.append(material_verde)

            obj.location = (parallelepiped_location.x, parallelepiped_location.y, new_z_position) #OJO
            context.collection.objects.link(obj)

            #Generar soporte para el proyector

            # Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            support_projector = bpy.data.objects.get("Projector support")

            if support_projector:
                bpy.data.objects.remove(support_projector)

                # Crear el objeto de soporte en la escena de Blender
            if height_m < 3.35: #1.60 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= height_m - new_z_position)
                objs = bpy.context.object
                objs.location.z = new_z_position + ((height_m - new_z_position)/2)
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            else: 
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs = bpy.context.object
                objs.location.z = 1.25 #2.5 dividido en 2
                objs.location.y = parallelepiped_location.y  # Configura la ubicación Y aquí
                objs.name = "Projector support"

            #Limpiar lista proyector
            ubic_proyector.clear()
            
            #Registrar ubicación del proyector
            ubic_proyector.append(parallelepiped_location.x)
            ubic_proyector.append(parallelepiped_location.y)
            ubic_proyector.append(new_z_position)


            # Limpiar la lista antes de agregar el nuevo valor
            proximidad_p_def.clear()

            # Agregar el último valor a la lista
            proximidad_p_def.append(insumo)

            texto_a_eliminar = "Proximity of the projector"

            eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

            return {'FINISHED'}

        return {'CANCELLED'}


### OPERADOR PARA DEFINIR PR ANGULOS DE VISION ------------------------------------------------------

class SetNumberOperator5(bpy.types.Operator):
    bl_idname = "object.set_number5"
    bl_label = "Degree of user vision over the mixed prototype"
    bl_description = "It refers to the degree of vision that users will have when co-designing the product in the space."
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Coverage angle",
        description="It refers to the degree of vision that users will have when co-designing the product in the space. Select the most representative option for your requirement.",
        items=[
            ('0° to 160°', "0° to 160°", "People will have a vision range of 0 to 160 degrees towards the mixed prototype."),
            ('160° to 240°', "160° to 240°", "People will have a vision range of 160 to 240 degrees towards the mixed prototype."),
            ('240° to 360°', "240° to 360°", "People will have a vision range of 240 to 360 degrees towards the mixed prototype."),
        ],
        default='160° to 240°'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada

        if self.options == '0° to 160°':
            number51 = cant_p[0][1]
            insumo51 = '0° to 160° vision of the mixed prototype'
            number52 = cant_p[1][1]
            insumo52 =  '1 projector'
            angulo.clear()
            angulo.append('180')

            #DEFINIR CONFIGURACIÓN DEL SISTEMA SAR

            # Filtrar según la dependencia del angulo de visión
        
            #Eliminar colecciones si es que ya existian
            #nombre_coleccion_a_eliminar1 = "Configuration 1"  # Reemplaza con el nombre de la colección que deseas eliminar
            #eliminar_coleccion(nombre_coleccion_a_eliminar1)
            #nombre_coleccion_a_eliminar2 = "Configuration 2"  # Reemplaza con el nombre de la colección que deseas eliminar
            #eliminar_coleccion(nombre_coleccion_a_eliminar2)

            #Ocultar colección original y dejar solo Configuration 1 visible
            #nombre_coleccion_original = "Collection"  # Reemplaza con el nombre de tu colección original
            #nombre_coleccion_destino = "Configuration 1"    # Reemplaza con el nombre de tu colección de destino Configuration 1
            #nombre_coleccion_destino2 = "Configuration 2"    # Reemplaza con el nombre de tu colección de destino Configuration 2

            #duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino)
            #duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino2)

            # Ocultar colección original
            #nombre_coleccion = "Collection"
            #ocultar_coleccion(nombre_coleccion)
            #ocultar_coleccion("Configuration 1")
            

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Calcular la posición Z del nuevo objeto
            new_z_position2 = height_m

            # Editar posicion de un objeto de la colección

            nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion1 = (vertice_1[0] + (length_m/2),vertice_1[1] - (width_m/2), 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion2 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion3 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar4 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion4 = (ubic_proyector[0], ubic_proyector[1] , ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            if height_m > 3.35:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            else:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #Reposición de sistema de tracking

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            
            if support_projectorA:
                nombre_objeto_reposicionar6 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)

            if support_projectorB:
                nombre_objeto_reposicionar6 = "Camera 1 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (pos_pm[0] + 1, pos_pm[1] + 1, new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar7 = "Camera 2 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (pos_pm[0] - 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar8 = "Camera 3 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (pos_pm[0] + 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Camera 4 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (pos_pm[0] - 1,pos_pm[1] + 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)

            #Definir posicion del PM para posteriormente añadir el tracking

            pos_pm.clear()
            pos_pm.append(vertice_1[0] + (length_m/2)) #x
            pos_pm.append(vertice_1[1] - (width_m/2)) #y
            pos_pm.append(new_z_position2) #z

        #elif self.options == '160° to 240° degrees':
            #number51 = cant_p[0][1]
            #insumo51 = '180° vision of the mixed prototype'
            #number52 = cant_p[1][2]
            #insumo52 = '2 projectors'
            #angulo.clear()
            #angulo.append('180')

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            #if CreateCubeOperator.created_dimensionsCube is None:
                #return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            #length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Verificamos si las dimensiones del PM fueron guardadas previamente
            #if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                #return {'CANCELLED'}

            # Obtener la ubicación del objeto previo seleccionado (Cube creado anteriormente)
            #cube_obj = bpy.context.active_object

            #if cube_obj and cube_obj.type == 'MESH':
                # Obtener la ubicación del objeto previo seleccionado
                #cube_location = cube_obj.location.copy()
                    
                # Dimensiones del nuevo Parallelepiped(52x45x19cm) EPSONL1000
                #new_length_m = 0.4
                #new_width_m = 0.4
                #new_height_m = 0.1

                # Calcular la posición Z del nuevo objeto (160 cm)
                #if height_m < 2.5:
                    #new_z_position2 = 1.6
                #else:
                    #new_z_position2 = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

                # Buscar si el objeto "Proyector" ya existe en la colección de objetos de Blender
                #custom_parallelepiped1_obj6 = bpy.data.objects.get("Projector 2")

                #if custom_parallelepiped1_obj6:
                    #bpy.data.objects.remove(custom_parallelepiped1_obj6)

                # Crear los vértices del Parallelepiped como se hace originalmente
            
                #vertices = [
                #(-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
                #(-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
                #(new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
                #(new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
                #(-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
                #(-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
                #(new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
                #(new_length_m / 2, -new_width_m / 2, -new_height_m),     # Vértice 7
                #]


                # Crear las caras del Parallelepiped
                #faces = [
                    #(0, 1, 2, 3),    # Cara inferior
                    #(4, 7, 6, 5),    # Cara superior
                    #(0, 4, 5, 1),    # Cara lateral 1
                    #(1, 5, 6, 2),    # Cara lateral 2
                    #(2, 6, 7, 3),    # Cara lateral 3
                    #(3, 7, 4, 0)     # Cara lateral 4
                    #]

                # Crear el objeto malla en Blender
                #mesh2 = bpy.data.meshes.new("Projector 2")
                #mesh2.from_pydata(vertices, [], faces)
                #mesh2.update()

                # Crear los objetos de Cube en la escena de Blender
                #obj6 = bpy.data.objects.new("Projector 2", mesh2)

                # Crear un nuevo material con el nombre "Green material"
                #material_verde = bpy.data.materials.new(name="Green material")
                #material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

                # Configurar el color verde para el material
                #material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

                # Asignar el material al objeto
                #obj6.data.materials.append(material_verde)

                # Calcular las coordenadas para ubicar los Cubes en esquinas distintas
                #cube_dimensions = (new_length_m, new_width_m, new_height_m)
                #space_dimensions = (length_m, width_m, height_m)
            
                # Asignar las ubicaciones de los objetos
                #obj6.location = (ubic_proyector[0] + tiro[0], ubic_proyector[1],new_z_position2)
                #context.collection.objects.link(obj6)

            #Generar soporte para el proyector 

            # Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            #support_projector2 = bpy.data.objects.get("Projector support 2")

            #if support_projector2:
                #bpy.data.objects.remove(support_projector2)

                # Crear el objeto de soporte en la escena de Blender
            #if height_m < 3.35: #1.60 + 0.85
                #bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= height_m - new_z_position2)
                #objs2 = bpy.context.object
                #objs2.location.z = new_z_position2 + ((height_m - new_z_position2)/2)
                #objs2.location.x = ubic_proyector[0] + tiro[0]  # Configura la ubicación Y aquí
                #objs2.name = "Projector support 2"

            #else: 
                #bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=1.5) #tripode desde piso
                #objs2 = bpy.context.object
                #objs2.location.z = 0.8 #1.60 dividido en 2
                #objs2.location.x = ubic_proyector[0] + tiro[0]  # Configura la ubicación Y aquí
                #objs2.name = "Projector support 2"

            #DEFINIR CONFIGURACIÓN DEL SISTEMA SAR

            # Filtrar según la dependencia del angulo de visión
        
            #Eliminar colecciones si es que ya existian
            #nombre_coleccion_a_eliminar1 = "Configuration 1"  # Reemplaza con el nombre de la colección que deseas eliminar
            #eliminar_coleccion(nombre_coleccion_a_eliminar1)
            #nombre_coleccion_a_eliminar2 = "Configuration 2"  # Reemplaza con el nombre de la colección que deseas eliminar
            #eliminar_coleccion(nombre_coleccion_a_eliminar2)

            #Ocultar colección original y dejar solo Configuration 1 visible
            #nombre_coleccion_original = "Collection"  # Reemplaza con el nombre de tu colección original
            #nombre_coleccion_destino = "Configuration 1"    # Reemplaza con el nombre de tu colección de destino Configuration 1
            #nombre_coleccion_destino2 = "Configuration 2"    # Reemplaza con el nombre de tu colección de destino Configuration 2

            #duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino)
            #duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino2)

            # Ocultar colección original
            #nombre_coleccion = "Collection"
            #ocultar_coleccion(nombre_coleccion)
            #ocultar_coleccion("Configuration 1")
            

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            #if CreateCubeOperator.created_dimensionsCube is None:
                #return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            #length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Calcular la posición Z del nuevo objeto
            #new_z_position2 = height_m

            # Editar posicion de un objeto de la colección

            #nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion1 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion2 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion3 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #nombre_objeto_reposicionar4 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion4 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #nombre_objeto_reposicionar5 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion5 = (ubic_proyector[0] - 0.5, ubic_proyector[1] - 0.5, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #nombre_objeto_reposicionar6 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
            #nueva_posicion6 = (ubic_proyector[0] - 0.5, ubic_proyector[1] - 0.5, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
            #reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
            #reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
            #reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
            #reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
            #reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)

            #Definir posicion del PM para posteriormente añadir el tracking

            #pos_pm.clear()
            #pos_pm.append(vertice_1[0] + 0.5) #x
            #pos_pm.append(vertice_1[1] - 0.5) #y
            #pos_pm.append(0.85) #z
            

        elif self.options == '160° to 240°':
            number51 = cant_p[0][2]
            insumo51 = '160° to 240° vision of the mixed prototype'
            number52 = cant_p[1][2]
            insumo52 = '2 projectors'
            angulo.clear()
            angulo.append('360')

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Verificamos si las dimensiones del PM fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtener la ubicación del objeto previo seleccionado (Cube creado anteriormente)
            cube_obj = bpy.context.active_object

            if cube_obj and cube_obj.type == 'MESH':
                # Obtener la ubicación del objeto previo seleccionado
                cube_location = cube_obj.location.copy()
                    
                # Dimensiones del nuevo Parallelepiped(52x45x19cm) EPSONL1000
                new_length_m = 0.4
                new_width_m = 0.4
                new_height_m = 0.1

            
                # Calcular la posición Z del nuevo objeto (160 cm)
                if height_m < 2.5:
                    new_z_position2 = 1.6
                else:
                    new_z_position2 = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

                # Buscar si el objeto "Proyector" ya existe en la colección de objetos de Blender
                custom_parallelepiped1_obj6 = bpy.data.objects.get("Projector 2")

                if custom_parallelepiped1_obj6:
                    bpy.data.objects.remove(custom_parallelepiped1_obj6)

                # Crear los vértices del Parallelepiped como se hace originalmente
            
                vertices = [
                (-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
                (-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
                (new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
                (new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
                (-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
                (-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
                (new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
                (new_length_m / 2, -new_width_m / 2, -new_height_m),     # Vértice 7
                ]


                # Crear las caras del Parallelepiped
                faces = [
                    (0, 1, 2, 3),    # Cara inferior
                    (4, 7, 6, 5),    # Cara superior
                    (0, 4, 5, 1),    # Cara lateral 1
                    (1, 5, 6, 2),    # Cara lateral 2
                    (2, 6, 7, 3),    # Cara lateral 3
                    (3, 7, 4, 0)     # Cara lateral 4
                    ]

                # Crear el objeto malla en Blender
                mesh2 = bpy.data.meshes.new("Projector 2")
                mesh2.from_pydata(vertices, [], faces)
                mesh2.update()

                # Crear los objetos de Cube en la escena de Blender
                obj6 = bpy.data.objects.new("Projector 2", mesh2)

                # Crear un nuevo material con el nombre "Green material"
                material_verde = bpy.data.materials.new(name="Green material")
                material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

                # Configurar el color verde para el material
                material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

                # Asignar el material al objeto
                obj6.data.materials.append(material_verde)

                # Calcular las coordenadas para ubicar los Cubes en esquinas distintas
                cube_dimensions = (new_length_m, new_width_m, new_height_m)
                space_dimensions = (length_m, width_m, height_m)
            
                # Asignar las ubicaciones de los objetos
                print(ubic_proyector)
                obj6.location = (ubic_proyector[0] + tiro[0]/2 - (1/2), ubic_proyector[1] - tiro[0] + (3**0.5)/2,new_z_position2) #con ese valor se forma 120° con el proyector
                #obj6.location = (ubic_proyector[0] + tiro[0], ubic_proyector[1] - tiro[0],new_z_position2)
                context.collection.objects.link(obj6)

            #Generar soporte para el proyector

            #Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            support_projector2 = bpy.data.objects.get("Projector support 2")

            if support_projector2: 
                bpy.data.objects.remove(support_projector2)

            resta = height_m - new_z_position2

            if resta > 0.01:
                depth_s = resta
            else:
                depth_s = 0.1

                # Crear el objeto de soporte en la escena de Blender
            if height_m < 3.35: #1.60 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= depth_s)
                objs2 = bpy.context.object
                objs2.location.z = new_z_position2 + ((depth_s)/2)
                objs2.location.x = ubic_proyector[0] + tiro[0]/2 - (1/2)  # Configura la ubicación Y aquí
                objs2.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2
                objs2.name = "Projector support 2"

            else: 
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs2 = bpy.context.object
                objs2.location.z = 1.25 #1.60 dividido en 2
                objs2.location.x = ubic_proyector[0] + tiro[0]/2 - (1/2)  # Configura la ubicación Y aquí
                objs2.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2
                objs2.name = "Projector support 2"



            # Editar posicion de un objeto de la colección

            nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion1 = (vertice_1[0] + (length_m/2),vertice_1[1] - (width_m/2), 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion2 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion3 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar4 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion4 = (ubic_proyector[0], ubic_proyector[1], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar5 = "Projector 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion5 = (ubic_proyector[0] - 1, ubic_proyector[1] , ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            
            if height_m > 3.35:
                nombre_objeto_reposicionar6 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar7 = "Projector support 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (ubic_proyector[0] - 1, ubic_proyector[1] - tiro[0]/2, ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)
            

            else:
                nombre_objeto_reposicionar6 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar7 = "Projector support 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (ubic_proyector[0] - 1, ubic_proyector[1] - tiro[0]/2, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)


            #Reposición de sistema de tracking

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            
            if support_projectorA:
                nombre_objeto_reposicionar8 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)

            if support_projectorB:
                nombre_objeto_reposicionar8 = "Camera 1 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (pos_pm[0] + 1, pos_pm[1] + 1, new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Camera 2 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (pos_pm[0] - 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar10 = "Camera 3 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion10 = (pos_pm[0] + 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar11 = "Camera 4 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion11 = (pos_pm[0] - 1,pos_pm[1] + 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)
                reposicionar_objeto(nombre_objeto_reposicionar10, nueva_posicion10)
                reposicionar_objeto(nombre_objeto_reposicionar11, nueva_posicion11)


            #Definir posicion del PM para posteriormente añadir el tracking

            pos_pm.clear()
            pos_pm.append(vertice_1[0] + (length_m/2)) #x
            pos_pm.append(vertice_1[1] - (width_m/2)) #y
            pos_pm.append(new_z_position2) #z
        

        elif self.options =='240° to 360°':
            number51 = cant_p[0][2]
            insumo51 = '240° to 360° vision of the mixed prototype'
            number52 = cant_p[1][3]
            insumo52 = '3 projectors'
            angulo.clear()
            angulo.append('360')

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Verificamos si las dimensiones del PM fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtener la ubicación del objeto previo seleccionado (Cube creado anteriormente)
            cube_obj = bpy.context.active_object

            if cube_obj and cube_obj.type == 'MESH':
                # Obtener la ubicación del objeto previo seleccionado
                cube_location = cube_obj.location.copy()
                    
                # Dimensiones del nuevo Parallelepiped(52x45x19cm) EPSONL1000
                new_length_m = 0.4
                new_width_m = 0.4
                new_height_m = 0.1

                # Calcular la posición Z del nuevo objeto (160 cm)
                if height_m < 2.5:
                    new_z_position2 = 1.6
                else:
                    new_z_position2 = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

                # Buscar si el objeto "Proyector" ya existe en la colección de objetos de Blender
                custom_parallelepiped1_obj6 = bpy.data.objects.get("Projector 2")
                custom_parallelepiped1_obj7 = bpy.data.objects.get("Projector 3")

                if custom_parallelepiped1_obj6:
                    bpy.data.objects.remove(custom_parallelepiped1_obj6)
                    bpy.data.objects.remove(custom_parallelepiped1_obj7)

                # Crear los vértices del Parallelepiped como se hace originalmente
            
                vertices = [
                (-new_length_m / 2, -new_width_m / 2, 0),     # Vértice 0
                (-new_length_m / 2, new_width_m / 2, 0),      # Vértice 1
                (new_length_m / 2, new_width_m / 2, 0),       # Vértice 2
                (new_length_m / 2, -new_width_m / 2, 0),      # Vértice 3
                (-new_length_m / 2, -new_width_m / 2, -new_height_m),   # Vértice 4
                (-new_length_m / 2, new_width_m / 2, -new_height_m),    # Vértice 5
                (new_length_m / 2, new_width_m / 2, -new_height_m),     # Vértice 6
                (new_length_m / 2, -new_width_m / 2, -new_height_m),     # Vértice 7
                ]


                # Crear las caras del Parallelepiped
                faces = [
                    (0, 1, 2, 3),    # Cara inferior
                    (4, 7, 6, 5),    # Cara superior
                    (0, 4, 5, 1),    # Cara lateral 1
                    (1, 5, 6, 2),    # Cara lateral 2
                    (2, 6, 7, 3),    # Cara lateral 3
                    (3, 7, 4, 0)     # Cara lateral 4
                    ]

                # Crear el objeto malla en Blender
                mesh2 = bpy.data.meshes.new("Projector 2")
                mesh2.from_pydata(vertices, [], faces)
                mesh2.update()


                # Crear los objetos de Cube en la escena de Blender
                obj6 = bpy.data.objects.new("Projector 2", mesh2)
                obj7 = bpy.data.objects.new("Projector 3", mesh2)

                # Crear un nuevo material con el nombre "Green material"
                material_verde = bpy.data.materials.new(name="Green material")
                material_verde.use_nodes = False  # Deshabilitar nodos para el material simple

                # Configurar el color verde para el material
                material_verde.diffuse_color = (0.1, 0.8, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

                # Asignar el material al objeto
                obj6.data.materials.append(material_verde)
                obj7.data.materials.append(material_verde)

                # Calcular las coordenadas para ubicar los Cubes en esquinas distintas
                cube_dimensions = (new_length_m, new_width_m, new_height_m)
                space_dimensions = (length_m, width_m, height_m)
            
                # Asignar las ubicaciones de los objetos
                #obj6.location = (ubic_proyector[0] + tiro[0], ubic_proyector[1] - tiro[0],new_z_position2)
                obj6.location = (ubic_proyector[0] + tiro[0]/2 - (1/2), ubic_proyector[1] - tiro[0] + (3**0.5)/2,new_z_position2)
                context.collection.objects.link(obj6)

                #obj7.location = (ubic_proyector[0] , ubic_proyector[1] - tiro[0]*2 ,new_z_position2) #ACAAA
                obj7.location = (-(ubic_proyector[0] + tiro[0]/2 - (1/2)), ubic_proyector[1] - tiro[0] + (3**0.5)/2,new_z_position2)
                context.collection.objects.link(obj7)

            #Generar soporte para el proyector

            # Buscar si el objeto "Cilindro" ya existe en la colección de objetos de Blender
            support_projector2 = bpy.data.objects.get("Projector support 2")
            support_projector3 = bpy.data.objects.get("Projector support 3")

            if support_projector2:
                bpy.data.objects.remove(support_projector2)
                bpy.data.objects.remove(support_projector3)

            resta = height_m - new_z_position2

            if resta > 0.01:
                depth_s = resta
            else:
                depth_s = 0.1

                # Crear el objeto de soporte en la escena de Blender
            if height_m < 3.35: #1.60 + 0.85
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= depth_s)
                objs2 = bpy.context.object
                objs2.location.z = new_z_position2 + ((depth_s)/2)
                objs2.location.x = ubic_proyector[0] + tiro[0]/2 - (1/2)  # Configura la ubicación Y aquí
                objs2.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2
                objs2.name = "Projector support 2"

                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth= depth_s)
                objs3 = bpy.context.object
                objs3.location.z = new_z_position2 + ((depth_s)/2)
                objs3.location.x = -(ubic_proyector[0] + tiro[0]/2 - (1/2))
                objs3.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2  # Configura la ubicación Y aquí
                objs3.name = "Projector support 3"

            else: 
                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs2 = bpy.context.object
                objs2.location.z = 1.25 #1.60 dividido en 2
                objs2.location.x = ubic_proyector[0] + tiro[0]/2 - (1/2)  # Configura la ubicación Y aquí
                objs2.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2
                objs2.name = "Projector support 2"

                bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.4) #tripode desde piso
                objs3 = bpy.context.object
                objs3.location.z = 1.25 #1.60 dividido en 2
                objs3.location.x = -(ubic_proyector[0] + tiro[0]/2 - (1/2))
                objs3.location.y = ubic_proyector[1] - tiro[0] + (3**0.5)/2 # Configura la ubicación Y aquí
                objs3.name = "Projector support 3"

            # Editar posicion de un objeto de la colección

            nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion1 = (vertice_1[0] + (length_m/2),vertice_1[1] - (width_m/2), 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion2 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion3 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar4 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion4 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar5 = "Projector 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion5 = (ubic_proyector[0] - 1, ubic_proyector[1] - tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar6 = "Projector 3"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion6 = (ubic_proyector[0] + 1,ubic_proyector[1] - tiro[0]*2, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            if height_m > 3.35:
                nombre_objeto_reposicionar7 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar8 = "Projector support 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (ubic_proyector[0] - 1, ubic_proyector[1] - tiro[0], ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Projector support 3"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (ubic_proyector[0] + 1, ubic_proyector[1] - tiro[0]*2, ubic_proyector[2] - 1.2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)
            

            else:
                nombre_objeto_reposicionar7 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (ubic_proyector[0], ubic_proyector[1] + tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar8 = "Projector support 2"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (ubic_proyector[0] - 1, ubic_proyector[1] - tiro[0], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Projector support 3"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (ubic_proyector[0] + 1, ubic_proyector[1] - tiro[0]*2, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #Reposición de sistema de tracking

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            
            if support_projectorA:
                nombre_objeto_reposicionar10 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion10 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)
                reposicionar_objeto(nombre_objeto_reposicionar10, nueva_posicion10)

            if support_projectorB:
                nombre_objeto_reposicionar10 = "Camera 1 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion10 = (pos_pm[0] + 1, pos_pm[1] + 1, new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar11 = "Camera 2 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion11 = (pos_pm[0] - 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar12 = "Camera 3 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion12 = (pos_pm[0] + 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar13 = "Camera 4 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion13 = (pos_pm[0] - 1,pos_pm[1] + 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)
                reposicionar_objeto(nombre_objeto_reposicionar10, nueva_posicion10)
                reposicionar_objeto(nombre_objeto_reposicionar11, nueva_posicion11)
                reposicionar_objeto(nombre_objeto_reposicionar12, nueva_posicion12)
                reposicionar_objeto(nombre_objeto_reposicionar13, nueva_posicion13)


            #Definir posicion del PM para posteriormente añadir el tracking

            pos_pm.clear()
            pos_pm.append(vertice_1[0] + (length_m/2)) #x
            pos_pm.append(vertice_1[1] - (width_m/2)) #y
            pos_pm.append(new_z_position2) #z
            
        else:
            return {'CANCELLED'}


        # Limpiar la lista antes de agregar el nuevo valor
        cant_p_def.clear()

        # Agregar el último valor a la lista
        cant_p_def.append(insumo51)
        cant_p_def.append(insumo52)

        #Diseño_final.append(insumo2)

        texto_a_eliminar = "Number of people"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #Verificar

        #print(veloc_sinc_def)
        #print(Brightness_def)
        #print(Sharpness_def)
        #print(cant_p_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}

### OPERADOR PARA DEFINIR PR Movement of the mixed prototype ### ----------------------------------------------------------------------------

class SetNumberOperator6(bpy.types.Operator):
    bl_idname = "object.set_number6"
    bl_label = "Movement of augmented object in space"
    bl_description = "It refers to the level of movement of the mixed prototype through space"
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Movement level",
        description="It refers to the level of movement of the mixed prototype through space. Select the most representative option for your requirement.",
        items=[
            ('1', "Motionless", "Does not require tracking system"),
            ('2', "Over the surface", "There is short rotational and translational movement within the space"),
            ('3', "Free movement", "There is extensive rotational and translational movement within the space"),
        ],
        default='2'
    )

    #mov_gir: bpy.props.BoolProperty(
        #name="Consider using a rotating platform?",
        #description="Enable to include rotating platform",
        #default=False,
    #)

    def execute(self, context):
        #mov_gir = self.mov_gir

        # Obtener el número de la opción seleccionada
        if self.options == '1':
            number6 = mov_pm[1]
            insumo6 = 'Does not include tracking system'

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            

            if support_projectorA:
                bpy.data.objects.remove(support_projectorA)

            if support_projectorB:
                bpy.data.objects.remove(support_projectorB)
                bpy.data.objects.remove(support_projectorC)
                bpy.data.objects.remove(support_projectorD)
                bpy.data.objects.remove(support_projectorE)

            print(pos_pm)


        elif self.options == '2':
            number6 = mov_pm[2]
            insumo6 = 'All-in-one system'

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            

            if support_projectorA:
                bpy.data.objects.remove(support_projectorA)

            if support_projectorB:
                bpy.data.objects.remove(support_projectorB)
                bpy.data.objects.remove(support_projectorC)
                bpy.data.objects.remove(support_projectorD)
                bpy.data.objects.remove(support_projectorE)

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Verificamos si las dimensiones del PM fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length3_m, width3_m, height3_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            # Obtener la ubicación del objeto previo seleccionado (Parallelepiped creado anteriormente)
            parallelepiped_obj = bpy.context.active_object

            if parallelepiped_obj and parallelepiped_obj.type == 'MESH':
                # Obtener la ubicación del objeto previo seleccionado
                parallelepiped_location = parallelepiped_obj.location.copy()
                    
                # Dimensiones del nuevo paralelepípedo (sistema de tracking de barra)
                new_length_m2 = 0.279
                new_width_m2 = 0.051
                new_height_m2 = 0.041

                # Calcular la posición Z del nuevo objeto (160 cm)
                if height_m < 2.5:
                    new_z_position2 = 1.6
                else:
                    new_z_position2 = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

                # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
                custom_parallelepiped1_obj2 = bpy.data.objects.get("All-in-one system")

                if custom_parallelepiped1_obj2:
                    bpy.data.objects.remove(custom_parallelepiped1_obj2)

                # Crear los vértices del Parallelepiped como se hace originalmente
            
                vertices = [
                (-new_length_m2 / 2, -new_width_m2 / 2, 0),     # Vértice 0
                (-new_length_m2 / 2, new_width_m2 / 2, 0),      # Vértice 1
                (new_length_m2 / 2, new_width_m2 / 2, 0),       # Vértice 2
                (new_length_m2 / 2, -new_width_m2 / 2, 0),      # Vértice 3
                (-new_length_m2 / 2, -new_width_m2 / 2, -new_height_m2),   # Vértice 4
                (-new_length_m2 / 2, new_width_m2 / 2, -new_height_m2),    # Vértice 5
                (new_length_m2 / 2, new_width_m2 / 2, -new_height_m2),     # Vértice 6
                (new_length_m2 / 2, -new_width_m2 / 2, -new_height_m2),     # Vértice 7 
                ]


                # Crear las caras del Parallelepiped
                faces = [
                    (0, 1, 2, 3),    # Cara inferior
                    (4, 7, 6, 5),    # Cara superior
                    (0, 4, 5, 1),    # Cara lateral 1
                    (1, 5, 6, 2),    # Cara lateral 2
                    (2, 6, 7, 3),    # Cara lateral 3
                    (3, 7, 4, 0)     # Cara lateral 4
                    ]

                # Crear el objeto malla en Blender
                mesh2 = bpy.data.meshes.new("All-in-one system")
                mesh2.from_pydata(vertices, [], faces)
                mesh2.update()

                # Crear el objeto de Cube en la escena de Blender
                obj2 = bpy.data.objects.new("All-in-one system", mesh2)

                # Crear un nuevo material con el nombre "Red material"
                material_rojo = bpy.data.materials.new(name="Red material")
                material_rojo.use_nodes = False  # Deshabilitar nodos para el material simple

                # Configurar el color rojo para el material
                material_rojo.diffuse_color = (0.8, 0.2, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

                # Asignar el material al objeto
                obj2.data.materials.append(material_rojo)

                #POSICION DE LA BARRA:Se ponen las coordenadas guardadas en la lista de las coordenadas del PM hechas con el operador de la cantidad de personas
                obj2.location = (pos_pm[0], pos_pm[1], new_z_position2)
                context.collection.objects.link(obj2)

                print(pos_pm)


        elif self.options == '3':
            number6 = mov_pm[3]
            insumo6 = 'Multi - camera system'

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            

            if support_projectorA:
                bpy.data.objects.remove(support_projectorA)

            if support_projectorB:
                bpy.data.objects.remove(support_projectorB)
                bpy.data.objects.remove(support_projectorC)
                bpy.data.objects.remove(support_projectorD)
                bpy.data.objects.remove(support_projectorE)

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Verificamos si las dimensiones del PM fueron guardadas previamente
            if OBJECT_OT_create_parallelepiped.created_dimensionsPM is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length3_m, width3_m, height3_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

            # Obtener la ubicación del objeto previo seleccionado (Parallelepiped creado anteriormente)
            parallelepiped_obj = bpy.context.active_object

            # Obtener la ubicación del objeto previo seleccionado (Cube creado anteriormente)
            cube_obj = bpy.context.active_object

            if cube_obj and cube_obj.type == 'MESH':
                # Obtener la ubicación del objeto previo seleccionado
                cube_location = cube_obj.location.copy()
                    
                # Dimensiones del nuevo Parallelepiped (sistema de tracking cámara)
                new_length_m2 = 0.069
                new_width_m2 = 0.053
                new_height_m2 = 0.069

                # Calcular la posición Z del nuevo objeto (160 cm)
                if height_m < 2.5:
                    new_z_position2 = 1.6
                else:
                    new_z_position2 = 2.5 #se refiere a la altura del proyector ya sea del techo o desde el piso

                # Buscar si el objeto "Parallelepiped" ya existe en la colección de objetos de Blender
                custom_parallelepiped1_obj2 = bpy.data.objects.get("Camera 1 tracking system")
                custom_parallelepiped1_obj3 = bpy.data.objects.get("Camera 2 tracking system")
                custom_parallelepiped1_obj4 = bpy.data.objects.get("Camera 3 tracking system")
                custom_parallelepiped1_obj5 = bpy.data.objects.get("Camera 4 tracking system")

                if custom_parallelepiped1_obj2:
                    bpy.data.objects.remove(custom_parallelepiped1_obj2)
                    bpy.data.objects.remove(custom_parallelepiped1_obj3)
                    bpy.data.objects.remove(custom_parallelepiped1_obj4)
                    bpy.data.objects.remove(custom_parallelepiped1_obj5)

                # Crear los vértices del Parallelepiped como se hace originalmente
            
                vertices = [
                (-new_length_m2 / 2, -new_width_m2 / 2, 0),     # Vértice 0
                (-new_length_m2 / 2, new_width_m2 / 2, 0),      # Vértice 1
                (new_length_m2 / 2, new_width_m2 / 2, 0),       # Vértice 2
                (new_length_m2 / 2, -new_width_m2 / 2, 0),      # Vértice 3
                (-new_length_m2 / 2, -new_width_m2 / 2, -new_height_m2),   # Vértice 4
                (-new_length_m2 / 2, new_width_m2 / 2, -new_height_m2),    # Vértice 5
                (new_length_m2 / 2, new_width_m2 / 2, -new_height_m2),     # Vértice 6
                (new_length_m2 / 2, -new_width_m2 / 2, -new_height_m2),     # Vértice 7 
                ]


                # Crear las caras del Parallelepiped
                faces = [
                    (0, 1, 2, 3),    # Cara inferior
                    (4, 7, 6, 5),    # Cara superior
                    (0, 4, 5, 1),    # Cara lateral 1
                    (1, 5, 6, 2),    # Cara lateral 2
                    (2, 6, 7, 3),    # Cara lateral 3
                    (3, 7, 4, 0)     # Cara lateral 4
                    ]

                # Crear el objeto malla en Blender
                mesh2 = bpy.data.meshes.new("Camera 1 tracking system")
                mesh2.from_pydata(vertices, [], faces)
                mesh2.update()


                # Crear los objetos de Cube en la escena de Blender
                obj2 = bpy.data.objects.new("Camera 1 tracking system", mesh2)
                obj3 = bpy.data.objects.new("Camera 2 tracking system", mesh2)
                obj4 = bpy.data.objects.new("Camera 3 tracking system", mesh2)
                obj5 = bpy.data.objects.new("Camera 4 tracking system", mesh2)

                # Crear un nuevo material con el nombre "Red material"
                material_rojo = bpy.data.materials.new(name="Red material")
                material_rojo.use_nodes = False  # Deshabilitar nodos para el material simple

                # Configurar el color rojo para el material
                material_rojo.diffuse_color = (0.8, 0.2, 0.2, 1.0)  # R, G, B, Alpha (todos en el rango de 0.0 a 1.0)

                # Asignar el material al objeto
                obj2.data.materials.append(material_rojo)
                obj3.data.materials.append(material_rojo)
                obj4.data.materials.append(material_rojo)
                obj5.data.materials.append(material_rojo)

                # Calcular las coordenadas para ubicar los Cubes en esquinas distintas
                cube_dimensions = (new_length_m2, new_width_m2, new_height_m2)
                space_dimensions = (length_m, width_m, height_m)
            
                # Asignar las ubicaciones de los objetos (este paso ya no es necesario pq ahora el reorden de las camaras se hace en un operador posterior)

                #if angulo[0] == '180': #Para que las camaras queden dentro de la sala
                    #obj2.location = (pos_pm[0] + 0.2, pos_pm[1] - 1, new_z_position2 + 0.5)
                    #context.collection.objects.link(obj2)

                    #obj3.location = (pos_pm[0] + 0.2, pos_pm[1] - 1,new_z_position2)
                    #context.collection.objects.link(obj3)

                    #obj4.location = (pos_pm[0] + 1, pos_pm[1] + 0.2,new_z_position2)
                    #context.collection.objects.link(obj4)

                    #obj5.location = (pos_pm[0] + 1,pos_pm[1] + 0.2,new_z_position2)
                    #context.collection.objects.link(obj5)

                #else:
                obj2.location = (pos_pm[0] + 1, pos_pm[1] + 1, new_z_position2 - 0.1)
                context.collection.objects.link(obj2)

                obj3.location = (pos_pm[0] - 1, pos_pm[1] - 1,new_z_position2 - 0.1)
                context.collection.objects.link(obj3)

                obj4.location = (pos_pm[0] + 1, pos_pm[1] - 1,new_z_position2 - 0.1)
                context.collection.objects.link(obj4)

                obj5.location = (pos_pm[0] - 1,pos_pm[1] + 1,new_z_position2 - 0.1)
                context.collection.objects.link(obj5)

                #print(pos_pm)


        else:
            return {'CANCELLED'}

        # Limpiar la lista antes de agregar el nuevo valor
        mov_pm_def.clear()

        # Agregar el último valor a la lista
        mov_pm_def.append(insumo6)
        
        # Realizar una acción adicional si el checkbox está activado
        #if mov_gir:
            #mov_pm_def.append('Type of rotating support')
        #else:
            #mov_pm_def.append('Type of static support')

        # Actualizar espacio de diseño
        texto_a_eliminar = "Movement of the mixed prototype"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #Verificar

        #print(veloc_sinc_def)
        #print(Brightness_def)
        #print(Sharpness_def)
        #print(cant_p_def)
        #print(mov_pm_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}



### OPERADOR PARA DEFINIR PR Interaction with the digital model (ACTUALIZADO) ---------------------------------------------------

class SetNumberOperator7(bpy.types.Operator):
    bl_idname = "object.set_number7"
    bl_label = "Interaction with digital modeling"
    bl_description = "It refers to the number of designers who are responsible for generating the changes in the design of the mixed prototype through the editing software during a co-design session"
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="UI devices",
        description= "It refers to the number of designers that will be in charge of generating the changes in the design of the mixed prototype through the editing software during a co-design session. Select the most representative option for your requirement.",
        items=[
            ('LIMITED', "Static user interface", "2 or 3 designers are in charge of modifying the digital modeling"),
            ('FLEXIBLE', "Mobile user interface", "More than 3 designers are in charge of modifying the digital modeling")
        ],
        default='FLEXIBLE'
        )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == 'LIMITED':
            number7 = imd[1]
            insumo7 = 'Computer monitor'
        elif self.options == 'FLEXIBLE':
            number7 = imd[2]
            insumo7 = 'Computer monitor + Device with touch screen'
        else:
            return {'CANCELLED'}

        # Limpiar la lista antes de agregar el nuevo valor
        imd_def.clear()

        # Agregar el último valor a la lista
        imd_def.append(insumo7)

        texto_a_eliminar = "Interaction with the digital model"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}

### OPERADOR PARA DEFINIR PR Augmented object placement (180 grados) -----------------------------------------------------------

class SetNumberOperator8(bpy.types.Operator):
    bl_idname = "object.set_number8"
    bl_label = "System placement"
    bl_description = "Refers to the type of configurations of the mixed prototyping system available for visualization in space"
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="Augmented object placement",
        description="It refers to the number of configurations of the mixed prototyping system available for visualization in space. Select the most representative option for your requirement.",
        items=[
            ('Centered', "Centered", "The projection of the mixed prototype is located in the center of the room."),
            ('In the corner', "In the corner", "The projection of the mixed prototype is located in the corner of the room.")
        ],
        default='In the corner'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == 'Centered':
            number8 = variedad_conf[1]
            insumo8 = 'Centered'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Calcular la posición Z del nuevo objeto
            new_z_position2 = height_m

            # Editar posicion de un objeto de la colección

            nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion1 = (vertice_1[0] + (length_m/2),vertice_1[1] - (width_m/2), 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion2 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion3 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar4 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion4 = (ubic_proyector[0], ubic_proyector[1], ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #reposición de soportes del proyector

            if height_m > 3.35:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0], ubic_proyector[1], ubic_proyector[2] - 1.2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            else:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0], ubic_proyector[1], ubic_proyector[2] + 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #Reposición de sistema de tracking

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            
            if support_projectorA:
                nombre_objeto_reposicionar6 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (vertice_1[0] + (length_m/2), vertice_1[1] - (width_m/2), new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)

            if support_projectorB:
                nombre_objeto_reposicionar6 = "Camera 1 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (pos_pm[0] + 1, pos_pm[1] + 1, new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar7 = "Camera 2 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (pos_pm[0] - 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar8 = "Camera 3 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 = (pos_pm[0] + 1, pos_pm[1] - 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Camera 4 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (pos_pm[0] - 1,pos_pm[1] + 1,new_z_position2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)

            #Definir posicion del PM para posteriormente añadir el tracking

            pos_pm.clear()
            pos_pm.append(vertice_1[0] + (length_m/2)) #x
            pos_pm.append(vertice_1[1] - (width_m/2)) #y
            pos_pm.append(new_z_position2) #z


            bpy.ops.object.set_number6() #solucion de error de que tracking se va muy arriba

        elif self.options == 'In the corner':
            number8 = variedad_conf[2]
            insumo8 = 'In the corner'

            # Verificamos si las dimensiones del espacio fueron guardadas previamente
            if CreateCubeOperator.created_dimensionsCube is None:
                return {'CANCELLED'}

            # Obtenemos las dimensiones del objeto previamente creado
            length_m, width_m, height_m = CreateCubeOperator.created_dimensionsCube

            # Calcular la posición Z del nuevo objeto
            new_z_position2 = height_m

            # Editar posicion de un objeto de la colección

            nombre_objeto_reposicionar1 = "Cilindro"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion1 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.375)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar2 = "Cilindro.001"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion2 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.825)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar3 = "Parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion3 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, 0.85)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            nombre_objeto_reposicionar4 = "Custom parallelepiped"  # Reemplaza con el nombre del objeto que deseas reposicionar
            nueva_posicion4 = (ubic_proyector[0] - 0.5, ubic_proyector[1] + 0.5, ubic_proyector[2])  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #Reposición de soportes de proyector

            if height_m > 3.35:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0] - 0.5, ubic_proyector[1] + 0.5, ubic_proyector[2] - 1.2 - 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            else:
                nombre_objeto_reposicionar5 = "Projector support"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion5 = (ubic_proyector[0] - 0.5, ubic_proyector[1] + 0.5, ubic_proyector[2]+ 0.1)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

            #Reposición del sistema de tracking

            # Buscar si el objeto "Tracking" ya existe en la colección de objetos de Blender
            support_projectorA = bpy.data.objects.get("All-in-one system")
            support_projectorB = bpy.data.objects.get("Camera 1 tracking system")
            support_projectorC = bpy.data.objects.get("Camera 2 tracking system")
            support_projectorD = bpy.data.objects.get("Camera 3 tracking system")
            support_projectorE = bpy.data.objects.get("Camera 4 tracking system")
            
            if support_projectorA:
                nombre_objeto_reposicionar6 = "All-in-one system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (vertice_1[0] + 0.5, vertice_1[1] - 0.5, new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
    

            if support_projectorB:
                nombre_objeto_reposicionar6 = "Camera 1 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion6 = (pos_pm[0] + 0.25, pos_pm[1] - 1, new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar7 = "Camera 2 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion7 = (pos_pm[0] + 0.5, pos_pm[1] - 0.75,new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar8 = "Camera 3 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion8 =  (pos_pm[0] + 0.75, pos_pm[1] - 0.5,new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                nombre_objeto_reposicionar9 = "Camera 4 tracking system"  # Reemplaza con el nombre del objeto que deseas reposicionar
                nueva_posicion9 = (pos_pm[0] + 1,pos_pm[1] - 0.25,new_z_position2)  # Reemplaza con las nuevas coordenadas de posición (x, y, z)

                reposicionar_objeto(nombre_objeto_reposicionar1, nueva_posicion1)
                reposicionar_objeto(nombre_objeto_reposicionar2, nueva_posicion2)
                reposicionar_objeto(nombre_objeto_reposicionar3, nueva_posicion3)
                reposicionar_objeto(nombre_objeto_reposicionar4, nueva_posicion4)
                reposicionar_objeto(nombre_objeto_reposicionar5, nueva_posicion5)
                reposicionar_objeto(nombre_objeto_reposicionar6, nueva_posicion6)
                reposicionar_objeto(nombre_objeto_reposicionar7, nueva_posicion7)
                reposicionar_objeto(nombre_objeto_reposicionar8, nueva_posicion8)
                reposicionar_objeto(nombre_objeto_reposicionar9, nueva_posicion9)
                

            #Definir posicion del PM para posteriormente añadir el tracking

            pos_pm.clear()
            pos_pm.append(vertice_1[0] + 0.5) #x
            pos_pm.append(vertice_1[1] - 0.5) #y
            pos_pm.append(0.85) #z

            bpy.ops.object.set_number6()

            
        else:
            return {'CANCELLED'}

        # Ocultar colección original
        #nombre_coleccion = "Configuration 2"
        #ocultar_coleccion(nombre_coleccion)

        # Limpiar la lista antes de agregar el nuevo valor
        variedad_conf_def.clear()

        # Agregar el último valor a la lista
        variedad_conf_def.append(insumo8)

        texto_a_eliminar = "Augmented object placement"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}



### OPERADOR PARA DEFINIR PR Augmented object placement (360 grados) -----------------------------------------------------------

class SetNumberOperator9(bpy.types.Operator):
    bl_idname = "object.set_number9"
    bl_label = "Augmented object placement"
    bl_description = "Refers to the type of configurations of the mixed prototyping system available for visualization in space"
    bl_options = {'REGISTER', 'UNDO'}

    options: bpy.props.EnumProperty(
        name="AO Placement",
        description="It refers to the number of configurations of the mixed prototyping system available for visualization in space. Select the most representative option for your requirement.",
        items=[
            ('Centered', "Centered", "A final configuration version of the mixed prototyping system in space is presented"),
        ],
        default='Centered'
    )

    def execute(self, context):
        # Obtener el número de la opción seleccionada
        if self.options == 'Centered':
            number8 = variedad_conf[1]
            insumo8 = 'Centered'

            #Eliminar colecciones si es que ya existian
            nombre_coleccion_a_eliminar1 = "Configuration 1"  # Reemplaza con el nombre de la colección que deseas eliminar
            eliminar_coleccion(nombre_coleccion_a_eliminar1)
            nombre_coleccion_a_eliminar2 = "Configuration 2"  # Reemplaza con el nombre de la colección que deseas eliminar
            eliminar_coleccion(nombre_coleccion_a_eliminar2)

            nombre_coleccion_original = "Collection"  # Reemplaza con el nombre de tu colección original
            nombre_coleccion_destino = "Configuration 1"    # Reemplaza con el nombre de tu colección de destino

            duplicar_coleccion(nombre_coleccion_original, nombre_coleccion_destino)

            # Ocultar coleccion original
            nombre_coleccion = "Collection"

            ocultar_coleccion(nombre_coleccion)

        else:
            return {'CANCELLED'}

        # Limpiar la lista antes de agregar el nuevo valor
        variedad_conf_def.clear()

        # Agregar el último valor a la lista
        variedad_conf_def.append(insumo8)

        texto_a_eliminar = "Augmented object placement"

        eliminar_lista_por_texto(Espacio_diseño_act, texto_a_eliminar)

        #print(veloc_sinc_def)
        #print(Espacio_diseño_act)

        return {'FINISHED'}


### OPERADOR DE CIERRE --------------------------------------------------------------------------------------------------------

class FinalOperator(bpy.types.Operator):
    bl_idname = "object.final_operator"                                     # Nombre único del operador
    bl_label = "Final configuration of the mixed prototyping system"       # Etiqueta que se mostrará en el botón
    bl_description = "It defines the final inputs according to the customization made of the mixed prototyping system" # Opciones del operador
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # Agregar el último valor a la lista

        insumos = veloc_sinc_def + Brightness_def + Sharpness_def + proximidad_p_def + cant_p_def + mov_pm_def + imd_def + variedad_conf_def

        # Limpiar la lista antes de agregar el nuevo valor
        diseño_final.clear()

        # Agregar el último valor a la lista
        diseño_final.append(insumos[0])
        diseño_final.append(insumos[1])
        diseño_final.append(insumos[2])
        diseño_final.append(insumos[3])
        diseño_final.append(insumos[4])
        diseño_final.append(insumos[5])
        diseño_final.append(insumos[6])
        diseño_final.append(insumos[7])
        diseño_final.append(insumos[8])
        #diseño_final.append(insumos[9])

        print("DISEÑO FINAL: ")
        print(diseño_final)


        #Definición de listas finales
        propuesta_final = []
        propuesta_final_2 = []
        propuesta_final_3 = []

        #Definir modelos ideales junto a su precio
        propuesta_final.clear()
        propuesta_final_2.clear()
        propuesta_final_3.clear()

        #Generar listas globales para iteración de elementos
        banco_de_proyectores = [Proyector_1,Proyector_2,Proyector_3,Proyector_4,Proyector_5,Proyector_6,Proyector_7,Proyector_8,Proyector_9,Proyector_10,Proyector_11,Proyector_12,Proyector_13,Proyector_14,Proyector_15,Proyector_16,Proyector_17,Proyector_18,Proyector_19,Proyector_20,Proyector_21,Proyector_22,Proyector_23,Proyector_24,Proyector_25,Proyector_26,Proyector_27,Proyector_28,Proyector_29,Proyector_30,Proyector_31,Proyector_32,Proyector_33,Proyector_34,Proyector_35,Proyector_36,Proyector_37,Proyector_38,Proyector_39,Proyector_40,Proyector_41,Proyector_42,Proyector_43,Proyector_44,Proyector_45,Proyector_46,Proyector_47,Proyector_48,Proyector_49,Proyector_50,Proyector_51,Proyector_52,Proyector_53,Proyector_54]

        banco_de_tracking = [sist_t_1,sist_t_2,sist_t_3,sist_t_4,sist_t_5,sist_t_6]

        banco_pantalla_tactil = [tactil_1,tactil_2]

        #CASOS POSIBLES

        print(proximidad_p_def)
        print('/n')
        print(veloc_sinc_def)
        print('/n')
        print(Brightness_def)
        print('/n')
        print(Sharpness_def)



        #PROYECTORES
        for proyector1 in banco_de_proyectores:
            if proximidad_p_def[0] in proyector1:
                propuesta_final.append(proyector1)

            #for proyector2 in propuesta_final:
                #if veloc_sinc_def[0] in proyector2:
                    #pass
                #else:
                    #if len(propuesta_final) == 1:
                        #pass
                    #else:
                        #propuesta_final.remove(proyector2)


            for proyector3 in propuesta_final:
                if Brightness_def[0] in proyector3:
                    pass
                else:
                    if len(propuesta_final) == 1:
                        pass
                    else:
                        propuesta_final.remove(proyector3)

                
            for proyector4 in propuesta_final:
                if Sharpness_def[0] in proyector4:
                    pass
                else:
                    if len(propuesta_final) == 1:
                        pass
                    else:
                        propuesta_final.remove(proyector4)


        #SISTEMA DE TRACKING
        propuesta_final_2.append(sist_t_0)

        for tracking in banco_de_tracking:
            if mov_pm_def[0] in tracking:
                propuesta_final_2.append(tracking)

        #INTERACCIÓN CON EL USUARIO (PANTALLA TACTIL)
        if imd_def[0] == 'Computer monitor + Device with touch screen':
            for elemento in banco_pantalla_tactil:
                propuesta_final_3.append(elemento)
        else:
            propuesta_final_3.extend([["No additional touch screen to PC required",0,0]])


        #ORDENAR POR PRECIOS CLP
        propuesta_final = sorted(propuesta_final, key=lambda x: float(x[13]))
        propuesta_final_2 = sorted(propuesta_final_2,key=lambda x: x[0][2])
        propuesta_final_3 = sorted(propuesta_final_3,key=lambda x: x[0][2])


    
        #Calculo del presupuesto total CLP
        total_clp = propuesta_final[0][13] + propuesta_final_2[0][2] + propuesta_final_3[0][2] + sist_t_0[2]

        #Calculo del presupuesto total USD
        total_usd = propuesta_final[0][12] + propuesta_final_2[0][1] + propuesta_final_3[0][1] + sist_t_0[1]
        total_usd_round = round(total_usd,2)

        # Obtenemos las dimensiones del objeto previamente creado
        length2_m, width2_m, height2_m = OBJECT_OT_create_parallelepiped.created_dimensionsPM

        PM_width = width2_m

        print("Propuesta final: ")
        print(propuesta_final)
        print("INSUMOS: ")
        print(insumos)
        #print(propuesta_final[0][7])



        #IMPRIMIR EN LA CONSOLA LA INFORMACIÓN

        print("PROPOSAL OF IDEAL COMPONENTS FOR THE MIXED PROTOTYPING SYSTEM:"+"\n")
        print("\n")
        print("From the configuration made with the customization tool, the ideal inputs were defined to generate the mixed prototyping space, which will be shown below:"+"\n")
        print("\n")
        print("This selection of components was made based on the requirements chosen during the customization process, which can be summarized as follows:"+"\n"+"-"+" "+"Optimal luminance:"+" "+str(insumos[1])+"\n"+"-"+" "+"Minimum required lumens:"+" "+str(int(round(lumens_fin[0])))+" "+"lumens"+"\n"+"-"+" "+"Resolution:"+" "+str(insumos[2])+"\n"+"-"+" "+"Throw distance:"+" "+str(insumos[3])+"\n"+"-"+" "+"User vision coverage angle:"+" "+str(insumos[4])+"\n"+"-"+" "+"Number of projectors:"+" "+str(insumos[5])+"\n"+"-"+" "+"Tracking system type:"+ " "+str(insumos[6])+"\n"+"-"+" "+"User interface device:"+" " +str(insumos[7])+"\n"+"-"+" "+"Placement:"+ " " +str(insumos[8])+"\n")

        print("\n")
        print("The ideal projectors for your system are:"+"\n") 
        print("-"+" "+str(propuesta_final[0][0])+","+"Ideal projection distance: "+str((round(propuesta_final[0][7]* PM_width,2)))+"[m]"+ ","+"$"+str(propuesta_final[0][12])+" "+"USD"+","+"$"+str(propuesta_final[0][13])+" "+"CLP"+"[RECOMMENDED]"+"\n")

        for p in propuesta_final[1:]:
            print("-"+" "+p[0]+","+"Ideal projection distance: "+str((round(p[7]* PM_width,2)))+"[m]"+"$"+str(p[12])+" "+"USD"+","+"$"+str(p[13])+" "+"CLP"+"\n")
        
        print("\n")
        print("The ideal components for the tracking system are:"+"\n")
        print("-"+" "+str(propuesta_final_2[0][0])+","+"$"+str(propuesta_final_2[0][1])+" "+"USD"+","+"$"+str(propuesta_final_2[0][2])+" "+"CLP"+"[RECOMMENDED]"+"\n")
        
        for t in propuesta_final_2[1:]:
            print("-"+" "+t[0]+","+"$"+str(t[1])+" "+"USD"+","+"$"+str(t[2])+" "+"CLP"+"\n")

        print("\n")
        print("The ideal user interaction devices for your system are:"+"\n")
        print("-"+" "+str(propuesta_final_3[0][0])+","+"$"+str(propuesta_final_3[0][1])+" "+"USD"+","+"$"+str(propuesta_final_3[0][2])+" "+"CLP"+"[RECOMMENDED]"+"\n")

        for d in propuesta_final_3[1:]:
            print("-"+" "+d[0]+","+"$"+str(d[1])+" "+"USD"+","+"$"+str(d[2])+" "+"CLP"+"\n")

        print("\n")
        print("Therefore, the estimated budget to install the mixed prototyping system would be:"+" "+"$"+ str(total_usd_round)+" "+"USD"+" "+"o"+" "+ str(total_clp)+" "+"CLP"+"\n")
        print("\n")
        print("IMPORTANT: The value of the budget is an estimate, since prices may vary depending on the preferred distributor store"+"\n")
    

        print("\n")

        print("Thank you for using the Mixed Prototyping System Customization Tool!")


        #GENERAR ARCHIVO TXT CON LA INFORMACIÓN
        selected_obj = bpy.context.object.name
        full_file_name = bpy.data.filepath.split("\\")
        file_name = full_file_name[-1]
        
        blend_path = bpy.path.abspath(path = "//")
        txt_export_filepath = blend_path + "\\" + "Custom Mixed Prototyping System"  + ".txt"
        log = open(txt_export_filepath,"a")
        
        #TEXTOS CONTENIDOS EN EL ARCHIVO TXT
        log.write("PROPOSAL OF IDEAL COMPONENTS FOR THE MIXED PROTOTYPING SYSTEM:"+"\n")
        log.write("\n")
        log.write("This selection of components was made based on the requirements chosen during the customization process, which can be summarized as follows:"+"\n"+"-"+" "+"Optimal luminance:"+" "+str(insumos[1])+"\n"+"-"+" "+"Minimum required lumens:"+" "+str(int(round(lumens_fin[0])))+" "+"lumens"+"\n"+"-"+" "+"Resolution:"+" "+str(insumos[2])+"\n"+"-"+" "+"Throw distance:"+" "+str(insumos[3])+"\n"+"-"+" "+"User vision coverage angle:"+" "+str(insumos[4])+"\n"+"-"+" "+"Number of projectors:"+" "+str(insumos[5])+"\n"+"-"+" "+"Tracking system type:"+ " "+str(insumos[6])+"\n"+"-"+" "+"User interface device:"+" " +str(insumos[7])+"\n"+"-"+" "+"Placement:"+ " " +str(insumos[8])+"\n")

        log.write("\n")
        log.write("From the configuration made with the customization tool, the ideal inputs were defined to generate the mixed prototyping space, which will be shown below:"+"\n")
        log.write("\n")
        log.write("The ideal projectors for your system are:"+"\n") 
        log.write("-"+" "+str(propuesta_final[0][0])+ ","+"Ideal projection distance: "+str((round(propuesta_final[0][7]* PM_width,2)))+"[m]"+ ","+"$"+str(propuesta_final[0][12])+" "+"USD"+" "+"[RECOMMENDED]"+"\n")

        for p in propuesta_final[1:]:
            log.write("-"+" "+ p[0]+","+"Ideal projection distance: "+str((round(p[7]* PM_width,2)))+"[m]"+"$"+str(p[12])+" "+"USD"+"\n")
        
        log.write("\n")
        log.write("The ideal components for the tracking system are:"+"\n")
        log.write("-"+" "+str(propuesta_final_2[0][0])+","+"$"+str(propuesta_final_2[0][1])+" "+"USD"+" "+"[RECOMMENDED]"+"\n")
        
        for t in propuesta_final_2[1:]:
            log.write("-"+" "+t[0]+","+"$"+str(t[1])+" "+"USD"+","+"$"+str(t[2])+" "+"\n")

        log.write("\n")
        log.write("The ideal user interaction devices for your system are:"+"\n")
        log.write("-"+" "+str(propuesta_final_3[0][0])+","+"$"+str(propuesta_final_3[0][1])+" "+"USD"+"[RECOMMENDED]"+"\n")

        for d in propuesta_final_3[1:]:
            log.write("-"+" "+d[0]+","+"$"+str(d[1])+" "+"USD"+"\n")

        log.write("\n")
        log.write("Therefore, the estimated budget to install the mixed prototyping system would be:"+" "+"$"+ str(total_usd_round)+" "+"USD"+"\n")
        log.write("\n")
        log.write ("IMPORTANT: The value of the budget is an estimate, since prices may vary depending on the preferred distributor store"+"\n")
        log.write("\n")

        log.write("Thank you for using the Mixed Prototyping System Customization Tool!")
        
        log.close()

        return {'FINISHED'}


################################################### PANELES DE INTERACCIÓN ##############################################################################################

    
### 1ER PANEL DE INTERACCIÓN CON EL USUARIO (se posicionan los primeros elementos en el espacio)(LISTO) -----------------------
class VIEW3D_PT_Input_1(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Define the first elements of space"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        layout.label(text = "Save the file in your preferred folder before getting started.(Shift+Ctrl+S)",icon ='NEWFOLDER')
        layout.label(text = "To set the values, pull down the lower-left corner panel on the screen.",icon ='HELP')
        layout.label(text = "⟷ Drag to the left to have a better visualization of the panel")
        
        col.operator('object.create_cube',
            text='Dimensions of space',
            icon='LIGHTPROBE_CUBEMAP')

        col.operator('object.create_parallelepiped',
            text='Dimensions of the interactive area',
            icon='TOOL_SETTINGS')


        # Agregar propiedad personalizada para el número ingresado
        if len(tipos_tiros) == 1:
            layout.label(text = "Displays the available projector positions")
            props = col.operator('object.create_custom_parallelepiped1',
                text='Set projector distance',icon='RESTRICT_SELECT_OFF',
                )

        elif len(tipos_tiros) == 2:
            layout.label(text = "Displays the available projector positions")
            props = col.operator('object.create_custom_parallelepiped2',
                text='Set projector distance',icon='RESTRICT_SELECT_OFF',
                )

        elif len(tipos_tiros) == 3:
            layout.label(text = "Displays the available projector positions")
            props = col.operator('object.create_custom_parallelepiped3',
                text='Set projector distance',icon='RESTRICT_SELECT_OFF',
                )

        else:
            return None

        #Previsualización parcial
        layout.label(text = proximidad_p_def[0])

       #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')



### 3ER PANEL Brightness (se seleccionan DPs)(LISTO)  ----------------------------------------------------------------------------

class VIEW3D_PT_Input_2(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Projection brightness"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.set_number2',
            text='Assign value',
            icon='GREASEPENCIL')

        #Previsualización parcial
        layout.label(text = Brightness_def[0])

        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')

### 4TO PANEL Sharpness (se seleccionan DPs)(LISTO)  ----------------------------------------------------------------------------

class VIEW3D_PT_Input_3(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Projection sharpness"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.set_number3',
            text='Assign value',
            icon='GREASEPENCIL')

        #Previsualización parcial
        layout.label(text = Sharpness_def[0])
        
        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')

### 2DO PANEL DE INTERACCIÓN CON EL USUARIO (se seleccionan DPs)(LISTO) -------------------------------------------------------

#class VIEW3D_PT_Input_4(bpy.types.Panel):
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "UI"
    #bl_category = "Customize Mixed Prototyping System"
    #bl_label = "Sync speed"

    #def draw(self, context):
        #layout = self.layout
        #layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        #col = layout.column(align=True)
        #col.label(text="Define the design parameter:") #icon='OUTLINER_OB_MESH'

        # Agregar propiedad personalizada para el número ingresado
        #props = col.operator('object.set_number',
            #text='Assign value',
            #icon='GREASEPENCIL')

        #Previsualización parcial
        #layout.label(text = veloc_sinc_def[0])

        #Indicación ir al segundo panel
        #layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')

### 6TO PANEL Number of people (se seleccionan DPs)(LISTO)  --------------------------------------------------------------

class VIEW3D_PT_Input_6(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Coverage angle"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.set_number5',
            text='Assign value',
            icon='GREASEPENCIL')

        #Previsualización parcial
        col.label(text = cant_p_def[0])
        col.label(text = cant_p_def[1])

        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')


### 7MO PANEL MOVIMIENTO DEL PROTOTIPO MIXTO (se seleccionan DPs)(Influye en configuraciones) ---------------------------------

class VIEW3D_PT_Input_7(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Movement of augmented object"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.set_number6',
            text='Assign value',
            icon='GREASEPENCIL')

        #Previsualización parcial
        col.label(text = mov_pm_def[0])
        #col.label(text = mov_pm_def[1])

        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')



### 8VO PANEL Interaction with the digital model (se seleccionan DPs)  ---------------------------------------------------------

class VIEW3D_PT_Input_8(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Interaction with the digital model"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.set_number7',
            text='Assign value',
            icon='GREASEPENCIL')

        #Previsualización parcial
        layout.label(text = imd_def[0])

        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')

### 9NO PANEL DE INTERACCIÓN CON EL USUARIO (se seleccionan DPs) --------------------------------------------------------------

class VIEW3D_PT_Input_9(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Augmented object placement"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "To define the values, pull down the panel located in the lower left corner of the screen",icon ='HELP')

        col = layout.column(align=True)
        col.label(text="Define the design parameter:")

        # Filtrar según la dependencia del angulo de visión
        if angulo[0] == '180':
            layout.label(text = "Display the available configurations")
            props = col.operator('object.set_number8',
                text='Select placement',icon='GREASEPENCIL',
                )
            #layout.label(text = "In 'Scene Collections', turn off the view of 'Settings 1' to only show 'Settings 2' and vice versa.",icon ='HIDE_OFF')

        elif angulo[0] == '360':
            layout.label(text = "Display the available configurations")
            props = col.operator('object.set_number9',
                text='Select placement',icon='GREASEPENCIL',
                )

        else:
            None

        #Previsualización parcial
        layout.label(text = variedad_conf_def[0])

        #Indicación ir al segundo panel
        layout.label(text="Ready? Go to the next panel", icon='SCREEN_BACK')

### 10MO PANEL DE INTERACCIÓN CON EL USUARIO ---------------------------------------------------------------------------------

class VIEW3D_PT_Input_10(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Customize Mixed Prototyping System"
    bl_label = "Final configuration"

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        # Agregar propiedad personalizada para el número ingresado
        props = col.operator('object.final_operator',
            text='Discover the ideal configuration for your space!',
            icon='GREASEPENCIL')

         # Visualización de la respuesta
        col.label(text="Ready!",icon = "CHECKMARK")
        col.label(text="Access the file 'Custom Mixed Prototyping System.txt' generated in the save folder of this same Blender file to see the ideal configuration of the mixed prototyping system for your space.",icon = 'FILE_FOLDER')
        col.label(text="Summary of Selected Requirements:")
        #col.label(text= diseño_final[0])
        col.label(text= diseño_final[1])
        col.label(text= diseño_final[2])
        col.label(text= diseño_final[3])
        col.label(text= diseño_final[4])
        col.label(text= diseño_final[5])
        col.label(text= diseño_final[6])
        col.label(text= diseño_final[7])
        col.label(text= diseño_final[8])
        #col.label(text= diseño_final[9])
        col.label(text="Thank you for using the Mixed Prototyping System Customization Tool!")

### Definir las clases y registrarlas (Funciones register y unregister)

classes = (
    CreateTableOperator,
    CreateCubeOperator,
    OBJECT_OT_create_parallelepiped,
    VIEW3D_PT_Input_1,
    VIEW3D_PT_Input_2,
    VIEW3D_PT_Input_3,
    VIEW3D_PT_Input_6,
    VIEW3D_PT_Input_7,
    VIEW3D_PT_Input_8,
     VIEW3D_PT_Input_9,
    VIEW3D_PT_Input_10,
    SetNumberOperator,
    SetNumberOperator2,
    SetNumberOperator3,
    SetNumberOperator5,
    SetNumberOperator6,
    SetNumberOperator7,
    SetNumberOperator8,
    SetNumberOperator9,
    FinalOperator,
    CreateCustomParallelepipedOperator1,
    CreateCustomParallelepipedOperator2,
    CreateCustomParallelepipedOperator3,
)

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_create_parallelepiped.bl_idname)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

#Esto le permite ejecutar el script directamente desde el editor de texto de Blender.
#Para probar el complemento sin tener que instalarlo.
if __name__ == "__main__":
    register()
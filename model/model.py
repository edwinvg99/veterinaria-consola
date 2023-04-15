from datetime import date

class Persona:
    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad

class Mascota:
    def __init__(self, id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso):
        self.id = id
        self.nombre = nombre
        self.cedula_dueno = cedula_dueno
        self.edad = edad
        self.especie = especie
        self.raza = raza
        self.caracteristicas = caracteristicas
        self.peso = peso

class usuario:
    def __init__(self, username, password,rol):
        self.username = username
        self.password = password
        self.rol = rol

class HistoriaClinica:
    def __init__(self,id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento):
        self.id_mascota=id_mascota
        self.fecha = fecha
        self.medico = medico
        self.motivo_consulta = motivo_consulta
        self.sintomatologia = sintomatologia
        self.diagnostico = diagnostico
        self.procedimiento = procedimiento
        self.medicamento = medicamento
        self.dosis = dosis
        self.id_orden = id_orden
        self.historial_vacunacion = historial_vacunacion
        self.alergias = alergias
        self.detalle_procedimiento = detalle_procedimiento

class Orden:
    def __init__(self, id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis,estado):
        self.id_orden = id_orden
        self.id_mascota = id_mascota
        self.cedula_dueno = cedula_dueno
        self.cedula_veterinario = cedula_veterinario
        self.medicamento = medicamento
        self.dosis = dosis
        self.fecha_generacion = date.today()
        self.estado=estado

class FacturaVenta:
    def __init__(self, id_factura, id_orden, nombre_producto, valor, cantidad):
        self.id_factura = id_factura
        self.id_orden = id_orden
        self.nombre_producto = nombre_producto
        self.valor = valor
        self.cantidad = cantidad
        self.fecha =  date.today()
        self.precio_total = self.valor*self.cantidad


class Factura_sin_orden:
    def __init__(self, id_factura,id_cliente, nombre_producto, valor, cantidad):
        self.id_factura = id_factura
        self.id_cliente = id_cliente
        self.nombre_producto = nombre_producto
        self.valor = valor
        self.cantidad = cantidad
        

        
class Veterinaria:
    def __init__(self):
        self.personas = []
        self.mascotas = []
        self.historiasClinicas = {}
        self.ordenes = []
        self.facturas_ventas = []
        self.facturas_sin_ordenes=[]
        
        self.Usuarios = []
        
        administrador=usuario("admin","pass","administrador")
        self.Usuarios.append(administrador)
        
        veterinario=usuario("vete","1234","veterinario")
        self.Usuarios.append(veterinario)
        
        vendedor=usuario("vende","1234","Vendedor")
        self.Usuarios.append(vendedor)
        
        self.usuario_actual = None

        persona_dueño= Persona("100", "andrea", "45")
        self.personas.append(persona_dueño)
        
        mascota_nueva=Mascota('200','perla',100,10,'perro','doberman','negro','15')
        self.mascotas.append(mascota_nueva)
        
        mascota_nueva=Mascota('201','pepe',100,10,'gato','peludo','blanco','8')
        self.mascotas.append(mascota_nueva)


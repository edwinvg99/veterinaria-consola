
from model import model
from controller import inputs
from controller import business
from datetime import datetime

Veterinaria1=model.Veterinaria()

def menu(usuario_actual):
    while True:
        print('')
        print("-----------------------------------------------")
        print("             Bienvenido a la Veterinaria         ")
        print("-----------------------------------------------")
        print(f"     Bienvenido al menú de {usuario_actual.rol}")
        print('')
        
        
        
        if usuario_actual.rol == "administrador":
            print("1. Registrar Persona")
            print("2. Registrar mascota")






        if usuario_actual.rol == "veterinario":
            print("1. Registrar historia clínica")
            print("2. Consultar historial clínico")
            print("3. Crear orden")
            print("4. Anular orden")



        if usuario_actual.rol == "Vendedor":
            print("1. Vender producto (sin orden)")
            print("2. Vender medicamento (con orden)")


            
        if usuario_actual.rol == "Vendedor" or usuario_actual.rol == "veterinario":
            print("5. Consultar ordenes")


    


            
        if usuario_actual.rol == "Vendedor" or usuario_actual.rol == "veterinario" or usuario_actual.rol== "administrador":
            print("10. Cerrar sesion")
            print("0. Salir")
        print()
        opcion = input("Ingrese una opción: ")
        print()

        if opcion == "1" and usuario_actual.rol == "administrador":
            
            cedula= input('Ingrese la cedula: ')
            nombre= input('Ingrese el nombre: ')
            edad= input('Ingrese la edad: ')

            inputs.ValidarRegistrar_Persona(cedula,nombre,edad,Veterinaria1)


        elif opcion == "2" and usuario_actual.rol == "administrador":
            
            id = input("Ingrese el ID de la mascota: ")
            nombre = input("Ingrese el nombre de la mascota: ")
            cedula_dueno = input("Ingrese la cédula del dueño: ")
            edad = input("Ingrese la edad de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            raza = input("Ingrese la raza de la mascota: ")
            caracteristicas = input("Ingrese las características de la mascota: ")
            peso = input("Ingrese el peso de la mascota en kilos: ")
            historia_clinica = {}
            
            inputs.ValidarRegistrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,Veterinaria1)



        elif opcion == "1" and usuario_actual.rol == "veterinario":
            
                id_mascota=input("Ingreas el id de la mascota: ")

                ahora = datetime.now()
                fecha = ahora.strftime("%Y-%m-%d %H:%M")
                #fecha =datetime.now().strftime("%Y-%m-%d") #arreglar, la fecha debe ser automatica
                medico = input("Ingrese el nombre del médico: ")
                motivo_consulta = input("Ingrese el motivo de consulta: ")
                sintomatologia = input("Ingrese la sintomatología: ")
                diagnostico = input("Ingrese el diagnóstico: ")
                procedimiento = input("Ingrese el procedimiento: ")
                medicamento = input("Ingrese el medicamento: ")
                dosis = input("Ingrese la dosis: ")
                id_orden = input("Ingrese el ID de la orden: ")
                historial_vacunacion = input("Ingrese el historial de vacunación: ")
                alergias = input("Ingrese las alergias: ")
                detalle_procedimiento = input("Ingrese el detalle del procedimiento: ")
                
                
                inputs.ValidarRegistrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento,Veterinaria1)


        elif opcion == "2" and usuario_actual.rol == "veterinario":

            id_mascota=input('Ingrese el ID de la mascota: ')
            fecha=input('Ingrese la fecha en que se registro la historia clinica en formato AAAA-MM-DD HH:MM  ')
            inputs.ValidarBuscar_historia_clinica(id_mascota, fecha, Veterinaria1)
                
        elif opcion == "3" and usuario_actual.rol == "veterinario":
            id_orden = input("Ingrese el ID de la orden: ")
            idM = input("Ingrese el ID de la mascota atendida: ")
            cedula_duenoM = input("Ingrese la cédula del dueño: ")
            cedula_vete = input("Ingrese la cedula del veterinario: ")
            medicamentoO = input("Ingrese el nombre del medicamento: ")
            dosis_enviada = input("Ingrese la dosis recomendada: ")
            estado="ACTIVO"
            
            inputs.ValidarCrear_orden(id_orden, idM, cedula_duenoM, cedula_vete, medicamentoO, dosis_enviada,estado,Veterinaria1)


        elif opcion == "4" and usuario_actual.rol == "veterinario":
            id_orden=input("Ingrese la orden a anular: ")
            
            business.anular_orden(id_orden,Veterinaria1)
        
            
        elif opcion == "5" and (usuario_actual.rol == "Vendedor" or usuario_actual.rol == "veterinario"):
            id_orden=input("Ingresa el numero de la orden a buscar: ")
            inputs.ValidarBuscar_ordenID(id_orden, Veterinaria1)

        elif opcion == "1" and (usuario_actual.rol == "Vendedor" ):

            id_factura=input("Ingrese el id dela factura: ")
            cedula_cliente=input("Ingrese la cedula del cliente: ")
            producto=input("Ingrese el producto a llevar: ")
            valor=input("Ingrese el valor del producto: ")
            cantidad_llevar=input("Ingrese la cantidad a llevar del producto: ")
            

            inputs.validarfactura_sin_orden(id_factura,cedula_cliente,producto,valor, cantidad_llevar,Veterinaria1)
            
        elif opcion == "2" and (usuario_actual.rol == "Vendedor" ):
        
        #Vender producto (con orden)
            idFactura= input("Ingrese el ID de la facura a crear: ")
            id_orden= input("Ingrese el ID de la orden a comprar: ")
            nombre_producto= input("Ingrese el nombre del medicamento: ")
            precio= input("Ingrese el precio unitario del medicamento: ")
            cantidad_llevar= input("Ingrese la cantidad a llevar: ")
            
            inputs.ValidarRegistrar_factura_venta(idFactura, id_orden, nombre_producto, precio, cantidad_llevar, Veterinaria1)
            

        elif opcion=="10":
            business.cerrar_sesion()
            respuesta = input('¿Desea continuar? ')
            if 's' in respuesta.lower():
                
                validar_Sesion()
            elif 'n' in respuesta.lower():
                print("¡Hasta pronto!")
                exit
                exit()
            else:
                print('Respuesta no válida')

    

        elif opcion == "0":
            print("¡Hasta pronto!")
            exit()
            
        else:
            print("Opción no válida, intente de nuevo.")
        print()

def validar_Sesion():
    usuario_valido = False
    while not usuario_valido:
        username = input("Ingrese el usuario: ")
        password = input("Ingrese la contraseña: ")
        if not username or not password:
            print("El nombre de usuario y la contraseña son obligatorios. Por favor, inténtelo de nuevo.")
            continue
        usuario_actual = business.iniciar_sesion(username, password, Veterinaria1)

        if isinstance(usuario_actual, model.usuario):
            menu(usuario_actual)
            usuario_valido = True
        else:
            print("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

validar_Sesion()

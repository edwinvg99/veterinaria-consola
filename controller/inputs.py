from controller import business
from model import model
from datetime import datetime


#VALIDACIONES COMPLETAS PARA REGISTRAR PERSONA
def ValidarRegistrar_Persona(cedula,nombre,edad,Veterinaria1):

    if not cedula.isdigit() or len(cedula) > 10 or int(cedula)<0:
        print("Error: La cédula debe ser numérica y tener un máximo de 10 caracteres y no puede ser negativa.")
        return
    if not nombre.isalpha():
        print("Error: El nombre solo puede contener letras.")
        return
    if not edad.isdigit() or len(edad) > 3 or int (edad) < 0:
        print("Error: La edad debe ser numérica,positiva y tener un máximo de 3 caracteres.")
        return
    if len(cedula) == 0 or len(nombre) == 0 or len(edad) == 0:
        print("Error: Ningún campo puede estar vacío.")
        return
    
    business.registrar_Persona(cedula,nombre,edad,Veterinaria1)


#VALIDACIONES COMPLETAS PARA REGISTRAR MASCOTA
def ValidarRegistrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso, Veterinaria1):
    # Validar que todos los campos estén llenos
    if not all([id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso]):
        print("Error: Todos los campos son obligatorios.")
        return

    # Validar que el ID de la mascota sea un número
    if not id.isdigit():
        print("Error: El ID de la mascota debe ser un número.")
        return

    # Validar que el nombre y la especie sean solo texto
    if not nombre.isalpha():
        print("Error: El nombre de la mascota debe ser solo texto.")
        return
    if not especie.isalpha():
        print("Error: La especie de la mascota debe ser solo texto.")
        return

    # Validar que la cédula del dueño sea un número
    if not cedula_dueno.isdigit():
        print("Error: La cédula del dueño debe ser un número.")
        return

    # Validar que la edad sea un número no negativo
    if not edad.isdigit() or int(edad) < 0:
        print("Error: La edad debe ser un número no negativo.")
        return

    # Validar que el peso sea un número no negativo
    if not peso.isdigit() or int(peso) < 0:
        print("Error: El peso debe ser un número no negativo.")
        return

    # Validar que las características, raza y veterinaria sean solo texto
    if not caracteristicas.isalpha():
        print("Error: Las características deben ser solo texto.")
        return
    if not raza.isalpha():
        print("Error: La raza debe ser solo texto.")
        return
    
    # Si todo está bien, llamar al método de negocio para registrar la mascota
    print("Todas las entradas son válidas.")
    business.registrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso, Veterinaria1)


#VALIDACIONES COMPLETAS PARA REGISTRAR HISTORIA CLINICA
def ValidarRegistrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento,Veterinaria1):
    if not id_mascota or not fecha or not medico or not motivo_consulta or not sintomatologia or not diagnostico or not procedimiento or not medicamento or not dosis or not id_orden or not historial_vacunacion or not alergias or not detalle_procedimiento:
        print("Error: Ningún campo puede estar vacío.")
    
    elif not id_mascota.isdigit():
        print("Error: El ID de la mascota debe ser un número.")
    elif not medico.isalpha():
        print("Error: El nombre del médico debe ser solo texto.")
    elif not motivo_consulta.isalpha():
        print("Error: El motivo de la consulta debe ser solo texto.")
    elif not sintomatologia.isalpha():
        print("Error: La sintomatología debe ser solo texto.")
    elif not diagnostico.isalpha():
        print("Error: El diagnóstico debe ser solo texto.")
    elif not procedimiento.isalpha():
        print("Error: El procedimiento debe ser solo texto.")
    elif not medicamento.isalpha():
        print("Error: El medicamento debe ser solo texto.")
    elif not dosis.isdigit():
        print("Error: La dosis debe ser un número.")
    elif not id_orden.isdigit():
        print("Error: El ID de la orden debe ser un número.")
    elif not historial_vacunacion.isalpha():
        print("Error: El historial de vacunación debe ser solo texto.")
    elif not alergias.isalpha():
        print("Error: Las alergias deben ser solo texto.")

    else:
        print("Todas las entradas son válidas.")
        business.registrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento,Veterinaria1)


#VALIDACIONES COMPLETAS PARA BUSCAR HISTORIA CLINICA
def ValidarBuscar_historia_clinica(id_mascota, fecha, Veterinaria1):
    if not id_mascota or not fecha:
                print("Error: Ningún campo debe estar vacío.")
    elif not id_mascota.isnumeric():
                print("Error: El campo id_mascota debe ser numérico.")
    else:
            try:
                datetime.strptime(fecha, '%Y-%m-%d %H:%M')
                business.buscar_historia_clinica(id_mascota, fecha, Veterinaria1)
            except ValueError:
                print("Error: La fecha debe tener el formato AAAA-MM-DD HH:MM.")


#VALIDACIONES COMPLETAS PARA CREAR ORDEN
def ValidarCrear_orden(id_orden, idM, cedula_duenoM, cedula_vete, medicamentoO, dosis_enviada,estado,Veterinaria1):
    if not id_orden or not idM or not cedula_duenoM or not cedula_vete or not medicamentoO or not dosis_enviada:
        print("Error: Ningún campo debe estar vacío.")
        
    elif not id_orden.isnumeric():
        print("Error: El campo id orden debe ser numerico.")
    elif not idM.isnumeric() :
        print("Error: El id de la mascota debe ser numerico")
    elif not cedula_duenoM.isnumeric():
        print("Error: La cedula del dueño debe ser numerica")
    elif not cedula_vete.isnumeric():
        print("Error: La cedula del veterinario debe ser numerica")
    elif not dosis_enviada.isnumeric():
        print("Error: El campo dosis recomendada debe ser numerica")
    elif int(dosis_enviada) < 0:
        print("Error: La dosis recomendada no puede ser negativa")
    elif medicamentoO.isnumeric():
        print("Error: El medicamento debe ser de tipo texto")
    elif estado.isnumeric():
        print('Error: El estado debe ser de tipo texto')
    else:
        business.crear_orden(id_orden, idM, cedula_duenoM, cedula_vete, medicamentoO, dosis_enviada,estado,Veterinaria1)


#VALIDACIONES COMPLETAS PARA BUSCAR ORDEN
def ValidarBuscar_ordenID(id_orden, Veterinaria1):
    if not id_orden:
        print('El campo no puede estar vacío')
        return
    if not id_orden.isnumeric():
        print('Solo se permiten números')
        return
    if int(id_orden) < 0:
        print('El número no puede ser negativo')
        return
    business.buscar_ordenID(id_orden, Veterinaria1)


#VALIDACIONES COMPLETAS PARA REGISTRAR FACTURA
def ValidarRegistrar_factura_venta(idFactura, id_orden, nombre_producto, precio, cantidad_llevar, Veterinaria1):
    if not all([idFactura, id_orden, nombre_producto, precio, cantidad_llevar]):
        print("Error: Ningún campo debe estar vacío.")
        
    elif not idFactura.isdigit():
        print("Error: El campo idFactura debe ser numérico.")
        
    elif not id_orden.isdigit():
        print("Error: El campo id_orden debe ser numérico.")
        
    elif not precio.isdigit():
        print("Error: El campo precio debe ser numérico.")
    elif int(precio) < 0:
        print("Error: El campo precio no puede ser negativo.")
        
    elif not cantidad_llevar.isdigit():
        print("Error: El campo cantidad_llevar debe ser numérico.")
    elif int(cantidad_llevar) < 0:
        print("Error: El campo cantidad_llevar no puede ser negativo.")
        
    elif nombre_producto.isnumeric():
        print("Error: El campo nombre_producto debe ser de texto.")
        
    else:
        precio=float (precio)
        cantidad_llevar=int (cantidad_llevar)
        business.registrar_factura_venta(idFactura, id_orden, nombre_producto, precio, cantidad_llevar, Veterinaria1)

#validaciones completas para registrar factura sin orden
def validarfactura_sin_orden(id_factura,cedula_cliente, producto, valor, cantidad_llevar, veterinaria1):
    
    if not all([id_factura, cedula_cliente, producto, valor, cantidad_llevar]):
            print("Error: Ningún campo debe estar vacío.")
    elif not id_factura.isdigit():
        print("Error: El campo id Factura debe ser numérico.")
    elif not cedula_cliente.isdigit():
        print("Error: El campo cedula cliente debe ser numérico.")
    elif producto.isnumeric():
        print("Error: El campo nombre producto debe ser de texto")
    elif not valor.isdigit():
            print("Error: El campo precio debe ser numérico.")
    elif int(valor) < 0:
            print("Error: El campo precio no puede ser negativo.")
    elif not cantidad_llevar.isdigit():
            print("Error: El campo cantidad_llevar debe ser numérico.")
    elif int(cantidad_llevar) < 0:
            print("Error: El campo cantidad_llevar no puede ser negativo.")
    else:
        valor= int(valor)
        cantidad_llevar= int(cantidad_llevar)
        business.factura_sin_orden(id_factura,cedula_cliente, producto, valor, cantidad_llevar,veterinaria1)

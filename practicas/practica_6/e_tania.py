pila_normal = []

pila_tercera_edad = []

cola_control = []

 

id_normal = 1

id_tercera_edad = 1

 

while True:

    print("\n--- MENÚ ATENCIÓN AL CLIENTE ---")

    print("1. Sacar ficha Normal")

    print("2. Sacar ficha Tercera Edad")

    print("3. Llamar fichas (Armar / Procesar Cola)")

    print("4. Ver fichas (Listar cola)")

    print("5. Atender ficha (Usuario vino)")

    print("6. El usuario no vino")

    print("7. Salir")

   

    opcion = input("Seleccione una opción: ")

 

    if opcion == "1":

        ticket = {"id": f"N-{id_normal}", "tipo": "normal", "estado": "pendiente"}

        pila_normal.append(ticket)

        print(f"Ticket generado: {ticket['id']}")

        id_normal += 1

 

    elif opcion == "2":

        ticket = {"id": f"TE-{id_tercera_edad}", "tipo": "tercera_edad", "estado": "pendiente"}

        pila_tercera_edad.append(ticket)

        print(f"Ticket generado: {ticket['id']}")

        id_tercera_edad += 1

 

    elif opcion == "3":

        if len(pila_normal) == 0 and len(pila_tercera_edad) == 0:

            print("No hay tickets nuevos en las filas para llamar.")

        else:

            if len(pila_tercera_edad) > 0:

                pila_tercera_edad.reverse()

                while len(pila_tercera_edad) > 0:

                    cola_control.append(pila_tercera_edad.pop())

           

            if len(pila_normal) > 0:

                pila_normal.reverse()

                while len(pila_normal) > 0:

                    cola_control.append(pila_normal.pop())

                   

            print("Cola de control armada con éxito respetando las prioridades.")

 

    elif opcion == "4":

        if len(cola_control) == 0:

            print("La cola de control está vacía.")

        else:

            print("\n--- FICHAS EN COLA DE CONTROL ---")

            for t in cola_control:

                print(f"Ticket: {t['id']} | Tipo: {t['tipo']} | Estado: {t['estado']}")

 

    elif opcion == "5":

        if len(cola_control) == 0:

            print("No hay nadie en la cola para atender.")

        else:

            ticket_atendido = cola_control.pop(0)

            ticket_atendido["estado"] = "atendido"

            print(f"Atendiendo al ticket: {ticket_atendido['id']}. Estado cambiado a ATENDIDO.")

 

    elif opcion == "6":

        if len(cola_control) == 0:

            print("No hay usuarios en la cola para procesar.")

        else:

            ticket_no_vino = cola_control.pop(0)

            ticket_no_vino["estado"] = "no atendido"

            print(f"El usuario del ticket {ticket_no_vino['id']} no se presentó.")

           

            if ticket_no_vino["tipo"] == "tercera_edad":

                pila_tercera_edad.append(ticket_no_vino)

                print("Devuelto a la fila de Tercera Edad.")

            else:

                pila_normal.append(ticket_no_vino)

                print("Devuelto a la fila Normal.")

 

    elif opcion == "7":

        print("Saliendo del sistema...")

        break

       

    else:

        print("Opción inválida, intente de nuevo.")


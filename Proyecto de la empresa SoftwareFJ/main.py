from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva


# Guardar logs
def guardar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


print("===== SISTEMA SOFTWARE FJ =====\n")


# SERVICIOS
sala = ReservaSala("Sala VIP", 50000)
equipo = AlquilerEquipo("Computador", 30000)
asesoria = AsesoriaEspecializada("Asesoría TI", 70000)


# 10 operaciones completas
casos = [
    ("Andrea", "153", "andereatj@gmail.com", "3001112222", sala, 2),
    ("Pablo", "416", "pablotorrez@gmail.com", "3012223333", equipo, 1),
    ("Lauren", "779", "laumarti@gmail.com", "3023334444", asesoria, 3),
    ("camil", "111", "camilbarrios@gmail.com", "3001334987", sala, 2),
    ("Martin", "125", "martinh43@gmail.com", "3001234567", sala, 2),
    ("Sarai", "222", "sarai355@gmail.com", "3001234567", sala, 2),
    ("Camilo", "363", "camilo456h@gmail.com", "telefono", equipo, 1),
    ("", "544", "", "3008889999", sala, -2),
    ("David", "545", "david46@gmail.com", "30077458888", asesoria, 0),
    ("Ema", "687", "ematamara56@gmail.com", "3005454844", equipo, 4)
]


for i, caso in enumerate(casos, start=1):
    try:
        print(f"\nOPERACIÓN {i}")

        cliente = Cliente(
            caso[0],
            caso[1],
            caso[2],
            caso[3]
        )

        reserva = Reserva(cliente, caso[4], caso[5])

    except Exception as e:
        guardar_log(f"Error en operación {i}: {str(e)}")
        print(f"Error: {e}")

    else:
        try:
            resultado = reserva.procesar()
            print(resultado)

            guardar_log(
                f"Operación {i} exitosa - {cliente.get_nombre()}"
            )

        except Exception as e:
            guardar_log(
                f"Reserva fallida en operación {i}: {str(e)}"
            )
            print(f"Reserva fallida: {e}")

    finally:
        print("Proceso finalizado")


HV = 100000

EVENTO = "---"
T = 0
NS = 0
NT = 0
TPLL = 8 * 60
TPS = HV
STLL = 0
STS = 0
PPS = 0
ITO = 8 * 60
STO = 0
PTO = 0
TF = 10 * 60 + 30

IA = 0
TA = 0

IAValoresPosibles = [10, 5, 60, 15, 30, 35, 10, 20, 15]
TAValoresPosibles = [40, 5, 15, 10, 30, 45, 15, 20, 10]

# String que le da formato a la tabla que será printeada
formatoString = "{:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7}"


def comenzarSimulacion():
    printPrimeraFilaTabla()

    ejecutarCicloSimulacion()


def ejecutarCicloSimulacion():
    global T
    global NS
    global NT
    global TPLL
    global TPS
    global STLL
    global STS
    global PPS
    global ITO
    global STO
    global PTO
    global TF
    global IA
    global TA
    global EVENTO

    printNuevaFilaTabla()

    # Se produce una llegada
    if TPLL <= TPS:
        EVENTO = "LLEGADA"
        T = TPLL
        STLL += T
        IA = obtenerIA()
        TPLL = T + IA
        NS += 1
        NT = NT + 1

        # Es el primero en la cola
        if NS == 1:
            STO += T - ITO
            TA = obtenerTA()
            TPS = T + TA

        # NO es el primero en la cola
        else:
            # No se hace nada
            pass

    # Se produce una salida
    else:
        EVENTO = "SALIDA"
        T = TPS

        STS += T

        NS -= 1

        # Quedan mas personas en la cola
        if NS >= 1:
            TA = obtenerTA()
            TPS = T + TA

        # La cola queda vacia
        else:
            ITO = T
            TPS = HV

    # La simulacion debe seguir
    if T < TF:
        ejecutarCicloSimulacion()

    # La simulacion terminó (falta vaciamiento)
    else:

        # No se requiere vaciamiento (la fila quedo vacia)
        if NS == 0:
            PPS = (STS - STLL) / NT
            PTO = (STO * 100) / T

            printNuevaFilaTabla()
            return

        # Se requiere vaciamiento
        else:
            TPLL = HV
            ejecutarCicloSimulacion()

#oldValues = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0]

def printNuevaFilaTabla():
    #newValues = [minutosAHora(T), NS, NT, minutosAHora(TPLL), minutosAHora(TPS)]

    print(formatoString.format(EVENTO, minutosAHora(T), NS, NT, minutosAHora(TPLL), minutosAHora(TPS),
                               minutosAHora(STLL), minutosAHora(STS), round(PPS, 2), minutosAHora(ITO), STO, round(PTO, 2), minutosAHora(TF)))


def printPrimeraFilaTabla():
    print(formatoString.format('Evento', 'T', 'NS', 'NT', "TPLL", "TPS",
                               "STLL", "STS", "PPS", "ITO", "STO", "PTO", "TF"))


def minutosAHora(minutes):
    if minutes == HV:
        return "H.V."
    hours = int(minutes / 60)
    minutes = minutes % 60
    return str(hours).rjust(2, "0") + ":" + str(minutes).rjust(2, "0")


def obtenerIA():
    global IAValoresPosibles

    if len(IAValoresPosibles) == 0:
        return 0
    siguienteValor = IAValoresPosibles[0]
    IAValoresPosibles.remove(siguienteValor)
    return siguienteValor


def obtenerTA():
    global TAValoresPosibles

    if len(TAValoresPosibles) == 0:
        return 0
    siguienteValor = TAValoresPosibles[0]
    TAValoresPosibles.remove(siguienteValor)
    return siguienteValor


def main():
    print("Comenzando simulacion...")
    comenzarSimulacion()
    print("Simulacion terminada. Finalizando programa.")


if __name__ == '__main__':
    main()

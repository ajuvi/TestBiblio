from biblioteca import consultar_llibres

def mostrar_llibres():
    llibres = consultar_llibres()

    for llibre in llibres:
        print(llibre["titol"], llibre["autor"])
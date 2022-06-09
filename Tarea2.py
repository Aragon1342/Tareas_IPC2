class Nodo:
    def __init__(self, data):
        self.item = data
        self.sig = None
        self.ant = None

class ListaDobleCircular:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar_en_listavacia(self, data):
        if self.inicio is None:
            new_nodo = Nodo(data)
            self.inicio = new_nodo
        else:
            print("La lista no está vacía")

    def insert_at_start(self, data):
        if self.inicio is None:
            new_nodo = Nodo(data)
            self.inicio = new_nodo
            print("Nodo insertado")
            return

        new_nodo = Nodo(data)
        new_nodo.sig = self.inicio
        self.inicio.ant = new_nodo
        self.inicio = new_nodo

    def traverse_list(self):
        if self.inicio is None:
            print("La lista no tiene elementos")
            return
        else:
            n = self.inicio
            while n is not None:
                print(n.item, "")
                n = n.sig

    def insert_at_end(self, data):
        if self.inicio is None:
            new_nodo = Nodo(data)
            self.inicio = new_nodo
            return
        n = self.inicio
        while n.sig is not None:
            n = n.sig
        new_nodo = Nodo(data)
        n.sig = new_nodo
        new_nodo.ant = n

    def valorAct(self, valor):
        val = self.inicio
        while (val != None):
            if (val.data == valor):
                print("\nEl anterior es: ", val.ant.item)
                print("El valor que escogio es:", val.item)
                print("El siguiente es: ", val.sig.item)
            if (val.siguiente == self.inicio):
                return
            val = val.sig

#Eva Gonzalez Correa

class calculadora:
    """
    Calculadora. Clase para la realizacion de operaciones matematicas a partir de dos operadores.

    Atributos:
        num1: primer operador
        num2: segundo operadores

    Metodos:
        set_num1: modifica el valor de la variable num1
        set_num2: modifica el valor de la variable num2
        get_num1: devuelve el valor de la variable num1
        get_num2: devuelve el valor de la variable num2
        sumar: realiza la suma entre num1 y num2. Este metodo se usara en el metodo condiciones
        restar: realiza la suma entre num1 y num2. Este metodo se usara en el metodo condiciones
        multiplicar: realiza la multipliacion entre num1 y num2. Este metodo se usara en el metodo condiciones
        dividir: realiza la division entre num1 y num2. Este metodo se usara en el metodo condiciones
        valorespantalla: pide al usuario que introduzca los valores num1 y num2 por pantalla
        condiciones: pregunta al usuario mediante un menu que quiere hacer con num1 y num2

    Ejemplo:

        >>> import calculadora
        >>> calc = calculadora(0,0)
        >>> calc.valorespantalla()
        >>> calc.condiciones()
    """
    # Definimos atributos o propiedades
    def __init__(self, num1 = None, num2 = None):   #Con None esta clase puede tener o no parametros --> calculadora()   o calculadora(7,9)
        """
        Constructor. Define los atributos o argumentos num1 y num2.
        """
        self.num1 = num1
        self.num2 = num2

    # Métodos SET (modificar valores)
    def set_num1(self, num1):
        """
        Método set num1. Modificación valor del operador num1.
        """
        self.num1 = num1

    def set_num2(self, num2):
        """
        Método set num2. Modificación valor del operador num2.
        """
        self.num2 = num2

    # Métodos GET (devuelven los valores)
    def get_num1(self):
        """
        Método get num1. Método para la obtención del valor del operador num1.
        """
        return self.num1

    def get_num2(self):
        """
        Método set num2. Método para la obtención del valor del operador num2.
        """
        return self.num2


    # DEFINIMOS FUNCIONES   -->  Funcionalidades que se le otorgan a la clase (en este caso, operaciones)

    def sumar(self):
        """
        Método de la suma. Realiza la suma de num1 y num2.
        Inputs:
            num1: primer operando
            num2: segundo operando
        Outputs:
            suma: devulve el resultado como un string en forma de suma.
        """
        suma = f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
        return suma

    def restar(self):
        """
        Método de la resta. Realiza la resta de num1 y num2.
        Inputs:
            num1: primer operando
            num2: segundo operando
        Outputs:
            resta: devulve el resultado como un string en forma de resta.
        """
        resta = f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
        return resta

    def multiplicar(self):
        """
        Método de la multiplicacion. Realiza la multiplicacion de num1 y num2.
        Inputs:
            num1: primer operando
            num2: segundo operando
        Outputs:
            multi: devulve el resultado como un string en forma de multiplicacion.
        """
        multi = f"{self.num1} x {self.num2} = {self.num1 * self.num2}"
        return multi

    def dividir(self):                  #Añadimos una excepcion, para cuando el divisor sea 0.
        """
        Método de la division. Realiza la division de num1 y num2.
        Inputs:
            num1: primer operando
            num2: segundo operando
        Outputs:
            division: devulve el resultado como un string en forma de division si esta puede realizarse. En caso contrario devuelve una excepcion.
        """
        try:
            division = f"{self.num1} / {self.num2} = {self.num1 / self.num2}"
        except ZeroDivisionError:
            division = "ERROR"
            print(f"{self.num1} / {self.num2} = No tiene resultado bien definido")
        return division

    #Hasta aquí tendríamos nuestra calculadora.

    #----------Funciones añadidas----------

    #Podemos añadirles funciones y asi obtner funcionalidades, como un Menu por el que navegar.

    def valorespantalla(self):
        """
        Método introducir por pantalla. Pide dos valores por pantalla que pasaran a ser num1 y num2.
        En caso de que los valores no sean correctos los vuelve a pedir.
        Intputs:
            n1: primer valor que introduce el usuario por pantalla
            n2: segundo valor que introduce el usuario por pantalla
        Outputs:
            set_num1: modifica el valor de num1 a n1
            set_num2: modifica el valor de num2 a n2
        """
        print(f"\n------------------- C A L C U L A D O R A -------------------\n")
        #Bucle que se ejecute mientras se satisfaga las siguientes condiciones

        while True:
            try:                                    #Abrimios un bloque de excepciones
                n1 = input("Introduce el 1º valor: ")  #Condiciones que cambian el bucle para que no sea finito
                n2 = input ("Introduce el 2º valor: ")

                if '.'in n1 or n2:   #para que acepte float, entendemos que si tiene un punto es float
                    n1=float(n1)
                    n2=float(n2)

                else:               #si no es float es entero
                    n1=int(n1)
                    n2=int(n2)
                self.set_num1(n1)
                self.set_num2(n2)
                break
            except ValueError:            #Si no es numerico sale la excepcion
                print("Introduce valores numericos")

    def condiciones(self):
        """
        Menu de condiciones. En este el usuario elige que accion realizar con los operadore introducimos num1 y num2.
        Intputs:
            entrada: pide por pantalla la opcion que queremos realizar, (S, R, M, D, T, C, X)
        Outputs:
            sumar: si elegimos la opcion S o s, imprime la funcion sumar. Con T o t imprime todas las operaciones, incluida la suma.
            restar: con R o r, imprime la funcion restar.  Con T o t imprime todas las operaciones, incluida la resta.
            multiplicar: con M o m, imprime la funcion multiplicar. Con T o t imprime todas las operaciones, incluida la multiplicacion.
            dividir: con D o d, imprime la funcion dividir. Con T o t imprime todas las operaciones, incluida la division.
            valorespantalla: con C o c, muestra modifica los valores por pantalla.
        """

        #Creamos un menu donde se muestra al usuario las opciones
        while True:
            menu = '''
Opciones:
    S    Suma                     T    Todas las operaciones
    R    Resta                    C    Modificar valores
    M    Multiplicacion
    D    Division                 X    SALIR
        '''
            print(menu)
            entrada = str(input(f"Selecciona una opción: ").capitalize())   #condicion de string (aunque ya lo sea por defecto). Las letras en mayusculas, para que funcione con minusculas tambien

            opcion = entrada             #condicion cambio de valores, para que el bucle no sea infinito.

            #condiciones para cada opcion del menu definido.
            if opcion == "S":
                print(self.sumar())

            elif opcion == "R":
                print(self.restar())

            elif opcion == "M":
                print(self.multiplicar())

            elif opcion == "D":
                print(self.dividir())

            elif opcion == "T":
                print(self.sumar())
                print(self.restar())
                print(self.multiplicar())
                print(self.dividir())

            elif opcion == "C":
                print(f"Cambiar numeros")
                self.valorespantalla()

            elif opcion == "X":        #se rompe el bucle al elegir esta opcion, para salir del programa
                break

            else:
                print("Opcion no valida, elija una de las siguientes opciones: ")

        print(f"¡Hasta la proxima!")   #Mensaje de despedida cuando se rompe el bucle

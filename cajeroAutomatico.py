class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo
        
    def verificar_pin(self,pin):
        return self.__pin == pin
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
        
    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            return True
        else:
            return False
    
    def obtener_saldo(self):
        return self.__saldo

    def transferir(self, cuenta_destino, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            cuenta_destino.__saldo += cantidad
            return True
        else:
            return False
    
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

class Banco:
    def __init__(self):
        self.__cuentas = {}
        self.cuentas_registradas()
        
    def agregar_cuenta(self, cuenta):
        self.__cuentas[cuenta.obtener_numero_cuenta()] = cuenta
        
    def obtener_cuenta(self, numero_cuenta):
        return self.__cuentas.get(numero_cuenta)
    
    def cuentas_registradas(self):
        cuentas_iniciales= [
            Cuenta(1234, 5678, 1000),
            Cuenta(5678, 1234, 500)
        ]
        for cuenta in cuentas_iniciales:
            self.agregar_cuenta(cuenta)
                
class CajeroAutomatico:
    def __init__(self, banco):
        self.__banco = banco
        self.__cuenta_actual = None
    
    def mostrar_bienvenida(self):
        print("-"*50)
        print("Bienvenido al Cajero Automatico")
        print("-"*50)
        numero_cuenta= int(input("Ingrese su número de cuenta: "))
        pin = int(input("Ingrese cu codigo pin: "))
        print("-"*50)
        return numero_cuenta, pin
        
    def autenticar_usuario(self, numero_cuenta, pin):
        cuenta = self.__banco.obtener_cuenta(numero_cuenta)
        if cuenta and cuenta.verificar_pin(pin):
            self.__cuenta_actual = cuenta
            return True
        else:
            return False
        
    def mostrar_menu(self):
        if self.__cuenta_actual:
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Transferir")
            print("5. Salir")
            print("-"*50)
            return input("Elija una opcion: ")
    
    def consultar_saldo(self):
        if self.__cuenta_actual:
            saldo = self.__cuenta_actual.obtener_saldo()
            print(f"Su saldo es S/{saldo}.")
    
    def depositar(self, cantidad):
        if self.__cuenta_actual:
            self.__cuenta_actual.depositar(cantidad)
            print(f"Se han depositado S/{cantidad}.")
            
    def retirar(self, cantidad):
        if self.__cuenta_actual:
            if self.__cuenta_actual.retirar(cantidad):
                print(f"Se han retirado S/{cantidad}.")
            else:
                print("Fondos insuficientes.")
                        
    def transferir(self, numero_cuenta_destino, cantidad):
        if self.__cuenta_actual:
            cuenta_destino = self.__banco.obtener_cuenta(numero_cuenta_destino)
            if cuenta_destino:
                if self.__cuenta_actual.transferir(cuenta_destino, cantidad):
                    print(f"Se han tranferido S/{cantidad}.")
                else:
                    print(f"Fondos insuficientes.")
            else:
                print("Cuenta destino no encontrada.")
                
    def ejecutar_menu(self):
        numero_cuenta, pin = self.mostrar_bienvenida()
        if self.autenticar_usuario(numero_cuenta, pin):
            while True:
                opcion = self.mostrar_menu()
                if opcion == '1':
                    self.consultar_saldo()
                elif opcion == '2':
                    cantidad = float(input("Ingrese la cantidad a depositar: "))
                    self.depositar(cantidad)
                elif opcion == '3':
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    self.retirar(cantidad)
                elif opcion == '4':
                    numero_cuenta_destino = int(input("Ingrese el número de cuenta destino: "))
                    cantidad = float(input("Ingrese la cantidad a transferir: "))
                    self.transferir(numero_cuenta_destino, cantidad)
                elif opcion == '5':
                    print("Gracias por usar el cajero automático.")
                    break
                else:
                    print("Opción no valida. Intente de nuevo")
        else:
            print("Autenticacion fallida.")
        

banco = Banco()
cajero = CajeroAutomatico(banco)
cajero.ejecutar_menu()
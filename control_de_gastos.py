import json
import os

class Control_Gasto:
    def __init__(self, nombre, salario):

        self.nombre = nombre
        self._salario = salario

        if os.path.exists("usuario_gastos.json"):

            try:
                with open("usuario_gastos.json", "r", encoding="utf-8") as archivo:
                    self.lista_gastos = json.load(archivo)

            except json.JSONDecodeError:
                print("El archivo esta dañado, se empezara con una lista vacia.")
                self.lista_gastos = []

        else:
            self.lista_gastos = []

    def registrar_gasto(self):


        nombre_producto = input("escribe el nombre del producto que compraste: ").capitalize().strip()
        try:
            precio_producto = float(input("Escribe el precio del producto: "))
        except ValueError:
            print("Escribe un valor valido.")
            return
        
        if precio_producto <= 0:
            print(f"{self.nombre} Solo puedes agregar numeros mayores que (0).")
            return
        
        dic_gastos = {"nombre": nombre_producto, "precio": precio_producto} 
        self.lista_gastos.append(dic_gastos)
        self.guardar()
                

       
    def eliminar_gasto(self):


        eliminar_producto = input("Escribe el nombre del producto que deseas eliminar: ").capitalize().strip()
        for indice, gastos in enumerate(self.lista_gastos):
            if  gastos["nombre"] == eliminar_producto:
                self.lista_gastos.pop(indice)

                self.guardar()
                print("Producto eliminado.")
                break
       
        else:
            print("Gasto no encontrado.")
            
       
    def mostrar_gastos(self):

        if not self.lista_gastos:
            print("\nno has hecho ningún gasto.")
            return
        
        print("---Gastos---\n")
        for gastos in self.lista_gastos:
            print(gastos)

        total = sum(gastos["precio"] for gastos in self.lista_gastos)

        
        porcentaje = (total / self._salario) * 100
        restante = self._salario - total

        print("\n---Otros---")
        print(f"\nHas gastado un {porcentaje:.2f}% de 100%") 
        print(f"Total de todo lo que has gastado: {total}")
        print(f"Esto es lo que te queda: {restante}")

    
    def guardar(self):

        with open("usuario_gastos.json", "w", encoding="utf-8") as archivo:
            json.dump(self.lista_gastos, archivo, indent=4, ensure_ascii=False)

def dolares_a_pesos():
    print("Vamos a cambiar de dolares a pesos colombianos")
    while True:
        try:
            num1 = float(input("Escribe el monto de dolares: "))
            num2 = float(input("Escribe la tasa en la que se encuentra el peso el dia de hoy: "))

            if num1 <= 0 or num2 <= 0:
                print("Debes escribir numeros mayores que (0).")
                continue

            else:
                resultado = num1 * num2
                return resultado
                
        except ValueError:
            print("Solo puedes escribir numeros.")




def pesos_a_dolares():
    print("Vamos a cambiar de pesos a dolares")
    while True:
        try:
            num1 = float(input("Escribe el monto de pesos colombianos: "))
            num2 = float(input("Escribe la tasa en la que se encuentra el dolar el dia de hoy: "))
        
            if num1 <= 0 or num2 <= 0:    
                print("Escribe numeros mayores que (0)")
                continue
        
            else:
                resultado = num1 / num2
                return resultado
            
                        
        except ValueError:
            print("Solo puedes escribir numeros.")


def pedir_salario():
     while True:
            
        try:
            salario = float(input("Escribe tu salario neto: "))
            if salario <= 0:
                print("Debes escribir un valor mayor que cero")
                continue
            else:
                print("Valor guardado correctamente.")
                return salario
            
    
        except ValueError:
            print("Escribe un valor valido, vuelve a intentarlo")



nombre = input("Escribe tu nombre: ")
salario = pedir_salario()

persona = Control_Gasto(nombre, salario)
    

while True:
    print("\n----Control de gastos----\n")
    print("-Menú-")
    print("escribe (1): si quieres agregar un gasto")
    print("escribe (2): si quieres eliminar un gasto")
    print("escribe (3): si quieres ver tus gastos")
    print("escribe (4): si quieres cambiar de moneda")
    print("escribe (5): si quieres salir del programa\n")

    try:
        opcion = int(input("Escribe tu respuesta: "))

    except ValueError:
        print("No puedes escribir letras.")
        continue

    if opcion == 1:
        persona.registrar_gasto()

    elif opcion == 2:
        persona.eliminar_gasto()
    
    elif opcion == 3:
        persona.mostrar_gastos()

    elif opcion == 4:
        while True:
            print("\nescribe (1): si quieres cambiar de dolares a pesos")
            print("escribe (2): si quieres cambiar de pesos a dolares")
            print("escribe (3): si quieres salir\n")

            try:
                opcion_moneda = int(input("Escribe tu respuesta: "))

            except ValueError:
                print("solo puedes escribir numeros.")
                continue

            if opcion_moneda == 1:
                print(dolares_a_pesos())

            elif opcion_moneda == 2:
                print(pesos_a_dolares())
    
            elif opcion_moneda == 3:
                print("Gracias por tu respuesta.")
                break
            else:
                print("Respuesta incorrecta.")
    
    elif opcion == 5:
        print("Gracias por usar el programa.")
        break

    else:
        print("Respuesta no válida.")
        continue


    

    


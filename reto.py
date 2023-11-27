import datetime

class Greeter:
    def greet(self, name):
        name = name.strip()
        name = name.capitalize()
        
        horaActual = datetime.datetime.now().hour
        if 6 <= horaActual < 12:
            greeting = "Buenos días"
        elif 18 <= horaActual < 22:
            greeting = "Buenas noches"
        else:
            greeting = "Buenas tardes"
        
        return f"{greeting} {name}"
    
greeter = Greeter()
saludo = greeter.greet("Juan")
print(saludo)
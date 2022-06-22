from django.shortcuts import render
from django.http import HttpResponse
from App.models import Familia
# Create your views.

def familia1(self):
    
    padre = Familia(familiar= "Papa", nombre= "Pedro", edad= "50")
    
    padre.save()
    
    madre = Familia(familiar= "Mama", nombre= "Ana", edad= "48")
    
    madre.save()
    
    hijo1 = Familia(familiar= "1er hijo", nombre= "Juan", edad= "18")
    
    hijo1.save()

    hijo2 = Familia(familiar= "2do hijo", nombre= "Pablo", edad= "15")
    
    hijo2.save()
    
    informacion = f"El {padre.familiar} se llama {padre.nombre}, tiene: {padre.edad} años \nLa {madre.familiar} se llama {madre.nombre} y tiene: {madre.edad} años \nEl {hijo1.familiar} se llama {hijo1.nombre}, el tiene: {hijo1.edad} años \nEl {hijo2.familiar} se llama {hijo2.nombre} y el tiene: {hijo2.edad} años, es el mas chico"
    
    return HttpResponse(informacion)
    

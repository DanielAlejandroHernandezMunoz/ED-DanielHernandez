```python
dic = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
}

print(dic["a"]) 
#nievo elemento
dic["F"] = 6
#modificar
dic["a"] = 10 
#eliminar
del dic["b"] 
#comprobar existencia
print("a" in dic) 
print("z" in dic)
#recorrer claves
for clave, valor in dic.items():
  print(clave, valor)
  #metodos utiles
  dic={"x":100, "y" : 200}
  print(dic.keys()) # x,y
  print(dic.values()) #100 y 200
  print(dic.items()) #clave y valor
#obtener valor con get
print(dic.get("x"))
#eliminar y devolver valor
valor.dic.pop("y")
print(valor)
#comparacion lista vd diccionario
```
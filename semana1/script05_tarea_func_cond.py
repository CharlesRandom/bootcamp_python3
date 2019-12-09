def cuadrado_rectangulo(num1, num2):
    if num1 == num2:
        return 'cuadrado'
    else:
        return 'rectangulo'

print(cuadrado_rectangulo(2,2))
print(cuadrado_rectangulo(2,4))
print(cuadrado_rectangulo(3,3))
print(cuadrado_rectangulo(3,4))
print(cuadrado_rectangulo(4,3))
print(cuadrado_rectangulo(4,4))
print(cuadrado_rectangulo(5,5))
print(cuadrado_rectangulo(6,6))
print(cuadrado_rectangulo(3.2,7))
print(cuadrado_rectangulo(9.5,100))
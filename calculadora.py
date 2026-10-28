def _validar_numeros(a, b):
    """Lanza TypeError si alguno de los argumentos no es numérico."""
    for valor in (a, b):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Ambos valores deben ser numéricos")
 
 
def sumar(a, b):
    return a + b
 
 
def restar(a, b):
    _validar_numeros(a, b)
    return a - b
 
 
def multiplicar(a, b):
    _validar_numeros(a, b)
    return a * b
 
 
def dividir(a, b):
    _validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
 
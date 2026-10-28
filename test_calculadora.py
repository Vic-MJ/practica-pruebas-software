import pytest
from calculadora import sumar, restar, multiplicar, dividir
 
def test_sumar_positivos():
    assert sumar(2, 3) == 5
 
def test_sumar_negativos():
    assert sumar(-2, -3) == -5
 
def test_restar_positivos():
    assert restar(10, 4) == 6
 
 
def test_restar_resultado_negativo():
    assert restar(3, 8) == -5
 
 
def test_restar_negativos():
    assert restar(-5, -2) == -3
 
 
def test_restar_decimales():
    assert restar(5.5, 2.5) == 3.0
 
 
def test_multiplicar_positivos():
    assert multiplicar(4, 3) == 12
 
 
def test_multiplicar_negativo_por_positivo():
    assert multiplicar(-4, 3) == -12
 
 
def test_multiplicar_negativos():
    assert multiplicar(-4, -3) == 12
 
 
def test_multiplicar_por_cero():
    assert multiplicar(7, 0) == 0
 
 
def test_dividir_exactamente():
    assert dividir(10, 2) == 5
 
 
def test_dividir_decimal():
    assert dividir(7, 2) == 3.5
 
 
def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
 
 
def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0
 
 
def test_dividir_cero_entre_negativo():
    assert dividir(0, -5) == 0
 
 
def test_dividir_texto_lanza_typeerror():
    with pytest.raises(TypeError):
        dividir("diez", 2)
 
 
def test_dividir_none_lanza_typeerror():
    with pytest.raises(TypeError):
        dividir(10, None)
 
 
def test_restar_texto_lanza_typeerror():
    with pytest.raises(TypeError):
        restar("a", 1)
 
 
def test_multiplicar_texto_lanza_typeerror():
    with pytest.raises(TypeError):
        multiplicar(2, "3")
 
 
@pytest.mark.parametrize("a, b", [("1", 2), (1, [2]), (None, 1), (True, 1)])
def test_multiplicar_entradas_invalidas(a, b):
    with pytest.raises(TypeError):
        multiplicar(a, b)
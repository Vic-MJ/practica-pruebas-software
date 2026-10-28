# Tabla de casos de prueba

| ID | Escenario | Entrada | Resultado esperado | Resultado obtenido | Estado |
|----|-----------|---------|--------------------|--------------------|--------|
| CP01 | Suma normal | sumar(2, 3) | 5 | 5 | PASSED |
| CP02 | Suma de negativos | sumar(-2, -3) | -5 | -5 | PASSED |
| CP03 | División exacta | dividir(10, 2) | 5 | 5.0 | PASSED |
| CP04 | División con decimal | dividir(7, 2) | 3.5 | 3.5 | PASSED |
| CP05 | División entre cero | dividir(10, 0) | ValueError | ValueError | PASSED |
| CP06 | Resta normal | restar(10, 4) | 6 | 6 | PASSED |
| CP07 | Resta con resultado negativo | restar(3, 8) | -5 | -5 | PASSED |
| CP08 | Resta de negativos | restar(-5, -2) | -3 | -3 | PASSED |
| CP09 | Resta con decimales | restar(5.5, 2.5) | 3.0 | 3.0 | PASSED |
| CP10 | Multiplicación normal | multiplicar(4, 3) | 12 | 12 | PASSED |
| CP11 | Negativo por positivo | multiplicar(-4, 3) | -12 | -12 | PASSED |
| CP12 | Negativo por negativo | multiplicar(-4, -3) | 12 | 12 | PASSED |
| CP13 | Multiplicar por cero (valor límite) | multiplicar(7, 0) | 0 | 0 | PASSED |
| CP14 | Cero entre número ≠ 0 | dividir(0, 5) | 0 | 0.0 | PASSED |
| CP15 | Cero entre negativo | dividir(0, -5) | 0 | -0.0 (== 0) | PASSED |
| CP16 | Entrada de texto en división | dividir("diez", 2) | TypeError | TypeError | PASSED |
| CP17 | None en división | dividir(10, None) | TypeError | TypeError | PASSED |
| CP18 | Texto en resta | restar("a", 1) | TypeError | TypeError | PASSED |
| CP19 | Texto en multiplicación | multiplicar(2, "3") | TypeError | TypeError | PASSED |
| CP20 | Booleano / lista / None en multiplicación | multiplicar(True, 1), etc. | TypeError | TypeError | PASSED |

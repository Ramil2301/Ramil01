def func(x):
    """Вычесляет ли правильно.
 >>> func(0)
     1.0
 >>> func(1)
     5.0
     
     """
    return float(x**4+4**x)

import doctest
    #втоматически проверяет тест в документе
doctest.testmod()

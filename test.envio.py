# test_envio.py
from envio import calcular_costo_envio

def test_casos_base_y_frontera():
    # Casos normales
    assert calcular_costo_envio(400) == 100
    assert calcular_costo_envio(700) == 50
    assert calcular_costo_envio(1200) == 0

    # Casos Frontera
    assert calcular_costo_envio(499.99) == 100
    assert calcular_costo_envio(500.00) == 50
    assert calcular_costo_envio(999.99) == 50
    assert calcular_costo_envio(1000.00) == 0
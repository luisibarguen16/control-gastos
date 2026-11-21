from control_de_gastos import Control_Gasto

def test_guardar_informacion(tmp_path):
    ruta = tmp_path / "usuario_gastos.json"
    control = Control_Gasto("luis", 1000, str(ruta))
    assert control.total == 0
    
    
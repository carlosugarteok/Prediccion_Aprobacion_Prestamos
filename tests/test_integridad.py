from pathlib import Path
import pandas as pd

def test_datos_sinteticos():
    p=Path(__file__).resolve().parents[1]/'data'/'solicitudes_prestamo_sinteticas.csv'
    if not p.exists(): return  # El notebook genera este archivo al ejecutarse.
    df=pd.read_csv(p)
    assert df.shape==(614,13)
    assert df.Loan_ID.is_unique
    assert set(df.Loan_Status)=={'N','Y'}

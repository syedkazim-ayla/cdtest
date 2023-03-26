from calc import Calc

def test_add():
  calc=Calc()
  result=calc.add(1,2)
  assert result==3

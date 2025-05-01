# pytest is n tool to point out mistake
import cal
def test_main():
  result = cal.add(2,5)
  assert result == 7, "5 + 2 is equall to 7"  # isky through errors ko find krskty hain
  result = cal.add(0,0)
  assert result == 0, "0+ 0is equall to 0" 
  result = cal.add(5,0)
  assert result == 5, "5 + 0 is equall to 5" 
  result = cal.add(-2,-2)
  assert result == -4, "-2 + -2 is equall to -4" 
  

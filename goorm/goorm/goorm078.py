from datetime import *

print("오늘 =",datetime.now())
hundred=timedelta(days=100)
plus100day=datetime.now()+hundred
print("100일 후 =",plus100day)
minus100day=datetime.now()-hundred
print("100일 전 =",minus100day)
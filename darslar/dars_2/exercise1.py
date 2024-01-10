# data types
# decimal type
from decimal import Decimal,getcontext,Context
import decimal

new_context = Context(prec=9,rounding=decimal.ROUND_UP)
decimal.setcontext(new_context)
print(Decimal(0.3432)-Decimal(0.2324))



print(Decimal(0.1))
print(float(0.1))
print(Decimal(0.3))
print(0.15+0.15==0.3)
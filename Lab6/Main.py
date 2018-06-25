from Controller import *
from Fuzificare import *

fuz = Fuzificare()
ctrl = Controller(fuz, 'temperature.in', 'capacity.in', 'power.in', 'functionality.in')
r = ctrl.run(100, 2)
print("Defuzificare:", ctrl.getDefuzificare())
print("Fuzificare capacitate:", fuz.fuzificareCapacitate(3, (0, 5)))
print(r)

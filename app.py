weight = input("how much do you weigh?")
metric_system = input("Kg (K) or Lbs (L)")
conversion = 0
if(metric_system.upper() == "L"):
    conversion = int(weight) * 0.45359237
else:
    conversion = int(weight) *2.2

if(metric_system == "L"):
    print(str(conversion) + " Kgs")
else:
    print(str(conversion) + " Lbs")
# Write your code here :-)
print("Tip Calculator SUPERWOOW, Welcome !!")
cuenta = float(input("Write the Total amount of the bill : $"))
propela = int(input("¿ How much is the tip pct. ? 10, 15 0 20 % ?"))
personas = int(input("¿ How many persons will pay the bill ? "))

propelapct = propela/100
cuentapct = cuenta * propelapct
total_con_propela = cuenta + cuentapct
total = total_con_propela / personas

total_final = round( total, 2 )

print(f"Each one must pay : ${total_final}")

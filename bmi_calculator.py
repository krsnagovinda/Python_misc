print(f'Bienvenid@, vamos a calcular tu Indice de Masa Corporal')
print("Welcome, let's calculate your Body Mass Index")
x = int(input("Cuanto mides en cm. ??,  How tall are you in cm? ??"))

estatura = x/100
peso = float(input("Cuanto pesas en kg. ??, How much do you weigh in kg? ?? "))

bmi =  peso / (estatura)**2

resultado = round(bmi, 2)

if bmi < 18.5:
    print("tu imc es: " + str(resultado) + " estas bajo de peso, lo mínimo es 18.5 ")
    print("Your BMI is: " + str(resultado) + " You are underweight, the minimum is 18.5")    

elif bmi < 25:
    print("tu imc es: " + str(resultado) + " estas dentro de lo normal, !!! Felicidades ¡¡¡")
    print("Your BMI is: " + str(resultado) + " You are within normal,!!! Congratulations")    

elif bmi < 30:
    print(" tu imc es: " + str(resultado) + " estas mal, tienes sobrepeso, lo máximo es 25" )
    print("Your BMI is: " + str(resultado) + " You are on overweight, the maximum is 25")    

elif bmi < 35:
    print("tu imc es " + str(resultado) + " cuidado, estas con obesidad ")
    print("Your BMI is: " + str(resultado) + " Beware !! You are obese, the maximun is 25")    

else:
    print("tu imc es " + str(resultado) + " Tienes que ir a Terapia, lo tuyo no es normal, lo máximo es 25 y tu haz sobrepasado el límite")
    print("Your BMI is: " + str(resultado) + " You have to go to therapy, this is not normal, the maximum is 25 and you have exceeded the limit")    




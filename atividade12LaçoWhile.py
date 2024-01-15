#Faça um programa que calcule e mostre a média aritmética de N notas.
average_addiction = 0

student = input("Enter your name:")

for i in range (1, 8):
    input_note = float(input(f"{student}...Enter a note {i}:"))

    average_addiction += input_note


result = average_addiction / 7

print(f"The value of average is {result:.2f}")


#average_addiction = 0
#count_notes = 0

#student = input("Enter your name:")

#While True:
    #input_note = input(f"Enter a note for {student} (or type 'STOP' to finish)")

    #if input_note.upper() == 'STOP':
        #break

#try:
    #input_note = float(input_note)
#except ValueError:
    #print("Invalid input.Please enter a valid number or 'STOP'.")
    #continue

#average_addiction += input_note
#count_notes += 1

#count_notes > 0:
    #result = average_addiction / count_notes
    #print(f"The name of the student is {student}.")
    #print(f"The average is {result:.2f})
#else:
    #print("No notes entered.")
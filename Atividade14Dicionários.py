#Crie um dicionário que relacione nomes de alunos às suas
#notas em uma disciplina. Calcule a média das notas e exiba-a.

student_names = {
    'Maria Eduarda': 88.5,
    'Gustavo': 45.00,
    'Matheus': 65.00,
    'Augusto': 37.0,
    'Alice': 77.5
}

total_notes = sum(student_names.values())
quantity_students = len(student_names)
average_notes = total_notes / quantity_students

print(f"Average notes of students: {average_notes:.2f}")

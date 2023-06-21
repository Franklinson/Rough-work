import random

students = [
    "NYAME BARNABAS", "OTENG SAMUEL BOAMAH", "NIMAKO JOSEPH AGYEKUM",
    "AKROFI ESTHER BOATENG", "DORGBEFU MILLICENT YAWA", "AGGREY CHRISTIAN KOFI",
    "DZIANY LIVINGSTONE", "ADJOKATCHER SAMUEL DORNU", "ADDO ERIC ADU",
    "ADDO JOSEPH", "HORMEKU STELLA", "OBEEL DEBORAH ASABEA", "ATTUAH MICHAEL OSAE"
]

lecturers = {
    "A": [], "B": [], "C": [], "D": [], "E": [], "F": []
}

random.shuffle(students)

letters = list(lecturers.keys())

while students and letters:
    letter = random.choice(letters)
    assigned_students = lecturers[letter]
    student1 = students.pop()
    student2 = students.pop()
    assigned_students.extend([student1, student2])
    letters.remove(letter)

# Assign the remaining students to the last available letter, if any
if students:
    last_letter = letters[0] if letters else None
    if last_letter:
        assigned_students = lecturers[last_letter]
        assigned_students.extend(students[:3])  # Assign three remaining students

# Print the assigned students for each letter
for letter, assigned_students in lecturers.items():
    print(f"Letter {letter} assigned students:")
    for student in assigned_students:
        print(student)
    print()

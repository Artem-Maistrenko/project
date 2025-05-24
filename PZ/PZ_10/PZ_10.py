# Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
# группе студент, который побывал в гостях у всех студентов. (Для каждого студента
# составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
# список не включать).

visits = {
    "Андрей": {"Виктор", "Максим"},
    "Виктор": {"Андрей", "Максим", "Ольга"},
    "Максим": {"Виктор", "Ольга"},
    "Ольга": {"Андрей", "Виктор", "Максим", "Елена"},
    "Елена": {"Ольга", "Дмитрий"},
    "Дмитрий": {"Елена"}
}

all_students = set(visits.keys())
universal_guest = None

for guest in all_students:

    visited_hosts = set()
    for host, guests in visits.items():
        if guest in guests:
            visited_hosts.add(host)

    if visited_hosts == all_students - {guest}:
        universal_guest = guest
        break

if universal_guest:
    print(f"Студент, который был в гостях у всех: {universal_guest}")
else:
    print("Нет студента, который был в гостях у всех.")
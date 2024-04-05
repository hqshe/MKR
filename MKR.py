def compare_files(file1_path, file2_path):
    # Зчитування рядків з файлів
    with open(file1_path, 'r') as file1:
        lines1 = set(file1.readlines())
    with open(file2_path, 'r') as file2:
        lines2 = set(file2.readlines())

    # Порівняння рядків
    same = lines1.intersection(lines2)
    diff = lines1.symmetric_difference(lines2)

    # Запис однакових рядків у файл
    with open('same.txt', 'w') as same_file:
        for line in sorted(same):
            same_file.write(line)

    # Запис унікальних рядків у файл
    with open('diff.txt', 'w') as diff_file:
        for line in sorted(diff):
            diff_file.write(line)

# Припускаємо, що імена файлів надані (вони мають бути змінені на відповідні шляхи до файлів)
compare_files('file1.txt', 'file2.txt')

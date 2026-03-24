def students_and_evaluations(students, result):
    try:
        with open(students, 'r', encoding='utf-8') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print(f"Файл {students} не найден")
        return

    except Exception as e:
        print(f"Ошибка при чтении файла {students}: {e}")
        return

    try:
        with open(result, 'w', encoding='utf-8') as f:
            dict_students = {}
            for line in lines:
                student, evaluations = line.strip().split(':')
                evaluations = evaluations.replace(',', ' ')
                lst_evaluations = []
                for evaluation in evaluations.split():
                    clean_evaluation = evaluation.strip('@#№$%&!?;:*^<>,.|/ ')
                    if clean_evaluation.isdigit():
                        lst_evaluations.append(int(clean_evaluation))
                dict_students[student] = lst_evaluations

            average_value = []
            for student, evaluations in dict_students.items():
                average = sum(evaluations) / len(evaluations)
                average_value.append((student, average))
                if average > 4:
                    f.write(f"{student} - {average}\n")

        if average_value:
            max_average = max(average_value, key=lambda x: x[1])[1]
            top_students = [student for student, average in average_value if average == max_average]
            print(f"Студенты с наивысшим средним баллом ({max_average}): {', '.join(top_students)}")
        else:
            print("Нет студентов с средним баллом выше 4.0")

    except Exception as e:
        print(f"Произошла ошибка при обработке данных: {e}")

if __name__ == '__main__':
    students_and_evaluations(students='students.txt', result='result.txt')



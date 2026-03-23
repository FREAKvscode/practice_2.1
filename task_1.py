def read_and_write(text):
    with open(text, 'w', encoding='utf-8') as f:
        f.write('Hello World\n')
        f.write('File\n')
        f.write('Python\n')
        f.write('Guido van Rossum\n')
        f.write('Good bye\n')

    with open(text, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count_lines = len(lines)
        count_words = 0
        long_line = ''

        for line in lines:
            words = line.split()
            count_words += len(words)
            if len(line) > len(long_line):
                long_line = line.strip()

    return (f"Количество строк в файле: {count_lines}\n"
            f"Количество слов в файле: {count_words}\n"
            f"Самая длинная строка: {long_line}")


if __name__ == '__main__':
    print(read_and_write(text='text.txt'))



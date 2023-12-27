def find_in_different_registers(word_list: list[str]) -> list[str]:
    uniq_words = []
    iterator_words = iter(word_list)

    for it_word in iterator_words:
        if word_list.count(it_word) > 1:
            word_list = [word for word in word_list if word.lower() != it_word.lower()]
    for word in word_list:
        if word.lower() not in uniq_words:
            uniq_words.append(word.lower())

    return uniq_words


words = ["Мама", "МАМА", "Мама", "папа", "ПАПА", "Мама", "ДЯдя", "брАт", "Дядя", "Дядя", "Дядя"]
print(find_in_different_registers(words))

words = ['МАМА', 'Мама', 'БРАТ', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
print(find_in_different_registers(words))

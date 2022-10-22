def words_sorting(*args):
    word_results = {}
    ordered_dict = {}
    result = ""
    for word in args:
        ascii_sum = 0
        for letter in word:
            ascii_sum += ord(letter)
        word_results[word] = ascii_sum

    if sum(word_results.values()) % 2 == 0:
        ordered_dict = dict(sorted(word_results.items(), key=lambda item: item[0]))
    elif sum(word_results.values()) % 2 == 1:
        ordered_dict = dict(sorted(word_results.items(), key=lambda item: item[1], reverse=True))

    for key, value in ordered_dict.items():
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


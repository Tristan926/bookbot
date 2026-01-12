def get_num_words(book_text):
	num_words = 0
	for word in book_text.split():
		num_words += 1
	return num_words

def get_num_characters(book_text):
	num_characters = {
	}
	for letter in book_text.lower():
		if letter not in num_characters:
			num_characters[letter] = 0
		num_characters[letter] += 1
	return num_characters

def sort_on(item):
    return item["num"]  # which key holds the count?

def sort_dictionary(num_characters):
    list_of_dicts = []
    for char, count in num_characters.items():
        if not char.isalpha():
            continue
        mini_dict = {
            "char": char,   # which variable is the character?
            "num":  count,   # which variable is the count?
        }
        list_of_dicts.append(mini_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)  # which function goes here?
    return list_of_dicts

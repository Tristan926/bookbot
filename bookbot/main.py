import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)


def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text(sys.argv[1])
	word_count = get_num_words(book_text)
	num_characters = get_num_characters(book_text)
	sorted_chars = sort_dictionary(num_characters)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for item in sorted_chars:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")
	print(f"{word_count} words found in the document")
	print(f"{num_characters}")
main()

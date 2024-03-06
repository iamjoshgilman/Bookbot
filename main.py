
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted_dict = sorted_output(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    # print(num_letters)
    print(sorted_dict)
    print("--- End Report ---")

def sorted_output(num_letters):
    sorted_output = []
    sorted_dict = {keys: num_letters[keys] for keys in sorted(num_letters)}
    for key, value in sorted_dict.items():
        if key.isalpha():
            sorted_output.append(f"The '{key}' character was found {value} times")
    return "\n".join(sorted_output)

def get_num_letters(text):
    num_letters = {}
    text = text.lower()
    for letter in text:
        if letter not in num_letters:
            num_letters[letter] = 1
        else:
            num_letters[letter] += 1
    return num_letters

def get_num_words(text):
    words =  text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
import re

def remove_text(sentences):
    cleaned_sentences = re.sub(r'[^\w\s\♥]', '', sentences) #지울특수 문자들

    return cleaned_sentences

def remove_num(sentences):
    cleaned_sentences = ''.join(char for char in sentences if char.isalpha() or char.isspace())

    return cleaned_sentences

def add(sentences):
    sentences_list = remove_text(sentences).split()

    quoted_sentences = [f'"{sentence}",\n' for sentence in sentences_list]

    result = " ".join(quoted_sentences)

    return result

input_sentences = """"넣을거^"""

input_sentences = remove_num(input_sentences)

result = add(input_sentences)
print(result)

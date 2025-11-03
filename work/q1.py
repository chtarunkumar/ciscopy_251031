words=input('words(separated by space)')
print(words)
word=words.split()
print(word,type(word))
words_tuple=tuple(word)
print(words_tuple,type(words_tuple))

with open('qn01_data.txt','w') as output_file:
    output_file.write(f'list:{word}')
    output_file.write(f'tuple:{words_tuple}')

with open('qn01_data.txt','r') as input_file:
    file_words_list=input_file.readline()
    file_words_tuple=input_file.readline()
    print(file_words_list)
    print(file_words_tuple)
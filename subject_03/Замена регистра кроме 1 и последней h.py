def change_h(text):
    first_h_index = text.find('h')
    last_h_index = text.rfind('h')

    result = text[:first_h_index+1] + text[first_h_index+1:last_h_index].replace('h', 'H') + text[last_h_index:]
    return result


text = 'hhdhschehthhyyhh'
new_text = change_h(text)
print(new_text)
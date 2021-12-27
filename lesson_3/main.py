words=[
'python',
'cobol',
'c++',
'c',
'scala',
'paskal',
'java',
'basic'
]
letter="c"

def count_letter (words, letter):
    count=0
    for word in words:
        if letter in word:
            count += 1
    return count
result = count_letter (words, letter)
print (result)
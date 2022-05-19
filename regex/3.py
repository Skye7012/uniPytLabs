import re
text = 'A, very very; irregular_sentence'  
print(re.findall('\w+', text)) # Все кроме букв и цифр     

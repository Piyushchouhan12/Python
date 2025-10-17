letter = str('''Dear <|Name|>,
You are selected!
<|Date|>''')
letter_new = str('''Dear <|Name|>,
 \tYou are selected!
\t<|Date|>''')
print(letter_new.replace("<|Name|>" , "Piyush").replace("<|Date|>" , "17_OCT_25"))

 
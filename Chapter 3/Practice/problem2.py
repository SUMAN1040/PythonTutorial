letter = '''Dear <|Name|>, 
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>", "Suman").replace("<|Date|>", "21/01/2026"))#here we can chaining the .replace()
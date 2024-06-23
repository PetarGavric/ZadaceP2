import re

regex = r'^A(?=.*[0-5])(?=.*\s).*P$'

test_unosa = [
    "A1 B2P",    
    "A test 3P", 
    "A5 0P",     
    "A0P",      
    "A P"        
]

matches = {test: bool(re.match(regex, test)) for test in test_unosa}
print(matches)

#!/usr/bin/python3
#!/usr/bin/python3
def remove_char_at(string, i):
if i >= 0:
string_1 = string[:i]
string_2 = string[i + 1:]
string = string_1 + string_2
return string

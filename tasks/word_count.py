# enter file name:
file_name = input("Enter the file name: ")
# start loop to count words
try:
    text = open(file_name, 'r')
    d1 = dict()
    punctuations = "!()-[]{};:',<>./?@#$%^&*_~"
    for lines in text:
        lines = lines.strip()
        lines = lines.lower()
        lines = lines.replace(".", "")
        lines = lines.replace(",", "")
        lines = lines.replace("?", "")
        lines = lines.replace("!", "")
        lines = lines.replace(":", "")
        lines = lines.replace(";", "")
        lines = lines.replace("'", "")
        words = lines.split(" ")
        for word in words:
            if word in d1:
                d1[word] = d1[word] + 1
            else:
                d1[word] = 1
    for k in d1.keys():
        print('Word: %s appears %s time(s).' % (k, d1[k]))
except:
    print("File not found.")

#I also saw this approach to replacing punctuation, but couldn't get it to work properly:
# punctuation = '''.,:;()[]{}/&'/n-?!+'''
# text_clean = ""

# for char in text:
#   if char not in punctuation:
#      text_clean = text_clean + char

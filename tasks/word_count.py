file_name = input("Enter the file name: ")
try:
    text = open(file_name, 'r')
    d1 = dict()
    punctuations = "!()-[]{};:',<>./?@#$%^&*_~"
    for lines in text:
        lines = lines.strip()
        lines = lines.lower()
        for x in punctuations:
            lines = lines.replace(x, "")
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
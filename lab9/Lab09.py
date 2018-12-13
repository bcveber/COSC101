def read_prompts(fileName):
    f = open('Chinchillas.txt')
    promptList = []
    line = f.readline()
    line = line.strip()
    while line != '***end of prompts***':
        promptList += [line]
        line = f.readline()
        line = line.strip()
    return promptList
        
def ask_prompts():
    responses = []
    promptList = read_prompts('Chinchillas.txt')
    for line in promptList:
        line = line + ': '
        one_response = input(line)
        responses += [one_response]
    return responses

def read_template(fileName):
    f = open('ShortTemplate.txt')
    wordtemplate = []
    line = f.readline()
    line = line.strip()
    marker = False
    while line !='':
        if line == '***end of prompts***\n':
            marker = True
        if marker == True:
            wordtemplate += [line]
        line = f.readline()
    return wordtemplate[1: ]

def replace_prompts(line, responses):
    newtemplate = []
    template = read_template('Chinchillas.txt')
    for line in template:
        newtemplate +=[line]
        for answer in responses:
            replacers = ['|0|','|1|','|2|','|3|','|4|','|5|','|6|','|7|','|8|','|9|','|10|']
            if line.find() == replacers:
                line.replace(replacers, answer)
                newtemplate += [line]
    print (newtemplate)
                
    


replace (old, new)




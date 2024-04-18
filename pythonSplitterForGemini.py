
questions=[]
answers=[]
options=[]
wrongAnswers=[]
lines=[]
numbers=[]
def convert_text_to_question(text_input_original):
    
    text_input=text_input_original.replace("\n"," ")
    number=text_input.split("**Question 2:**",1)[0]
    remaining=text_input.split("**Question 2:**",1)[1]
    numbers.append(number)
    number=remaining.split("**Question 3:**",1)[0]
    remaining=remaining.split("**Question 3:**",1)[1]
    numbers.append(number)
    numbers.append(remaining)
    for i in range(len(numbers)):
        question=numbers[i].split("(a)",1)[0]
        if "**Question 1:**" in question:
            question=question.replace("**Question 1:**"," ").strip()
        questions.append(question)
        remain=numbers[i].split("(a) ",1)[1]
        option=remain.split("(b) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(b) ",1)[1]
        option=remain.split("(c) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(c) ",1)[1]
        option=remain.split("(d) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(d) ",1)[1].strip()
        option=remain.split("**Correct Answer:**",1)[0].strip()
        options.append(option)
        remain=remain.split("**Correct Answer:**",1)[1].strip()
        answers.append(remain)
     
    for i in range(len(answers)):
        if "(a)" in answers[i]:
            answers[i]=answers[i].replace("(a) ","")
        elif "(b)" in answers[i]:
            answers[i]=answers[i].replace("(b) ","")
        elif "(c)" in answers[i]:
            answers[i]=answers[i].replace("(c) ","")
        elif "(d)" in answers[i]:
            answers[i]=answers[i].replace("(d) ","")
        
    for i in range(0,len(options)):
        
       if not(options[i] == answers[0] or options[i] == answers[1] or options[i] == answers[2]):
           wrongAnswers.append(options[i])
            
               
    
    for p in range(len(answers)):
        print(answers[p])
    
    return len(wrongAnswers)
    
                 
print(convert_text_to_question(input("Enter your text:")))
     
     
def display():
    if len(questions) != 0:
        
        return options[2]
    else:
        return  "no string"      
        
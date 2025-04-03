"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: Junior ROBERT

#----------------------------------------------------------------

#Quesiton 1



course_names=["Data Structures and Algorithm 1","Computer Programming 1","Calculus 1","Set Theory and Lgic",
              "Discrete Mathematics 1"]



#Question 2


MCS_253_std_IDs=("2023314260","2023314233","202412245","202412253","202412232","202412236")



#Question 3


students_records={2023314260:{'Name':'Jonah ALBERT','Gender':'Male','DOB':'09/05/2004','Province':'Central',
                              'Email adress':'2023314260@stu.unigoroka.ac.pg'},
                  2023314233:{'Name':'Rophie NOMORU','Gender':'Male','DOB':'19/10/2002','Province':'Morobe',
                              'Email adress':'2023314233'},
                    202412245:{'Name':'Margreth KURI','Gender':'Female','DOB':'18/12/1998','Province':'Jiwaka',
                               'Email adress':'kurimargreth@gmail.com'},
                    202412253:{'Name':'Junior ROBERT','Gender':'Male','DOB':'12/10/2000','Province':'Jiwaka',
                                 'Email adress':'juniorwalrob127@gmail.com'},
                    202412232:{'Name':'Dahan TIMINAI','Gender':'Male','DOB':'11/11/2001','Province':'Western',
                               'Email adress':'timinaidahan@gmail.com'},
                    202412236:{'Name':'Natasha RICKY','Gender':'Female','DOB':'05/07/1998','Province':'Eastern Highland',
                               'Email adress':'202412236@stu.unigoroka.ac.pg'} }



#Question 4


print(course_names[1])


#Question 5


print(MCS_253_std_IDs[3])


#Question 6


print(students_records.values())

#Question 7


print(students_records[202412253])



#Question 8

"""we have AttributeError when' append' is used and TypeError when' del' or 'remov' is used.That means it
 is a tuple,meaning that it is immuteabble(cannot be modified,added'removed or updated)"""


#Question 9


print(type(course_names))
print(type(MCS_253_std_IDs))
print(type(students_records))
print(type(course_names[1]))
print(type(MCS_253_std_IDs[3]))
print(type(students_records.values()))
print(type(students_records[202412253]))





#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 
# Big_Data_programming_1
Project Title : husHUsh Recruiter In this project we tried to automate the job hiring process by dividing the process into 3 steps:

Shortlist a candidate based on the consideration of various data points and applying a selection algorithm

Sending an email to the shortlisted candidate in python to attempt a test in the next round of interview

Selecting a candidate by applying another selection algorithm.

Motivation The main idea in trying to develop the project is to understand how we could use python programming languange and its libraries to automate a particular process

Build Status The project is in completed status with no bugs or issues

Code Style We have used standard code style in this project using python programming language

Tech/Framework used This project was developed using python programming with the help of pandas data frame to shorlist a candidate We have also used object oriented programming to select the candidate

Features Application of pandas dataframe in python Application of Object Oriented Programming

Code Examples

To shortlist a candidate

#Checking for condition to select the candidate for i,j in df.iterrows(): if j['total_points']>=8: df.at[i,'Candidate_shortlisted']='Yes' else: df.at[i,'Candidate_shortlisted']='No'

Filtering columns based on condition
final_list_df=df[df["Candidate_shortlisted"]=="Yes"]

print(final_list_df)
filtered_information_df=final_list_df.filter(["First_Name","Last_Name","Email_address","Candidate_shortlisted"])

print(filtered_information_df)
Converting the data frame variable to csv
filtered_information_df.to_csv('selected_candidates_list.csv', index=False)
To select a candidate
test=TestFunc(question_bank) while test.still_has_questions(): test.next_question()

if test.score >=7: print(f"Your final score is {test.score}/{test.question_number}") print("Congratulations , you have been selected to join Doodle ") else: print(f"Your final score is {test.score}/{test.question_number}") print("Sorry , you were unable to clear the interview process. Better luck next time!")

API reference https://api.github.com/search/repositories?q=created:">2018-09-30"language:python&sort=stars&order=desc https://docs.github.com/en/rest/reference/search#search-repositories

Tests

The weights for each data point could be altered to select the candidate

for i,j in df.iterrows(): k=(j['Gold_badges(stack_overflow)']) # print(k)

if k > mean_gold_badges_stack:
    df.at[i,'points_gold_badges_stack']=2 
else:
    df.at[i,'points_gold_badges_stack']=0 
The cut off criteria to select a candidate could be altered
if test.score >=7: print(f"Your final score is {test.score}/{test.question_number}") print("Congratulations , you have been selected to join Doodle ")

10.How to Use? The project has been split into 3 parts which occurs sequentially

Process to shortlist a candidate - we have used pandas dataframe in python to create calculate new columns and compare it with the mean of the data points to shortlist a candidate
Send an email in python to the selected candidate
Process to select a candidate- Provide the shortlisted candidate with an interface to answer some questions. They need to clear a cut off mark to get into Doodle

import pandas as pd
df=pd.read_csv('BDP_project.csv')

#print first 5 records of the dataframe
print(df.head())

#Calculating the mean of each column for the data point selected
mean_starred_rep=df["Starred_repositories(git_hub)"].mean()
mean_followers_git=df["Followers(git_hub)"].mean()
mean_reputaion_stack=df["Reputation(stack_overflow)"].mean()
mean_gold_badges_stack=df["Gold_badges(stack_overflow)"].mean()
mean_answers_stack=df["Answers(stack_overflow)"].mean()
mean_certification_linkedin=df["Certifications(linkedin)"].mean()
mean_endorsements_linkedin=df["Endorsements(linkedin)"].mean()

#Creating a calculated column(points) based on the provided condition

for i,j in df.iterrows():
    k=(j['Starred_repositories(git_hub)'])
    # print(k)

    if k > mean_starred_rep:
        df.at[i,'points_star_rep']=2 
    else:
        df.at[i,'points_star_rep']=0 

# print(df.head())



# df.iloc[1,3]

# for i,j in df.iterrows():
#     k=(j['Followers(git_hub)'])
#     # print(k)

#     if k > mean_followers_git:
#         df.at[i,'points_followers_git']=2 
#     else:
#         df.at[i,'points_followers_git']=0 

# for i,j in df.iterrows():
#     k=(j['Reputation(stack_overflow)'])
#     # print(k)

#     if k > mean_reputaion_stack:
#         df.at[i,'points_reputation_stack']=2 
#     else:
#         df.at[i,'points_reputation_stack']=0 

# for i,j in df.iterrows():
#     k=(j['Gold_badges(stack_overflow)'])
#     # print(k)

#     if k > mean_gold_badges_stack:
#         df.at[i,'points_gold_badges_stack']=2 
#     else:
#         df.at[i,'points_gold_badges_stack']=0 

# for i,j in df.iterrows():
#     k=(j['Answers(stack_overflow)'])
#     # print(k)

#     if k > mean_answers_stack:
#         df.at[i,'points_answers_stack']=2 
#     else:
#         df.at[i,'points_answers_stack']=0 

# for i,j in df.iterrows():
#     k=(j['Certifications(linkedin)'])
#     # print(k)

#     if k > mean_certification_linkedin:
#         df.at[i,'points_certification_linkedin']=1 
#     else:
#         df.at[i,'points_certification_linkedin']=0 

# for i,j in df.iterrows():
#     k=(j['Endorsements(linkedin)'])
#     # print(k)

#     if k > mean_certification_linkedin:
#         df.at[i,'points_endorsements_linkedin']=1 
#     else:
#         df.at[i,'points_endorsements_linkedin']=0 

#Creating a calculated column to find the total points earned
# sum_column = df['points_followers_git']+df['points_reputation_stack']+df['points_gold_badges_stack']+df['points_answers_stack']+df['points_certification_linkedin']+df['points_endorsements_linkedin']
# df["total_points"] = sum_column

# df.to_csv('updated_candidates_list.csv', index=False)

# print(df.head())

#Checking for condition to select the candidate
# for i,j in df.iterrows():
#     if j['total_points']>=8:
#         df.at[i,'Candidate_shortlisted']='Yes'
#     else:
#         df.at[i,'Candidate_shortlisted']='No'

# Filtering columns based on condition
# final_list_df=df[df["Candidate_shortlisted"]=="Yes"]
# print(final_list_df)
# filtered_information_df=final_list_df.filter(["First_Name","Last_Name","Email_address","Candidate_shortlisted"])
# print(filtered_information_df)

# Converting the data frame variable to csv
# filtered_information_df.to_csv('selected_candidates_list.csv', index=False)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading in the clean data
student_df = pd.read_csv('data_clean/clean_StudentPerformance.csv')

######################################
#garph 1
#####################################

#this bar helps to find out if the test preparation course helped student improve their test score or not

#calculate mean of avg score for each attribute in the test preparation course cal
df_groups = student_df.groupby('test preparation course')['avg score'].mean()

#create bar plot by group
df_groups.plot(kind='bar')
plt.savefig('results/test_prep_course.png')
plt.close()

###############################
#graph
##############################

#this histogram graph shows each race group scored on the test
#from the graph its clear that the students from the group E scored higher score than other groups
#And group A had more score on lower end of spectreum

eth_df = student_df[['race/ethnicity', 'avg score']]
eth_df.plot.hist(by='race/ethnicity',subplots=True, layout=(3,2), figsize=(10, 10), bins=20)
plt.savefig('results/race_scores.png')
plt.close()

############################
#graph 2 
############################

#in this graph we study the impact of economic condition on student performance
#this graph suggest that student living in lower income household had worse score

student_df.groupby('lunch')['avg score'].mean().plot(kind='pie', autopct='%1.1f%%')
plt.title('Impact of economic condition on student performance')
plt.savefig('results/eco_cond.png')
plt.close()

################################
#graph 3
################################

#In this graph we check which section of the exam did the students find more diffcult
#result show that the students found the math section slitly harder

score_df = student_df[['math score', 'reading score', 'writing score']]
#taking mean of all the scores
mean_scores = score_df.mean()
# Plotting the bar graph for the mean scores
plt.figure(figsize=(8,5))
plt.bar(mean_scores.index, mean_scores, color=['blue', 'green', 'red'], edgecolor='grey')

# Adding titles and labels
plt.title('Mean Scores of Math, Reading, and Writing')
plt.xlabel('Subjects')
plt.ylabel('Mean Score')
plt.savefig('results/all_avg_score.png')
plt.close()

####################################
#graph 4
###################################

#This graph look over the difference in boys and girls score
#from this graph its clear that girls on avg did better on the exam
#But boys outshined girls in math

# Subjects
subjects = ['Avg Score', 'Math score', 'Reading Score', 'Writing Score']

# Scores of boys and girls in each subject
df_group = student_df.groupby('gender')[['avg score', 'math score', 'reading score', 'writing score']].mean()

boys_scores = df_group.loc['male'].values.tolist() 
girls_scores = df_group.loc['female'].values.tolist()

# Bar width
bar_width = 0.35

# Positions for boys' bars
r1 = np.arange(len(subjects))

# Positions for girls' bars
r2 = [x + bar_width for x in r1]

# Creating the bar graph
plt.figure(figsize=(8,5))
plt.bar(r1, boys_scores, color='blue', width=bar_width, edgecolor='grey', label='Boys')
plt.bar(r2, girls_scores, color='pink', width=bar_width, edgecolor='grey', label='Girls')

# Adding titles and labels
plt.title('Scores of Boys Vs Girls')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.xticks([r + bar_width/2 for r in range(len(subjects))], subjects)

# Adding legend
plt.legend()

plt.savefig('results/boys_vs_girls.png')
plt.close()

##############################
#graph 5
############################

#In this graph we look over how the parent education level impact the performace of the students
#In the graph we have distinstion between the total student in each catagory and the students who had above avg score

total_student = student_df['parental level of education'].value_counts(sort=False)
pass_student = student_df.loc[student_df['avg score'] > 65, 'parental level of education'].value_counts(sort=False)
# Creating a stacked bar plot
plt.figure(figsize=(12,5))
# Bar width
bar_width = 0.4
# Positions of the bars on the x-axis
r = np.arange(len(total_student))
#plotting the graph for total student distributed across the parental level of education
plt.bar(r, total_student, width=bar_width, color='grey', edgecolor='black', label='total student')
#plotting the graph for pass student
plt.bar(r, pass_student, width=bar_width, color='red', edgecolor='grey', label='Above avg student', zorder = 2)

# Adding titles and labels
plt.title('Parental level of education')
plt.xlabel('education Level')
plt.ylabel('stundet count')
plt.xticks(r, total_student.index)

# Adding a legend
plt.legend()

plt.savefig('results/parent_edu.png')
plt.close()

# Extra Credit Assignment
# Group D (Punit,Saad,Lamonte,Scott)

# The output file from Twitter being used is Pokemon.txt

######################################################

import operator

# Ask the user to indicate the number of records to be displayed

n = int(input('Please enter the # of records to display: '))

# Read the file contents into a list of strings for parsing

file = open('/Users/Amy/Documents/ITCS_5102/Pokemon.txt','r',encoding='UTF-8')

contents = file.read().split('\n')

del contents[len(contents)-1]


######################################################

## Part i - The top n users who have tweeted the most over entire timeline ##

# Create a file to write the results to

outFile = open('/Users/Amy/Documents/ITCS_5102/xtraCrdtOutFile1.txt','w',encoding='UTF-8')

users = {}

for x in contents:
    usr_name = x.split(' ')[0]
    if usr_name in users.keys():
        users[usr_name] += 1
    else:
        users[usr_name] = 1

tupleSort = sorted(users.items(),key=operator.itemgetter(1))
tupleSort.reverse()

print('\nThe top '+str(n)+' users who have tweeted the most in this time-frame are: \n')
outFile.write('\nThe top '+str(n)+' users who have tweeted the most in this time-frame are: \n\n')

for j in range(0,n):
    print(tupleSort[j][0]+' ...with '+str(tupleSort[j][1])+' tweet(s)')
    outFile.write(tupleSort[j][0]+' ...with '+str(tupleSort[j][1])+' tweet(s)\n')

# close the output file 

outFile.close()

######################################################

## Part ii - The top n users who have tweeted the most for every hour ##

# Create a file to write the results to

outFile = open('/Users/Amy/Documents/ITCS_5102/xtraCrdtOutFile2.txt','w',encoding='UTF-8')

ref = []

# dictionary to hold a dictionary for each hour represented in Pokemon.txt file

mostPerHour = {}

for x in contents:
    hour = int(x.split('[')[1].split(']')[0].split(':')[1])
    if hour not in ref:
        ref.append(hour)
        mostPerHour[hour]={}
    usr_name = x.split(' ')[0]
    if usr_name in mostPerHour[hour].keys():
        mostPerHour[hour][usr_name] += 1
    else:
        mostPerHour[hour][usr_name] = 1

print('\n\nThe top '+str(n)+' users who have tweeted the most for every hour are: \n')
outFile.write('\n\nThe top '+str(n)+' users who have tweeted the most for every hour are: \n')

for i in list(mostPerHour.keys()):
    print('\nHour: ',i,'\n')
    outFile.write('\n\nHour: '+str(i)+'\n\n')
    tupleSort2 = sorted(mostPerHour[i].items(),key=operator.itemgetter(1))
    tupleSort2.reverse()
    for j in range(0,n):
        print(tupleSort2[j][0]+' ...with '+str(tupleSort2[j][1])+' tweet(s)')
        outFile.write(tupleSort2[j][0]+' ...with '+str(tupleSort2[j][1])+' tweet(s)\n')

# close the output file 

outFile.close()

######################################################

## Part iii - The top n users who have the most followers ##

# Create a file to write the results to

outFile = open('/Users/Amy/Documents/ITCS_5102/xtraCrdtOutFile3.txt','w',encoding='UTF-8')

users_followers = {}

for x in range(0,len(contents)):
    usr_name = contents[x].split(' ')[0]
    follow_cnt = int(contents[x].split('"')[len(contents[x].split('"'))-1].strip().split(' ')[1])
    users_followers[usr_name]= follow_cnt

tupleSort3 = sorted(users_followers.items(),key=operator.itemgetter(1))
tupleSort3.reverse()

print('\nThe top '+str(n)+' users who have the most followers are: \n')
outFile.write('\n\nThe top '+str(n)+' users who have the most followers are: \n\n')

for j in range(0,n):
    print(tupleSort3[j][0]+'\n\t...with '+str(tupleSort3[j][1])+' follower(s)\n')
    outFile.write(tupleSort3[j][0]+'\n\t...with '+str(tupleSort3[j][1])+' follower(s)\n\n')

# close the output file 

outFile.close()

######################################################    

## Part iv - The top n tweets which have the highest retweet counts ##

# Create a file to write the results to

outFile = open('/Users/Amy/Documents/ITCS_5102/xtraCrdtOutFile4.txt','w',encoding='UTF-8')

tweets_retweets = {}

for x in range(0,len(contents)):
    tweet = contents[x][(contents[x].index('"')+1): contents[x].rindex('"')]
    retweet_cnt = int(contents[x].split('"')[len(contents[x].split('"'))-1].strip().split(' ')[0])
    tweets_retweets[tweet]= retweet_cnt

tupleSort4 = sorted(tweets_retweets.items(),key=operator.itemgetter(1))
tupleSort4.reverse()

print('\n\nThe top '+str(n)+' tweets which have the most retweets are: \n')
outFile.write('\n\nThe top '+str(n)+' tweets which have the most retweets are: \n\n')

for j in range(0,n):
    print(tupleSort4[j][0]+'\n\t...with '+str(tupleSort4[j][1])+' retweet(s)\n')
    outFile.write(tupleSort4[j][0]+'\n\t...with '+str(tupleSort4[j][1])+' retweet(s)\n\n')

# close the output file 

outFile.close()

######################################################



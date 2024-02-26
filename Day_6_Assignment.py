import re
# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

# Output
#['#sunny', '#California', '#travel', '#fun']
# Get the words with the hashtags
hashtags = re.findall(r'#\w+', post)
print(hashtags)

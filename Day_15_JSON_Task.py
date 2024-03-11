import json
from pprint import pprint

# Task
# Starting blog_post.json

# Expected output posts_summary.json

# Read a file
with open("blog_post.json", "r") as file:
    data = json.load(file)

posts_summary = []
data1 = data["posts"]
for dt in data1:
    posts_summary.append(
        {
            "title": dt["title"],
            "author": dt["author"],
            "number_of_comments": len(dt["comments"]),
        }
    )

# Now put posts_summary in a dictionary with key as posts_summary
dict = {"posts_summary": posts_summary}
print(dict)

# Now write it to file
with open("posts_summary1.json", "w") as file:
    json.dump(dict, file, indent=4)

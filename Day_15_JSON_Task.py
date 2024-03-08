import json
from pprint import pprint

# Task
# Starting blog_post.json

# Expected output posts_summary.json

# Read a file
with open("blog_post.json", "r") as file:
    data = json.load(file)

# for dt in data:

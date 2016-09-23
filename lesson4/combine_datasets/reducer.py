#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    
    users = {}
    posts = {}
    
    for line in sys.stdin:
        
        # YOUR CODE HERE
        data = line.strip().split("\t")
        type = data[1]
        if type == "A":
            users[data[0]] = data[2:]
        elif type == "B":
            posts[data[0]] = data[2:]
            
    for author_id in posts:
        output = posts[author_id] + users[author_id]
        print('\t'.join(map(str, output)))
        
def canFinish(numCourses, prerequisites):
    c = {p[0]:p[1] for p in prerequisites}
    for pair in prerequisites:
        r = pair[0]
        while True:
            

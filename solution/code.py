from operator import attrgetter
import sys
from collections import defaultdict
from collections import OrderedDict
from copy import copy
from tokenize import Double

sys.stdin = open("solution\input.txt", "r")
sys.stdout = open("solution\output.txt", "w")


class contributor:
    def __init__(self, name, d):
        self.name = name
        self.d = d


class project:
    def __init__(self, name, days, points, bestbefore, req, d):
        self.name = name
        self.days = days
        self.points = points
        self.bestbefore = bestbefore
        self.req = req
        self.d = d
        self.rating = sum(d.values())
        self.pp = int(points) - int(points)


c, p = list(map(int, input().split()))
contributors = []
for i in range(c):
    name, n = input().split()
    d = defaultdict()
    for i in range(int(n)):
        skill, level = input().split()
        d[skill] = int(level)
    contributors.append(contributor(name, d))

# for i in contributors:
#     # print(i.name, i.d)
#     pass
projects = []
for i in range(p):
    d = OrderedDict()
    name, days, points, bestbefore, req = input().split()
    for i in range(int(req)):
        skill, level = input().split()
        d[skill] = int(level)
    projects.append(project(name, days, points, bestbefore, req, d))

# for i in projects:
#     # print(i.name, i.days, i.points, i.bestbefore, i.req, i.d)
#     pass
answers = 0
completed = defaultdict()
projects.sort(key=lambda x: x.pp)
# for i in projects:
#     print(i.name, i.days, i.points, i.bestbefore, i.req, i.d)
#     pass

for i in projects:
    temp = copy(contributors)
    r = int(i.req)
    useful = []
    for k in i.d.items():
        if r > 0:
            for j in temp:
                try:
                    if j.d[k[0]] >= k[1]:
                        useful.append(j.name)
                        temp.remove(j)
                        r -= 1
                        if r == 0:
                            completed[i.name] = useful
                            answers += 1
                        break
                except:
                    pass
print(answers)
for i in completed.items():
    print(i[0])
    print(*i[1])
    
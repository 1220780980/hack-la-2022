import pandas
from matplotlib import pyplot as plt

navigation_events = pandas.read_csv("../data/navigation_events.csv")
assignments = pandas.read_csv("../data/additional/assignments.csv")
discussion_topics = pandas.read_csv("../data/additional/discussion_topics.csv")
discussion = pandas.read_csv("../data/additional/discussions.csv")
enrollments = pandas.read_csv("../data/additional/enrollments.csv")
files = pandas.read_csv("../data/additional/files.csv")
gradebook = pandas.read_csv("../data/additional/gradebook.csv")
module_items = pandas.read_csv("../data/additional/module_items.csv")
pages = pandas.read_csv("../data/additional/pages.csv")

total_time = enrollments.sort_values(by=["user_id"]).drop(index=34)["total_activity_time"]
score = gradebook.sort_values(by=["Student"]).drop(index=0).drop(index=1)["Current Score"]
# for i in range(len(score)):
#     score.iloc[i] = float(score.iloc[i])
# plt.scatter(total_time, score)
# plt.xlabel("Total Activity Time")
# plt.ylabel("Current Score")
# plt.title("Total Activity Time vs Current Score")
for i in range(score.shape[0]):
    print(total_time.iloc[i])
# print(enrollments.sort_values(by=["user_id"])["total_activity_time"])
# print(enrollments.sort_values(by=["user_id"]).drop(index=34))
# print(gradebook.sort_values(by=["Student"]).drop(index=0).drop(index=1)["Current Score"])



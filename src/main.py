import pandas

navigation_events = pandas.read_csv("../data/navigation_events.csv")
assignments = pandas.read_csv("../data/additional/assignments.csv")
discussion_topics = pandas.read_csv("../data/additional/discussion_topics.csv")
discussion = pandas.read_csv("../data/additional/discussions.csv")
enrollments = pandas.read_csv("../data/additional/enrollments.csv")
files = pandas.read_csv("../data/additional/files.csv")
gradebook = pandas.read_csv("../data/additional/gradebook.csv")
module_items = pandas.read_csv("../data/additional/module_items.csv")
pages = pandas.read_csv("../data/additional/pages.csv")

print(navigation_events["session_id"].value_counts())

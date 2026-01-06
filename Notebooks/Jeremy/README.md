**2025-12-23**

------------------------------------------------------------------------------------------------------------------------------------------

First Brainstorm: Hector and I decided to roll with the course recommendation application idea. The goal is to build a website that allows students to easily find and schedule courses based on their preferences using natural language. Currently, to sign up for a course, students need to spend hours browsing through the course catalog, matching that with course explorer and the sections offered, and then finding out about professor ratings and gpa disparity through other third-party resources. Our plan is to congregate all of that data into an application, and then attach a chatbot interface that can be used to efficiently search and schedule courses. We also want to develop an interactive UI that will display tentative schedules similar to how they would appear in schedule generator.

We are going to conduct some preliminary research this week and meet on Friday to decide how to plan out work for the project

------------------------------------------------------------------------------------------------------------------------------------------

**2025-12-25**

------------------------------------------------------------------------------------------------------------------------------------------

**This is the kind of user story we are looking for:**
User types:

“I’m a CompE junior. Need one tech elective + one easy gen ed. No Fridays, and I prefer classes after 11”

App responds:

“I found 14 matching electives + 22 GenEds. Here are 4 schedules that fit.”

Shows 4 schedule cards + right-side schedule grid preview

Click schedule → conflicts none → “lock this class” → regenerate around it

**Here are some helpful links to look at for gathering data:**

UIUC Course Catalog API: https://courses.illinois.edu/cisdocs/api

GitHub containing data used for UIUC Grade Disparity: https://github.com/wadefagen/datasets/blob/main/gpa/raw/sp2025.csv

Rate My Professor API: https://pypi.org/project/RateMyProfessorAPI/

We should start with data processing just from the course catalog. The GPA and Professor Ratings can be enrichments later on. Immediate next step: Start pulling some of the data to see how it lays out. Come up with necessary queries our schema will need to answer.

------------------------------------------------------------------------------------------------------------------------------------------

**2026-1-06**

------------------------------------------------------------------------------------------------------------------------------------------

Created a python script getCourses.py to test retrieving data from the public UIUC Course API.

Instead of the original URL, use the explorer app. It doesn't require authentication and is a publicly available api: https://courses.illinois.edu/cisdocs/explorer

Some useful URLs for schedule data:

http://courses.illinois.edu/cisapp/explorer/schedule/:year 
http://courses.illinois.edu/cisapp/explorer/schedule/:year/:semester -> 
http://courses.illinois.edu/cisapp/explorer/schedule/:year/:semester/:subjectCode -> Courses offered for the subject that semester/year
http://courses.illinois.edu/cisapp/explorer/schedule/:year/:semester/:subjectCode/:courseNumber -> Sections offered that year/semester for a specific course number
http://courses.illinois.edu/cisapp/explorer/schedule/:year/:semester/:subjectCode/:courseNumber/:crn -> Metadata about the specific section CRN

I created a folder called data to store some samples I retrieved from the api, as well as some notes on them

Shift + Alt + F to format XML

Ctrl + Alt + I to activate copilot
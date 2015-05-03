#Populate DB
db.courses.insert(name="Software Engineering", description="Introduction to concurrent systems and programming style.", credits=4, l_t_p="3-0-2")
db.courses.insert(name="Parallel Programming", description="Introduction to concurrent systems and programming style.", credits=4, l_t_p="3-0-2")

db.registered_courses.insert(course_id=1, professor=1, year_=2015, semester=2)
db.registered_courses.insert(course_id=2, professor=2, year_=2015, semester=2)

db.static_vars.insert(name="current_year",int_value=2015,string_value="2015")
db.static_vars.insert(name="current_sem",int_value=2,string_value="2")

db.student_registrations.insert(student_id=1,registered_course_id=1)
db.student_registrations.insert(student_id=1,registered_course_id=2)
db.student_registrations.insert(student_id=4,registered_course_id=1)


db.events.insert(registered_course_id=1,type_=0,name="Project Submission 1: Draft Requirement Document",description="<p><br></p><p>Organise 2 hr meeting of the team to</p><p>-Choose one of the Projects discussed in the class on Wed 21st Jan</p><p>-Discuss the specification of the selected project. Identify the aspects to be explored by team members&nbsp;</p><p>-Document the discussion and the initial specs of the project</p><p><br></p><p>Organise 2nd 2 hr meeting &nbsp;to</p><p>-Share the homework done by each team member</p><p>-Discuss and finalise the specs of the projects</p><p>-Prepare 1 or 2 page document on the draft project specification&nbsp;</p><p><br></p><p>Submit the draft Project Requirement Document by Wed (28) mid night.</p><p>Add title of the project in the group excel sheet</p>",created_at=datetime.now(),deadline=datetime.now()-timedelta(days=-7),late_days_allowed=5)
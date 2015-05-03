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
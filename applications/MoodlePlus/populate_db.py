## Populate DB Script

## clear database
for table in db.tables():
	db(db[table].id>0).delete()

## create 5 students
db.users.insert(
	id=5,
	first_name="Abhishek",
	last_name="Bansal",
	email="abhishek.bansal@gmail.com",
	username="cs5110271",
	entry_no="2011CS50271",
	type_=0,
	password="1",
)

## create 3 professors
db.users.insert(
	id=0,
	first_name="SC",
	last_name="Gupta",
	email="scgupta@cse.moodle.in",
	username="scgupta",
	entry_no="scgupta",
	type_=1,
	password=db.auth_user.password.validate(1),
)


## create 10 courses
db.courses.insert(
	id=0,
	name="Software Engineering",
	code="csl740",
	description="Introduction to the concepts of Software Design and Engineering.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	id=1,
	name="Parallel Programming",
	code="csl730",
	description="Introduction to concurrent systems and programming style.",
	credits=4,
	l_t_p="3-0-2"
)

## create 8 registered courses
db.registered_courses.insert(
	id=0,
	course_id=1,
	professor=1,
	year_=2015,
	semester=2,
	starting_date=datetime(2015,1,1),
	ending_date=datetime(2015,5,10),
)

## register 3 students for 6 courses each out of 8 registered courses
db.student_registrations.insert(student_id=1,registered_course_id=1)
db.student_registrations.insert(student_id=1,registered_course_id=2)
db.student_registrations.insert(student_id=4,registered_course_id=1)

## create 3 assignments in Software engineering course
db.events.insert(registered_course_id=1,type_=0,name="Project Submission 1: Draft Requirement Document",description="<p><br></p><p>Organise 2 hr meeting of the team to</p><p>-Choose one of the Projects discussed in the class on Wed 21st Jan</p><p>-Discuss the specification of the selected project. Identify the aspects to be explored by team members&nbsp;</p><p>-Document the discussion and the initial specs of the project</p><p><br></p><p>Organise 2nd 2 hr meeting &nbsp;to</p><p>-Share the homework done by each team member</p><p>-Discuss and finalise the specs of the projects</p><p>-Prepare 1 or 2 page document on the draft project specification&nbsp;</p><p><br></p><p>Submit the draft Project Requirement Document by Wed (28) mid night.</p><p>Add title of the project in the group excel sheet</p>",created_at=datetime.now(),deadline=datetime.now()-timedelta(days=-7),late_days_allowed=5)

## create 4 threads in Different courses


## Create Static Variables
db.static_vars.insert(
	name="current_year",
	int_value=2015,
	string_value="2015"
)

db.static_vars.insert(
	name="current_sem",
	int_value=2,
	string_value="2"
)





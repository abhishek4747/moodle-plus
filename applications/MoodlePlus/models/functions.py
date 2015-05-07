def isUserRegisteredForCourse(course_code):
	return registered_courses(course_code)>0

def registeredForCourse(course_code):
	if type(course_code)==str:
		course = db(db.courses.code==course_code).select()
		if len(course)<1:
			return -1
		reg_course = db(db.registered_courses.course_id==course.first().id)(db.registered_courses.year_==get_current_year())(db.registered_courses.semester==get_current_sem()).select()
		if len(reg_course)<1:
			return -1
		stu_course = db(db.student_registrations.student_id==auth.user.id)(db.student_registrations.registered_course_id==reg_course.first().id).select()
		if len(stu_course)<1:
			return -1
		return reg_course.first().id
	return -1
		

def getValidThreadTitle(thread):
	return (thread.title.title() if thread.title != None else thread.description[:20]).title()


def getProfileLink(user_id):
	return XML('<a href="/Users/user/1">Abhishek Kumar</a>')
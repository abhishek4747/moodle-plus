def list():
	if auth.is_logged_in():
		return courses_list()

def course():
	course_arg = str(request.args[0])
	course = db(db.courses.code==course_arg).select()
	if len(course)>0:
		course = course.first()
	else:
		raise HTTP(404)
	try:
		year = int(request.args[1])
	except Exception, e:
		year = get_current_year()
	sems = ["summer","break","winter"]
	try:
		sem = str(request.args[2])
		sem = sems.index(sem)
	except Exception, e:
		sem = get_current_sem()

	previous = db((db.registered_courses.course_id==course.id)&(~((db.registered_courses.year_==year)&(db.registered_courses.semester==sem)))).select()
	registered = db(db.registered_courses.course_id==course.id)(db.registered_courses.year_==year)(db.registered_courses.semester==sem).select()

	return dict(course=course, year=year, sem=sem, previous=previous, registered=registered)
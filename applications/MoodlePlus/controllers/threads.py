def index():
	if len(request.args)<1:
		raise HTTP(404)
	return request.args[0]


def new():
	if auth.is_logged_in() and "course_code" in request.vars and "description" in request.vars:
		course_code = str(request.vars["course_code"])
		# check if course is currently registered for this user
		reg_course = registeredForCourse(course_code)
		if reg_course>-1:
			description = str(request.vars["description"]).strip()
			if description!='':
				tid = db.threads.insert(user_id=auth.user.id, registered_course_id=reg_course, description=description)
				return dict(success=True, thread_id=tid)
	return dict(success=False)


def thread():
	try:
		tid = int(request.args[0])
	except Exception, e:
		raise e
	thread = db(db.threads.id==tid).select().first()
	return dict(thread=thread)

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
			title = str(request.vars["title"]).strip()
			if description!='':
				tid = db.threads.insert(user_id=auth.user.id, registered_course_id=reg_course, description=description, title=title)
				return dict(success=True, thread_id=tid)
	return dict(success=False)

def delete():
	thread = db(db.threads.id==request.args[0]).select()
	if len(thread)>0:
		thread = thread.first()
		session.flash = "Thread deleted successfully!!"
		db(db.threads.id==request.args[0]).delete()
		redirect(URL('courses','course',args=[db(db.courses.id==thread.registered_course_id.course_id).select().first().code,'threads']))
	if request.env.http_referer:
		redirect(request.env.http_referer)
	else:
		redirect('/')

@auth.requires_login()
def thread():
	try:
		tid = int(request.args[0])
	except Exception, e:
		raise e
	thread = db(db.threads.id==tid).select().first()
	course = db(db.courses.id==thread.registered_course_id.course_id).select().first()
	comments = get_comments(tid)
	comment_users = []		
	times_readable = []
	for comment in comments:
		comment_users.append(db(db.users.id==comment.user_id).select().first())
		times_readable.append(timeHuman(comment.created_at))
	return dict(thread=thread, comments=comments, course=course, comment_users=comment_users, times_readable=times_readable)

def get_comments(thread_id):
	return db(db.comments.thread_id==thread_id).select()

def comments():
	try:
		tid = int(request.vars["thread_id"])
	except Exception, e:
		raise e
	return dict(comments=get_comments(tid))

@auth.requires_login()
def post_comment():
	if "description" not in request.vars:
		raise HTTP(404)
	try:
		tid = int(request.vars["thread_id"])
	except Exception, e:
		raise e

	try:
		description = str(request.vars["description"]).strip()	
	except Exception, e:
		raise e
	if db(db.threads.id==tid).count()<1:
		return dict(success=False, err_msg="Invalid Thread Id")
	comment_id = db.comments.insert(thread_id=tid, user_id=auth.user.id, description=description)
	comment = db(db.comments.id==comment_id).select().first()
	return dict(success=True, comment=comment, user_name=(auth.user.first_name+" "+auth.user.last_name).title(), time_readable=timeHuman(comment.created_at))


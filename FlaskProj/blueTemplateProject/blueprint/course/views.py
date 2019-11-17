from blueprint.course import course


@course.route('/')
def course():
    return 'hello,course'

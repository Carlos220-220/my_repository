from blueprint.user import user


@user.route("/")
def index():
    return "hello user"

from TestLou import app
from flask import render_template, Response
from TestLou.models import Course, Label, User
from flask import request
from sqlalchemy import and_
import random
import os
import hashlib
from flask import redirect
from TestLou.models import db
from TestLou import api
from flask_restful import Resource


@app.route("/register/", methods=["get", "post"])
def register():
    status = 0
    now_status = cookie_valid(status)
    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User()
        user.u_name = username
        user.u_password = set_password(password)
        user.u_email = email
        user.save()

    return Response(render_template("index.html", **locals()))


@app.route('/login/', methods=["get", "post"])
def login():
    response = Response(render_template("index.html", **locals()))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(u_email=email).first()
        if user:
            request_password = set_password(password)
            if request_password == user.u_password:
                response.set_cookie("email", user.u_email)
    return response


@app.route('/logout/')
def logout():
    response = redirect("/")
    response.delete_cookie("email")
    return response


def cookie_valid(status):
    get_cookie = request.cookies.get("email")
    if get_cookie:
        status = 1  # 检验是否含有cookie,含有就返回1,没有则是0
    return status


def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


@app.route('/', methods=["get", "post"])
def index():
    status = 0
    now_status = cookie_valid(status)
    register = request.args.get("register")
    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User()
        user.u_name = username
        user.u_password = set_password(password)
        user.u_email = email
        user.save()
        register = True
    response = Response(render_template("index.html", **locals()))
    return response


@app.route('/course/<path:url_arg>/')
def course(url_arg):
    status = 0
    now_status = cookie_valid(status)
    label_list = Label.query.all()
    search_key = request.args.get('search')
    if search_key:
        course_list = Course.query.filter(
            Course.c_name.like("%{}%".format(search_key))
        ).all()
    else:
        args = url_arg.split('/')
        len_arg = len(args)
        c_type = ""
        label = ""
        referer_url1 = ""
        referer_url2 = ""

        if len_arg == 2:
            c_type, label = args
            referer_url1 = "/course/%s/" % c_type
            referer_url2 = label + "/"
            label_id = Label.query.filter_by(l_name=label)[0].id
            course_list = Course.query.filter(
                and_(
                    Course.c_type == int(c_type),
                    Course.label_id == label_id
                )
            )
        elif len_arg == 1:
            arg, = args
            if arg.isdigit():
                c_type = arg
                referer_url1 = "/course/%s/" % c_type
                if int(c_type) == 3:
                    course_list = Course.query.all()
                else:
                    course_list = Course.query.filter_by(c_type=int(c_type))
            else:
                label = arg
                referer_url1 = label + "/"
                course_list = Course.query.filter_by(l_name=label)[0].c_label
    return render_template('course.html', **locals())


@app.route('/show/')
def show():
    status = 0
    now_status = cookie_valid(status)
    return render_template('show.html', **locals())


@app.route('/al/')
def add_label():
    string = "Python C C++ Linux Web 信息安全 PHP Java NodeJS Android GO Spark 计算机专业课 Hadoop HTML5 Scala Ruby R 网络 Git " \
             "SQL NoSQL 算法 Docker Swift 汇编 Windows UI CAD"
    for i in string.split(' '):
        label = Label()
        label.l_name = i
        label.description = "%s课啊,是真滴好啊" % i
        label.save()
    return "Save success!"


@app.route('/add_msg/')
def add_msg():
    lst = [
        {'src': 'https://dn-simplecloud.shiyanlou.com/ncn63.jpg', 'alt': '新手指南之玩转实验楼'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/ncn1.jpg', 'alt': 'Linux 基础入门（新版）'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1480389303324.png', 'alt': 'Kali 渗透测试 - 后门技术实战（10个实验）'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1480389165511.png', 'alt': 'Kali 渗透测试 - Web 应用攻击实战'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482113947345.png', 'alt': '使用OpenCV进行图片平滑处理打造模糊效果'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482807365470.png', 'alt': '使用 Python 解数学方程'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482215587606.png', 'alt': '跟我一起来玩转Makefile'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1480386391850.png', 'alt': 'Kali 渗透测试 - 服务器攻击实战（20个实验）'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482113981000.png', 'alt': '手把手教你实现 Google 拓展插件'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482113522578.png', 'alt': 'DVWA之暴力破解攻击'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1482113485097.png', 'alt': 'Python3实现简单的FTP认证服务器'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1481689616072.png', 'alt': 'SQLAlchemy 基础教程'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1481511769551.png', 'alt': '使用OpenCV&&C++进行模板匹配'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1481512189119.png', 'alt': 'Metasploit实现木马生成、捆绑及免杀'},
        {'src': 'https://dn-simplecloud.shiyanlou.com/1480644410422.png', 'alt': 'Python 3 实现 Markdown 解析器'},
    ]
    for j in range(25):
        for i in lst:
            c = Course()
            c.c_name = i["alt"]
            c.description = i["alt"]
            c.picture = i["src"]
            c.show_number = random.randint(9999, 99999)
            c.c_time_number = random.randint(9999, 99999)
            c.c_type = random.randint(0, 2)
            c.course_label = random.choice(Label.query.all())

            # c.label_id = random.choice(Label.query.all()).id
            c.save()

    return 'Save success!'


class CourseApi(Resource):
    def __init__(self):
        self.result = {
            "version": "v1",
            "code": "200",
            "data": [],
            "methods": "",
            "pagination": {}
        }

    def to_dict(self, obj):
        query_str = str(obj.query).split("SELECT")[1].split("FROM")[0].strip()
        key_list = [k.split(" AS ")[1].replace("course_", "") for k in query_str.split(",")]
        obj_to_dict = dict(
            zip(key_list, [getattr(obj, key) for key in key_list])
        )
        return obj_to_dict

    def get(self, id=None, page=None, page_num=None, field=None, value=None):
        if id:
            course_list = Course.query.get(int(id))
            data = self.to_dict(course_list)
            self.result["data"].append(data)
        else:
            if page == "page":
                page_obj = Course.query.order_by(db.desc("id")).paginate(int(page_num), 15)
                if field and str(value):
                    dicts = {field: value}
                    page_obj = Course.query.filter_by(**dicts).paginate(int(page_num), 15)
                self.result["pagination"]["has_next"] = page_obj.has_next
                self.result["pagination"]["has_prev"] = page_obj.has_prev
                self.result["pagination"]["next_num"] = page_obj.next_num
                self.result["pagination"]["page"] = page_obj.page
                self.result["pagination"]["pages"] = page_obj.pages
                self.result["pagination"]["per_page"] = page_obj.per_page
                self.result["pagination"]["prev_num"] = page_obj.prev_num
                self.result["pagination"]["total"] = page_obj.total
                course_list = page_obj.items
            else:
                if field and str(value):
                    dicts = {field: value}
                    course_list = Course.query.filter_by(**dicts).all()
                else:
                    course_list = Course.query.all()
            self.result["data"] = [self.to_dict(i) for i in course_list]
        self.result["methods"] = request.method
        return self.result


@app.route('/get_test/')
def get_test():
    req = int(request.args.get("page", 1))
    page_size = 5
    start = (req - 1) * page_size
    course_list = Course.query.offset(start).limit(page_size).all()
    return render_template('request_ex.html', **locals())


@app.route('/post_test/', methods=["GET", "POST"])
def post_test():
    course = ""
    label_list = Label.query.all()
    if request.method == 'POST':
        data = request.form
        c_name = data.get("c_name")
        show_number = data.get("show_number")
        c_time_number = data.get("c_time_number")
        label = data.get("label")
        description = data.get("description")
        logo = request.files.get("logo")

        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "static\img\%s" % logo.filename
        )
        logo.save(file_path)
        course = Course()
        course.c_name = c_name
        course.show_number = show_number
        course.description = description
        course.c_time_number = c_time_number
        course.picture = "img\%s" % logo.filename
        course.course_label = Label.query.get(int(label))
        course.save()

    return render_template("request_ex.html", **locals())


api.add_resource(
    CourseApi,
    "/CourseApi/",
    "/CourseApi/<int:id>/",
    "/CourseApi/<string:field>/<string:value>/",
    "/CourseApi/<string:field>/<string:value>/<string:page>/<int:page_num>/",
    "/CourseApi/page/<string:page>/<int:page_num>/",

)


@app.route("/ajax_vue/")
def course_page():
    return render_template("ajax+vue.html", **locals())


@app.route("/login_ajax/", methods=["get", "post"])
def valid_ajax():
    result = {"is_user": False}
    if request.method == "POST":
        get_email = request.form.get("email")
        get_password = request.form.get("password")
        user = User.query.filter_by(u_email=get_email).first()
        if user:
            post_password = set_password(get_password)
            if post_password == user.u_password:
                result["is_user"] = True
    return result


@app.route("/register_ajax/")
def register_ajax():
    result = {"is_exist": True}
    get_email = request.args.get("email")
    user = User.query.filter_by(u_email=get_email)
    if not user:
        result["is_exist"] = False
    return result

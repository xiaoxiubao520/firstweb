from flask import Flask, render_template,redirect,request,url_for,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from password_check import validate_password
from Db import Config
from io import BytesIO
import base64,os
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from yanzhengma import check_code
class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer,primary_key=True)
        User_name = db.Column(db.String(10),unique=True)
        User_password = db.Column(db.String(16))

        def __repr__(self) -> str:
             return f"{{username:{self.User_name}}}"
        
@app.route('/')
def index():
    if request.args.get("tk") == "quit" and session.get("username"):
        session.pop('username')
        return redirect(url_for("loging"))
    else:
            return render_template("loging.html")
    
    if session.get('username'):
        source_dir = "/static/vedio/S01"
        filelist_1 = os.listdir("D:/pythonflask/static/vedio/S01")
        filelist_1 = [os.path.join(source_dir,i) for i in filelist_1 if i.endswith(".mp4")]
        return render_template("index.html",filelist=filelist_1)
   
    else:
        return redirect('login')
    
@app.route('/login',methods=["GET",'POST'])
def loging():
    if session.get('username'):
        return redirect(url_for('index'))
    if request.method == "POST":
       username = request.form['user']
       passwd = request.form['pwd']
       result_type = request.form["sub"]
       yzm = request.form["yzm"]
       result = User.query.filter_by(User_name=username).first()
       yzm = yzm.lower()
       if result_type == "登录":
            if result:
                    if result.User_password == passwd and session.get("yanzhengma") == yzm:
                        session['username'] = username
                        return redirect(url_for('index'))
                    elif session.get("yanzhengma") != yzm:
                        return render_template("loging.html",error="验证码错误")
                    elif result.User_password != passwd:
                        return render_template("loging.html",error="密码错误")                    
            else:
                    if session.get("yanzhengma") == yzm:
                        return render_template("loging.html",error="还没注册?")
                    else:
                        return render_template("loging.html",error="验证码错误")
       else:
            if result:
                return render_template("loging.html",error="用户名已存在")
            elif session.get("yanzhengma") != yzm:
                return render_template("loging.html",error="验证码错误")
            elif not validate_password(passwd):
                return render_template("loging.html",error="需要大小写字母数字和符号")
            else :
                 user = User(User_name=username,User_password=passwd)
                 db.session.add(user)
                 db.session.commit()
                 return render_template("skip.html")
            
        
       return redirect(url_for('index'))
    else:
        return render_template('loging.html')

@app.route('/show/<id>')
def show_user(id):
    if id == '99':
    # source_dir = "/static/video/S01"
        filelist_1 = os.listdir("D:/pythonflask/static/video/S01")
        filelist_1 = [ i.replace(".mp4","")  for i in filelist_1 if i.endswith(".mp4")]
        return render_template("index.html",filelist=filelist_1)



@app.route("/mkimg")
def mk_img():
    img, code_str = check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    img = stream.getvalue()
    image_encding = base64.b64encode(img).decode("utf-8")
    image_b64 = 'data:image/png;base64,' + image_encding
    session["yanzhengma"] = code_str.lower()
    return jsonify({"code": code_str, "img": image_b64})
    

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(host="0.0.0.0",port=80,debug=True)

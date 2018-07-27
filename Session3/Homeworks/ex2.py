from flask import Flask,render_template
import mlab_1
from ex2_class import PushHobby

app=Flask(__name__)

mlab_1.connect()
@app.route("/")
def hobby():
    hobby_list=PushHobby.objects()
    return render_template("homeworktemplate.html",hobby_infos = hobby_list) 

if __name__ == "__main__":
    app.run(debug=True)
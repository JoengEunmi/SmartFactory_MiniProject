from sqlalchemy import create_engine, or_
from flask import Flask, url_for, render_template, request, redirect, session, jsonify, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from sqlalchemy.sql.expression import desc
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruit.db'
db = SQLAlchemy(app)


class Personal_user(db.Model):
    __tablename__ = "pusers"
    
    pid = db.Column(db.String, primary_key=True)
    pname = db.Column(db.String)
    pphone = db.Column(db.String)
    pjumin = db.Column(db.String)
    paddress = db.Column(db.String)
    pemail = db.Column(db.String)
    ppassword = db.Column(db.String)
    pgender = db.Column(db.String)
    
    def __init__(self, pid, pname, pphone, pjumin, paddress, pemail, ppassword, pgender):
        self.pid = pid
        self.pname = pname
        self.pphone = pphone
        self.pjumin = pjumin
        self.paddress = paddress
        self.pemail = pemail
        self.ppassword = ppassword
        self.pgender = pgender
        
    def __repr__(self):
        return "<Personal_user('%s', '%s', '%s', '%s','%s', '%s', '%s','%s')>" % (self.pid, self.pname, self.pphone, self.pjumin, self.paddress, self.pemail, self.ppassword, self.pgender)
        
        
class Company_user(db.Model):
    __tablename__ = "cusers"
    
    cid = db.Column(db.String, primary_key=True)
    cphone = db.Column(db.String)
    cpassword = db.Column(db.String)
    caddress = db.Column(db.String)
    cnumber = db.Column(db.String)
    ctype = db.Column(db.String)
    cfax = db.Column(db.String)
    cpresident = db.Column(db.String)
    cinfo = db.Column(db.String)
    
    def __init__(self, cid, cpassword, cphone, caddress, cnumber, ctype, cfax, cpresident, cinfo):
        self.cid = cid
        self.cpassword = cpassword
        self.cphone = cphone
        self.caddress = caddress
        self.cnumber = cnumber
        self.ctype = ctype
        self.cfax = cfax
        self.cpresident = cpresident
        self.cinfo = cinfo
        
    def __repr__(self):
        return "<cusers('%s', '%s', '%s','%s', '%s', '%s', '%s','%s','%s')>" % (self.cid, self.cphone, self.cpassword, self.caddress, self.cnumber, self.ctype, self.cfax, self.cpresident, self.cinfo)


class QnA(db.Model):
    __tablename__ = "qna"
    
    qid = db.Column(db.Integer, primary_key=True)
    qtitle = db.Column(db.String)
    qread = db.Column(db.Integer)
    qdate = db.Column(db.Integer)
    qcontent = db.Column(db.String)
    pid = db.Column(db.String)

    def __init__(self, qtitle, qread, qdate, qcontent, pid):
        self.qtitle = qtitle
        self.qread = qread
        self.qdate = qdate
        self.qcontent = qcontent
        self.pid = pid
        
    def __repr__(self):
        return "<QnA('%s', '%d', '%d', '%s', '%s')>" % (self.qtitle, self.qread, self.qdate, self.qcontent, self.pid)


class QnAa(db.Model):
    __tablename__ = "qnaa"
    
    qaid = db.Column(db.Integer, primary_key=True)
    qid = db.Column(db.Integer)
    cid = db.Column(db.String)
    qadate = db.Column(db.Integer)
    qacontent = db.Column(db.String)
    
    def __init__(self, qid, cid, qadate, qacontent):      
        self.qid = qid
        self.cid = cid
        self.qadate = qadate
        self.qacontent = qacontent
        
    def __repr__(self):
        return "<QnAa('%d', '%s', '%d', '%s')>" % (self.qid, self.cid, self.qadate, self.qacontent)


class Recruit(db.Model):
    __tablename__ = "recruit"
    
    cid = db.Column(db.String)
    ctype = db.Column(db.String)
    rid = db.Column(db.Integer, primary_key=True)
    rfinaldate = db.Column(db.Integer)
    rstartdate = db.Column(db.Integer)
    rtitle = db.Column(db.String)
    rlogo = db.Column(db.String)
    rarea = db.Column(db.String)
    rfield = db.Column(db.String)
    rcontent = db.Column(db.String)
    rQ1 = db.Column(db.String)
    rQ2 = db.Column(db.String)
    rQ3 = db.Column(db.String)
    rQ4 = db.Column(db.String)
    read = db.Column(db.Integer)
    
    def __init__(self, cid, ctype, rfinaldate, rstartdate, rtitle, rlogo, rarea, rfield, rcontent, rQ1, rQ2, rQ3, rQ4, read=0):
        self.cid = cid
        self.ctype = ctype
        self.rfinaldate = rfinaldate
        self.rstartdate = rstartdate
        self.rtitle = rtitle
        self.rlogo = rlogo
        self.rarea = rarea
        self.rfield = rfield
        self.rcontent = rcontent
        self.rQ1 = rQ1
        self.rQ2 = rQ2
        self.rQ3 = rQ3
        self.rQ4 = rQ4
        self.read = read
        
    def __repr__(self):
        return "<Recruit('%s','%s','%d','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%d')>" % (self.cid, self.ctype, self.rfinaldate, self.rstartdate, self.rtitle, self.rlogo, self.rarea, self.rfield, self.rcontent, self.rQ1, self.rQ2, self.rQ3, self.rQ4, self.read)

'''
class CoverLetter(db.Model):
    __tablename__ = "coverletter"
    
    rid = db.Column(db.Integer)
    pid = db.Column(db.String)
    clid = db.Column(db.Integer, primary_key = True)
    clcerti = db.Column(db.String)
    clpicture = db.Column(db.String)
    clhigh = db.Column(db.String)
    cluni = db.Column(db.String)
    clmajor = db.Column(db.String)
    clgpa = db.Column(db.String)
    clrQ1 = db.Column(db.String)
    clrQ2 = db.Column(db.String)
    clrQ3 = db.Column(db.String)
    clrQ4 = db.Column(db.String)
    
    def __init__(self, rid, pid, clcerti, clpicture, clhigh, cluni, clmajor, clgpa, clrQ1, clrQ2, clrQ3, clrQ4):
        self.rid = rid
        self.pid = pid
        self.clcerti = clcerti
        self.clpicture = clpicture
        self.clhigh = clhigh
        self.cluni = cluni
        self.clmajor = clmajor
        self.clgpa = clgpa
        self.clrQ1 = clrQ1
        self.clrQ2 = clrQ2
        self.clrQ3 = clrQ3
        self.clrQ4 = clrQ4
        
    def __repr__(self):
        return "<CoverLetter('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" %(self.rid, self.pid, self.clcerti, self.clpicture, self.clhigh, self.cluni, self.clmajor, self.clgpa, self.clrQ1, self.clrQ2, self.clrQ3, self.clrQ4 )
'''


class Coverletter(db.Model):
    __tablename__ = "coverletter"
    
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String)
    rid = db.Column(db.Integer)
    rtitle = db.Column(db.String)
    name = db.Column(db.String)
    englishname = db.Column(db.String)
    genderFlag = db.Column(db.String)
    birthday = db.Column(db.Integer)
    rfield = db.Column(db.String)
    profilepic = db.Column(db.String)
    postNumber = db.Column(db.String)
    addressName = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    highschoolGraduationTypeCode = db.Column(db.String)
    highName = db.Column(db.String)
    highschoolLocationCode = db.Column(db.String)
    highschoolHighschoolCategoryCode = db.Column(db.String)
    highschoolDayOrNight = db.Column(db.String)
    highschoolEntranceDate = db.Column(db.Integer)
    highschoolGraduationDate = db.Column(db.Integer)
    collegeDegreeTypeCode = db.Column(db.String)
    universityName = db.Column(db.String)
    collegeLocationCode = db.Column(db.String)
    collegeHeadOrBranch = db.Column(db.String)
    collegeEntranceDate = db.Column(db.Integer)
    collegeGraduationDate = db.Column(db.Integer)
    collegeEntranceTypeCode = db.Column(db.String)
    collegeGraduationTypeCode = db.Column(db.String)
    majorName = db.Column(db.String)
    collegeCollegeMajorMajorCategoryCode = db.Column(db.String)
    collegeCollegeMajorDayOrNight = db.Column(db.String)
    collegeScore = db.Column(db.Float)
    collegePerfectScore = db.Column(db.Float)
    testName = db.Column(db.String)
    languageSkillLanguageCode = db.Column(db.String)
    languageSkillSpeakingLevelCodeSn = db.Column(db.String)
    languageSkillWritingLevelCodeSn = db.Column(db.String)
    languageSkillReadingLevelCodeSn = db.Column(db.String)
    certificateName = db.Column(db.String)
    certificatePlace = db.Column(db.String)
    certificateNumber = db.Column(db.String)
    licenseAcquireDate = db.Column(db.Integer)
    etcFile = db.Column(db.String)
    clq1 = db.Column(db.String)
    clq2 = db.Column(db.String)
    clq3 = db.Column(db.String)
    clq4 = db.Column(db.String)
    rfinaldate = db.Column(db.Integer)
    lastmodifydate = db.Column(db.Integer)
    
    def __init__(self, pid, rid, rtitle, name, englishname, genderFlag, birthday, rfield, profilepic, postNumber, addressName, email, phone, highschoolGraduationTypeCode, highName, highschoolLocationCode, highschoolHighschoolCategoryCode, highschoolDayOrNight, highschoolEntranceDate, highschoolGraduationDate, collegeDegreeTypeCode, universityName, collegeLocationCode, collegeHeadOrBranch, collegeEntranceDate, collegeGraduationDate, collegeEntranceTypeCode, collegeGraduationTypeCode, majorName, collegeCollegeMajorMajorCategoryCode, collegeCollegeMajorDayOrNight, collegeScore, collegePerfectScore, testName, languageSkillLanguageCode, languageSkillSpeakingLevelCodeSn, languageSkillWritingLevelCodeSn, languageSkillReadingLevelCodeSn, certificateName, certificatePlace, certificateNumber, licenseAcquireDate, etcFile, clq1, clq2, clq3, clq4, rfinaldate, lastmodifydate):
        self.pid = pid
        self.rid = rid 
        self.rtitle = rtitle
        self.name = name 
        self.englishname = englishname 
        self.genderFlag = genderFlag 
        self.birthday = birthday 
        self.rfield = rfield 
        self.profilepic = profilepic 
        self.postNumber = postNumber 
        self.addressName = addressName 
        self.email = email 
        self.phone = phone 
        self.highschoolGraduationTypeCode = highschoolGraduationTypeCode 
        self.highName = highName 
        self.highschoolLocationCode = highschoolLocationCode 
        self.highschoolHighschoolCategoryCode = highschoolHighschoolCategoryCode 
        self.highschoolDayOrNight = highschoolDayOrNight 
        self.highschoolEntranceDate = highschoolEntranceDate 
        self.highschoolGraduationDate = highschoolGraduationDate 
        self.collegeDegreeTypeCode = collegeDegreeTypeCode 
        self.universityName = universityName 
        self.collegeLocationCode = collegeLocationCode 
        self.collegeHeadOrBranch = collegeHeadOrBranch 
        self.collegeEntranceDate = collegeEntranceDate 
        self.collegeGraduationDate = collegeGraduationDate 
        self.majorName = majorName 
        self.collegeCollegeMajorMajorCategoryCode = collegeCollegeMajorMajorCategoryCode 
        self.collegeCollegeMajorDayOrNight = collegeCollegeMajorDayOrNight 
        self.collegeScore = collegeScore 
        self.collegePerfectScore = collegePerfectScore 
        self.testName = testName 
        self.languageSkillLanguageCode = languageSkillLanguageCode 
        self.languageSkillSpeakingLevelCodeSn = languageSkillSpeakingLevelCodeSn 
        self.languageSkillWritingLevelCodeSn = languageSkillWritingLevelCodeSn 
        self.languageSkillReadingLevelCodeSn = languageSkillReadingLevelCodeSn 
        self.certificateName = certificateName 
        self.certificatePlace = certificatePlace 
        self.certificateNumber = certificateNumber 
        self.licenseAcquireDate = licenseAcquireDate  
        self.etcFile = etcFile
        self.clq1 = clq1
        self.clq2 = clq2
        self.clq3 = clq3
        self.clq4 = clq4
        self.rfinaldate = rfinaldate
        self.lastmodifydate = lastmodifydate
        self.collegeEntranceTypeCode = collegeEntranceTypeCode
        self.collegeGraduationTypeCode = collegeGraduationTypeCode
            
    def __repr__(self):
        return "<Coverletter('%s', '%d', '%s', '%s', %s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%f', '%f', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%d', '%s','%s','%s')>" % (self.pid , self.rid , self.name , self.rtitle, self.englishname , self.genderFlag , self.birthday , self.rfield , self.profilepic , self.postNumber , self.addressName , self.email , self.phone , self.highschoolGraduationTypeCode , self.highName, self.highschoolLocationCode , self.highschoolHighschoolCategoryCode , self.highschoolDayOrNight , self.highschoolEntranceDate , self.highschoolGraduationDate , self.collegeDegreeTypeCode , self.universityName , self.collegeLocationCode , self.collegeHeadOrBranch , self.collegeEntranceDate , self.collegeGraduationDate , self.majorName , self.collegeCollegeMajorMajorCategoryCode , self.collegeCollegeMajorDayOrNight , self.collegeScore , self.collegePerfectScore , self.testName , self.languageSkillLanguageCode , self.languageSkillSpeakingLevelCodeSn , self.languageSkillWritingLevelCodeSn , self.languageSkillReadingLevelCodeSn , self.certificateName , self.certificatePlace , self.certificateNumber , self.licenseAcquireDate , self.etcFile, self.Q1, self.Q2, self.Q3, self.Q4, self.collegeEntranceTypeCode, self.collegeGraduationTypeCode)
   
      
def format_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')


def stringtotimestamp(s):
    timestamp = time.mktime(datetime.strptime(s, "%Y-%m-%d").timetuple())
    temp = int(timestamp) + 86400
    return temp


@app.route("/")
def home():
    recruit_data = Recruit.query.filter_by(ctype="대기업").order_by(desc(Recruit.read)).limit(5)
    return render_template("home.html", rec=recruit_data)


@app.route("/pregister", methods=["GET", "POST"])
def pregister():
    if request.method == 'GET':
        return render_template("p_register.html")
    elif request.method == "POST":
        try:
            new_user = Personal_user(pid=request.form["pid"], pname=request.form["pname"], pphone=request.form["pphone"], pjumin=request.form["pjumin"], paddress=request.form["paddress"], pemail=request.form["pemail"], ppassword=request.form["ppassword"], pgender=request.form["pgender"])
            db.session.add(new_user)
            db.session.commit()
            return render_template("p_login.html")
        except:
            message = "이미 가입된 회원입니다"
            return render_template("message.html", msg=message)
    

@app.route("/cregister", methods=["GET", "POST"])
def cregister():    
    if request.method == 'GET':
        return render_template("c_register.html")
    elif request.method == "POST":
        try:
            new_user = Company_user(cid=request.form["cid"], cpassword=request.form["cpassword"], cphone=request.form["cphone"], caddress=request.form["caddress"], cnumber=request.form["cnumber"], ctype=request.form["ctype"], cfax=request.form["cfax"], cpresident=request.form["cpresident"], cinfo=request.form["cinfo"])
            db.session.add(new_user)
            db.session.commit()
            return render_template("c_login.html")
        except:
            message = "이미 가입된 회원입니다"
            return render_template("message.html", msg=message)


@app.route("/plogin", methods=['GET', 'POST'])
def plogin():
    if request.method == 'GET':
        return render_template("p_login.html")
    elif request.method == "POST":
        uid = request.form["pid"]
        upassword = request.form["ppassword"]
        try:
            user_data = Personal_user.query.filter_by(pid=uid, ppassword=upassword).first()
            if user_data is not None:
                session['user_id'] = user_data.pid
                session['logged_in'] = True
                session['usertype'] = "person"
                return redirect(url_for("home"))
            else:
                message = "회원이 아닙니다"
                return render_template("message.html", msg=message)
        except:
            message = "exception!!!"
            return render_template("message.html", msg=message)
            

@app.route("/clogin", methods=["GET", "POST"])
def clogin():
    if request.method == "GET":
        return render_template("c_login.html")
    elif request.method == "POST":
        uid = request.form["cid"]
        upassword = request.form["cpassword"]
        try:
            user_data = Company_user.query.filter_by(cid=uid, cpassword=upassword).first()
            if user_data is not None :
                session ['user_id'] = user_data.cid
                session ['logged_in'] = True
                session ['usertype'] = "company"
                return redirect(url_for("home"))
            else :
                message = "회원이 아닙니다"
                return render_template("message.html", msg=message)
        except:
            message = "exception!!"
            return render_template("message.html", msg=message)    


@app.route("/recruit", methods=["GET", "POST"])
def recruit():
    rec = Recruit.query.order_by(desc(Recruit.read)).all()
    return render_template("recruit.html", recruit=rec)

        
@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['user_id'] = None
    session['usertype'] = None
    return redirect(url_for("home"))


@app.route("/unjoin")
def unjoin():
    try:
        if(session['usertype'] == "person"):
            user_data = Personal_user.query.filter_by(pid=session['user_id']).first()
            db.session.delete(user_data)
            db.session.commit()
            session['logged_in'] = False
            session['user_id'] = None
            session['usertype'] = None
            return redirect(url_for('home'))
        elif(session['usertype'] == "company"):
            user_data = Company_user.query.filter_by(cid=session['user_id']).first()
            db.session.delete(user_data)
            db.session.commit()
            session['logged_in'] = False
            session['user_id'] = None
            session['usertype'] = None
            return redirect(url_for('home'))
    except:
        message = "exception!!!"
        return render_template("message.html", msg=message)

    
@app.route("/recruit/add", methods=["GET", "POST"])
def addrecruit():
    if request.method == "GET":
        user_data = Company_user.query.filter_by(cid=session['user_id']).first()
        return render_template("newrecruit.html", cuser=user_data)
    elif request.method == "POST":
        try:
            f = request.files['rlogo']
            temp = str(int(time.time()))
            f.save("static/img/" + temp + secure_filename(f.filename))
            rlogopath = "/static/img/" + temp + secure_filename(f.filename)
            rec_data = Recruit(cid=session['user_id'], ctype=request.form["ctype"], rfinaldate=stringtotimestamp(request.form["rfinaldate"]), rstartdate=stringtotimestamp(request.form['rstartdate']), rtitle=request.form["rtitle"], rlogo=rlogopath, rarea=request.form["rarea"], rfield=request.form["rfield"], rcontent=request.form["rcontent"], rQ1=request.form["rQ1"], rQ2=request.form["rQ2"], rQ3=request.form["rQ3"], rQ4=request.form["rQ4"], read=0)
            db.session.add(rec_data)
            db.session.commit()
            return redirect(url_for("recruit"))
        except:
            message = "exception!!!"
            return render_template("message.html", msg=message)

    
@app.route("/recruit/view/<int:recruit_id>")
def recruitview(recruit_id=None):
    rec = Recruit.query.filter_by(rid=recruit_id).first()
    rec.read = rec.read + 1
    db.session.commit()
    com = Company_user.query.filter_by(cid=rec.cid).first()
    return render_template("recruitview.html", recruit=rec, company=com)

    
@app.route("/qna", methods=["GET", "POST"])
def qna():
    try:
        if session['logged_in'] == False:
            message = "로그인이 필요합니다"
            return render_template("message.html", msg=message)
    except:
        message = "로그인이 필요합니다"
        return render_template("message.html", msg=message)
    if request.method == "POST":
        key_data = QnA.query.filter(or_(QnA.qtitle.like('%' + request.form["keyword"] + '%')))
        return render_template("qna.html", qna=key_data)
    else:
        qnadata = QnA.query.all()
        return render_template("qna.html", qna=qnadata)

    
@app.route("/qna/write", methods=["GET", "POST"])
def qnawrite():
    if request.method == "GET":
#         print(session['usertype'])
        if(session['usertype'] == "company"):
            message = "개인 회원만 작성 가능합니다"
            return render_template("message.html", msg=message)
        elif (session['usertype'] == "person"):
            return render_template("qwrite.html")
    elif (request.method == "POST"):
        new_qna = QnA(qtitle=request.form["qtitle"], qdate=int(time.time()), qread=0, qcontent=request.form["qcontent"], pid=session['user_id'])
        db.session.add(new_qna)
        db.session.commit()
        return redirect(url_for("qna"))

    
@app.route("/recruit/field")
def recruitbyfield(field=None):
#     print(request.args.get("field"))
    if request.args.get("field") == "all":
        rec = Recruit.query.order_by(desc(Recruit.read)).all()
        return render_template("recruit.html", recruit=rec)
    else:
        rec = Recruit.query.filter_by(rfield=request.args.get("field")).order_by(desc(Recruit.read)).all()
        return render_template("recruit.html", recruit=rec)


@app.route("/recruit/location")
def recruitbyloc(location=None):
    if request.args.get("location") == "all":
        rec = Recruit.query.order_by(desc(Recruit.read)).all()
        return render_template("recruit.html", recruit=rec)
    else:
        rec = Recruit.query.filter_by(rarea=request.args.get("location")).order_by(desc(Recruit.read)).all()
        return render_template("recruit.html", recruit=rec)


@app.route("/qna/<int:qqid>", methods=["GET", "POST"])
def qnaview(qqid=None):
    if request.method == "POST":
        if session['usertype'] == "person":
            message = "기업 회원만 작성 가능합니다"
            return render_template("message.html", msg=message)
#         print(request.form["qacontent"])
        qnaaadd(qqid, request.form["qacontent"])
        qna_data = QnA.query.filter_by(qid=qqid).first()
        qnaa_data = QnAa.query.filter_by(qid=qqid).all()
        return render_template("qnaview.html", qna=qna_data, qnaa=qnaa_data)
    else:
        qna_data = QnA.query.filter_by(qid=qqid).first()
        qna_data.qread += 1
        db.session.commit()
        qnaa_data = QnAa.query.filter_by(qid=qqid).all()
        return render_template("qnaview.html", qna=qna_data, qnaa=qnaa_data)

    
def qnaaadd(qqid, qqacontent):
    temp = int(time.time())
    qnaa_data = QnAa(qid=qqid, cid=session['user_id'], qadate=temp, qacontent=qqacontent)
    db.session.add(qnaa_data)
    db.session.commit()
    return


@app.route("/recruitsearch")
def recruitsearch():
    if request.args.get("select") == "all":
        rec_data = Recruit.query.filter(or_(Recruit.rtitle.like('%' + request.args.get("keyword") + '%'))).all()
        return render_template("recruit.html", recruit=rec_data)
    else:
        rec_data = Recruit.query.filter_by(rarea=request.args.get("select")).filter(or_(Recruit.rtitle.like('%' + request.args.get("keyword") + '%'))).all()
        return render_template("recruit.html", recruit=rec_data)

    
@app.route("/mycrecruit")
def mycrecruit():
    rec_data = Recruit.query.filter_by(cid=session['user_id']).all()
    return render_template("mycrecruit.html", recruit=rec_data)


@app.route("/myprecruit")
def myprecruit():
    cov_data = Coverletter.query.filter_by(pid=session['user_id']).all()
    return render_template("myprecruit.html", coverletter=cov_data)


@app.route("/coverletter/<int:rrid>", methods=["GET", "POST"])
def coverletter(rrid=None):
    try:
        if session['logged_in'] == False:
            message = "로그인이 필요합니다"
            return render_template("message.html", msg=message)
    except:
        message = "로그인이 필요합니다"
        return render_template("message.html", msg=message)
    
    if request.method == "POST":
        temp = str(int(time.time()))
#         print(request.files)
        f = request.files['profilepic']
        f.save("static/img/" + temp + secure_filename(f.filename))
        pic = "/static/img/" + temp + secure_filename(f.filename)
        f2 = request.files['etcFile']
        f2.save("static/port/" + temp + secure_filename(f2.filename))
        port = "/static/port/" + temp + secure_filename(f2.filename)
        lasttime = int(time.time())
        
        new_cover = Coverletter(pid=request.form['pid'], rid=request.form['rid'], rtitle=request.form['rtitle'], name=request.form['username'], englishname=request.form['englishName'], genderFlag=request.form['genderFlag'], birthday=stringtotimestamp(request.form['birthday']), rfield=request.form['field'], profilepic=pic, postNumber=request.form['postNumber'], addressName=request.form['addressName'], email=request.form['email'], phone=request.form['phone'], highschoolGraduationTypeCode=request.form['highschool.graduationTypeCode'], highName=request.form['highName'], highschoolLocationCode=request.form['highschool.locationCode'], highschoolHighschoolCategoryCode=request.form['highschool.highschoolCategoryCode'], highschoolDayOrNight=request.form['highschool.dayOrNight'], highschoolEntranceDate=stringtotimestamp(request.form['highschool.entranceDate']), highschoolGraduationDate=stringtotimestamp(request.form['highschool.graduationDate']), collegeDegreeTypeCode=request.form['college.degreeTypeCode'], universityName=request.form['universityName'], collegeLocationCode=request.form['college.locationCode'], collegeHeadOrBranch=request.form['college.headOrBranch'], collegeEntranceDate=stringtotimestamp(request.form['college.entranceDate']), collegeGraduationDate=stringtotimestamp(request.form['college.graduationDate']), majorName=request.form['majorName'], collegeCollegeMajorMajorCategoryCode=request.form['college.collegeMajor.majorCategoryCode'], collegeCollegeMajorDayOrNight=request.form['college.collegeMajor.dayOrNight'], collegeScore=request.form['college.score'], collegePerfectScore=request.form['college.perfectScore'], testName=request.form['testName'], languageSkillLanguageCode=request.form['languageSkill.languageCode'], languageSkillSpeakingLevelCodeSn=request.form['languageSkill.speakingLevelCodeSn'], languageSkillWritingLevelCodeSn=request.form['languageSkill.writingLevelCodeSn'], languageSkillReadingLevelCodeSn=request.form['languageSkill.readingLevelCodeSn'], certificateName=request.form['certificateName'], certificatePlace=request.form['certificatePlace'], certificateNumber=request.form['certificateNumber'], licenseAcquireDate=stringtotimestamp(request.form['license.acquireDate']), etcFile=port, clq1=request.form['cla1'], clq2=request.form['cla2'], clq3=request.form['cla3'], clq4=request.form['cla4'], lastmodifydate=lasttime, rfinaldate=request.form['rfinaldate'], collegeEntranceTypeCode=request.form['college.entranceTypeCode'], collegeGraduationTypeCode=request.form['college.graduationTypeCode'])
        db.session.add(new_cover)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        rec_data = Recruit.query.filter_by(rid=rrid).first()
        user_data = Personal_user.query.filter_by(pid=session['user_id']).first()
        return render_template("coverletter.html", recruit=rec_data, user=user_data)

    
@app.route("/personalinfo", methods=["GET", "POST"])
def personalinfo():
    if request.method == "POST":
        user_data = Personal_user.query.filter_by(pid=session['user_id']).first()
        user_data.pname = request.form['pname']
        user_data.ppassword = request.form['ppassword']
        user_data.pemail = request.form['pemail']
        user_data.pphone = request.form['pphone']
        user_data.paddress = request.form['paddress']
        db.session.commit()
        return redirect(url_for("home"))
    else:    
        user_data = Personal_user.query.filter_by(pid=session['user_id']).first()
        return render_template("pmmypage.html", user=user_data)


@app.route("/companyinfo", methods=["GET", "POST"])
def companyinfo():
    if request.method == "POST":
        user_data = Company_user.query.filter_by(cid=session['user_id']).first()
        user_data.cpresident = request.form['cpresident']
        user_data.cpassword = request.form['cpassword']
        user_data.ctype = request.form['ctype']
        user_data.cinfo = request.form['cinfo']
        user_data.cphone = request.form['cphone']
        user_data.cfax = request.form['cfax']
        user_data.caddress = request.form['caddress']
        db.session.commit()
        return redirect(url_for("home"))
    else:  
        user_data = Company_user.query.filter_by(cid=session['user_id']).first()
        return render_template("cmmypage.html", user=user_data)


@app.route("/coverletterview/<int:clid>")
def coverletterview(clid=None):
    cov_data = Coverletter.query.filter_by(id=clid).first()
    rec_data = Recruit.query.filter_by(rid=cov_data.rid).first()
    user_data = Personal_user.query.filter_by(pid=cov_data.pid).first()
    return render_template("coverletterview.html", coverletter=cov_data, recruit=rec_data, user=user_data)


@app.route("/coverlettermodi/<int:clid>", methods=["GET", "POST"])
def coverlettermodi(clid=None):
    if request.method == "POST":
        cov_data = Coverletter.query.filter_by(id=clid).first()
        cov_data.englishname = request.form['englishName']
        cov_data.genderFlag = request.form['genderFlag']
        cov_data.postNumber = request.form['postNumber']
        cov_data.addressName = request.form['addressName']
        cov_data.highschoolGraduationTypeCode = request.form['highschool.graduationTypeCode']
        cov_data.highName = request.form['highName']
        cov_data.highschoolLocationCode = request.form['highschool.locationCode']
        cov_data.highschoolHighschoolCategoryTypeCode = request.form['highschool.highschoolCategoryCode']
        cov_data.highschoolDayOrNight = request.form['highschool.dayOrNight']
        cov_data.collegeDegreeTypeCode = request.form['college.degreeTypeCode']
        cov_data.universityName = request.form['universityName']
        cov_data.collegeLocationCode = request.form['college.locationCode']
        cov_data.collegeHeadOrBranch = request.form['college.headOrBranch']
        cov_data.collegeEntranceTypeCode = request.form['college.entranceTypeCode']
        cov_data.collegeGraduationTypeCode = request.form['college.graduationTypeCode']
        cov_data.majorName = request.form['majorName']
        cov_data.collegeCollegeMajorMajorCategoryCode = request.form['college.collegeMajor.majorCategoryCode']
        cov_data.collegeCollegeMajorDayOrNight = request.form['college.collegeMajor.dayOrNight']
        cov_data.collegeScore = request.form['college.score']
        cov_data.collegePerfectScore = request.form['college.perfectScore']
        cov_data.languageSkillLanguageCode = request.form['languageSkill.languageCode']
        cov_data.languageSkillSpeakingLevelCodeSn = request.form['languageSkill.speakingLevelCodeSn']
        cov_data.languageSkillWritingLevelCodeSn = request.form['languageSkill.writingLevelCodeSn']
        cov_data.languageSkillReadingLevelCodeSn = request.form['languageSkill.readingLevelCodeSn']
        cov_data.certificateName = request.form['certificateName']
        cov_data.certificatePlace = request.form['certificatePlace']
        cov_data.certificateNumber = request.form['certificateNumber']
        cov_data.clq1 = request.form['cla1']
        cov_data.clq2 = request.form['cla2']
        cov_data.clq3 = request.form['cla3']
        cov_data.clq4 = request.form['cla4']
        
        f = request.files['profilepic']
        if f.filename == '':
            pass
        else:
            temp = str(int(time.time()))
            f.save("static/img/" + temp + secure_filename(f.filename))
            pic = "/static/img/" + temp + secure_filename(f.filename)
            cov_data.profilepic = pic
        
        if type(request.form['birthday']) == type(5):
            cov_data.birthday = request.form['birthday']
        else:
            cov_data.birthday = stringtotimestamp(request.form['birthday'])
        
        if type(request.form['license.acquireDate']) == type(5):
            cov_data.licenseAcquireDate = request.form['license.acquireDate']
        else:
            cov_data.licenseAcquireDate = stringtotimestamp(request.form['license.acquireDate'])
        
        if type(request.form['highschool.entranceDate']) == type(5):
            cov_data.highschoolEntranceDate = request.form['highschool.entranceDate']
        else:
            cov_data.highschoolEntranceDate = stringtotimestamp(request.form['highschool.entranceDate'])
        
        if type(request.form['highschool.graduationDate']) == type(5):
            cov_data.highschoolGraduationDate = request.form['highschool.graduationDate']
        else:
            cov_data.highschoolGraduationDate = stringtotimestamp(request.form['highschool.graduationDate'])
        
        if type(request.form['college.entranceDate']) == type(5):
            cov_data.collegeEntranceDate = request.form['college.entranceDate']
        else:
            cov_data.collegeEntranceDate = stringtotimestamp(request.form['college.entranceDate'])
        
        if type(request.form['college.graduationDate']) == type(5):
            cov_data.collegeGraduationDate = request.form['college.graduationDate']
        else:
            cov_data.collegeGraduationDate = stringtotimestamp(request.form['college.graduationDate'])
        cov_data.lastmodifydate = time.time()
        db.session.commit()
        
        return redirect(url_for("myprecruit"))
    else:
        cov_data = Coverletter.query.filter_by(id=clid).first()
        user_data = Personal_user.query.filter_by(pid=session['user_id']).first()
        rec_data = Recruit.query.filter_by(rid=cov_data.rid).first()
        return render_template("coverlettermodi.html", coverletter=cov_data, user=user_data, recruit=rec_data)

    
@app.route("/recruitmodi/<int:rrid>", methods=["GET", "POST"])
def recruitmodi(rrid=None):
    if request.method == "POST":
        rec_data = Recruit.query.filter_by(rid=rrid).first()
        rec_data.rtitle = request.form['rtitle']
        rec_data.rarea = request.form['rarea']
        rec_data.rfield = request.form['rfield']
        rec_data.rcontent = request.form['rcontent']
        rec_data.rQ1 = request.form['rQ1']
        rec_data.rQ2 = request.form['rQ2']
        rec_data.rQ3 = request.form['rQ3']
        rec_data.rQ4 = request.form['rQ4']
        
        if type(request.form['rstartdate']) == type(5):
            rec_data.rstartdate = request.form['rstartdate']
        else:
            rec_data.rstartdate = stringtotimestamp(request.form['rstartdate'])
        
        if type(request.form['rfinaldate']) == type(5):
            rec_data.collegeGraduationDate = request.form['rfinaldate']
        else:
            rec_data.collegeGraduationDate = stringtotimestamp(request.form['rfinaldate'])
        db.session.commit()
        return redirect(url_for("mycrecruit"))
        
    else:
        rec_data = Recruit.query.filter_by(rid=rrid).first()
#         print(rec_data)
        user_data = Company_user.query.filter_by(cid=rec_data.cid).first()
#         print(user_data)
        return render_template("recruitmodi.html", recruit=rec_data, cuser=user_data)

    
@app.route("/applicantlist/<int:rrid>")
def applicantlist(rrid=None):
    cov_data = Coverletter.query.filter_by(rid=rrid).all()
    return render_template("applicantlist.html", coverletter=cov_data)    


@app.route("/futureyearcalculate")
def futureyearcalculate():
    return render_template("futureyearcalculate.html")


@app.route("/changescore")
def changescore():
    return render_template("changescore.html")


@app.route("/hakjomcount")
def hakjomcount():
    return render_template("hakjomcount.html")


@app.route("/hangulcheck")
def hangulcheck():
    return render_template("hangulcheck.html")


@app.route("/salarycalculator")
def salarycalculator():
    return render_template("salarycalculator.html")


app.jinja_env.filters['datetimeformat'] = format_datetime

if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.secret_key = "1234567890"
    app.run(host="0.0.0.0")
        

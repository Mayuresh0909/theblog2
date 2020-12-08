from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json
import os


local_server = True
with open('config.json', 'r') as configurations:
    params = json.load(configurations)["params"]


app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['email_username'],
    MAIL_PASSWORD=params['email_password']
)


mail = Mail(app)


if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(15), unique=False, nullable=False)
    message = db.Column(db.String(500), unique=False, nullable=False)
    datetime = db.Column(db.String(12), unique=False, nullable=True)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(5000), unique=False, nullable=False)
    department = db.Column(db.String(500), unique=False, nullable=False)
    category = db.Column(db.String(500), unique=False, nullable=False)
    event = db.Column(db.String(500), unique=False, nullable=False)
    photo = db.Column(db.String(500), unique=False, nullable=True)
    date = db.Column(db.String(12), unique=False, nullable=True)


@app.route('/posts', methods=['GET', 'POST'])
def newPost():
    """Add new post to database"""

    if request.method == 'POST':
        title = request.form.get('title')
        slug = title
        content = request.form.get('content')
        department = request.form.get('department')
        category = request.form.get('category')
        event = request.form.get('event')
        photo = request.files['addimage']

        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(photo.filename)))

        #photo_url = os.path.join(
            #r"C:\Users\mayur\Desktop\Documents\College Documents\Semesters\sem 5\WDL\mycollege blog\flask\theblog\uploaded_images",
            #secure_filename(photo.filename))

        photo_url = secure_filename(photo.filename)

        entry = Posts(title=title,
                      slug=slug,
                      content=content,
                      department=department,
                      category=category,
                      event=event,
                      photo=photo_url,
                      date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        #mail.send_message("New Post on Blogee!!!")

    # return render_template('create-post.html')
    return "Submitted!"


@app.route("/post/<string:post_slug>", methods=['GET', 'POST'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('complete-blog.html', post=post, params=params)


@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        """Add entry to database"""

        email = request.form.get('email')
        name = request.form.get('name')
        phone_num = request.form.get('phone_num')
        message = request.form.get('message')

        entry = Contacts(email=email,
                         name=name,
                         phone_num=phone_num,
                         datetime=datetime.now(),
                         message=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Message on Blogee from ' + name,
                          sender=email,
                          recipients=[params['email_username']],
                          body=message + "\n" + phone_num)

    return render_template('contactUs.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fullblog')
def fullblog():
    return render_template('complete-blog.html', params=params)


@app.route('/createpost')
def create_post():
    return render_template('create-post.html')


@app.route('/hackathon')
def hackathon():
    posts = Posts.query.filter_by(event='HACKATHON').all()

    """
    database posts ==> events column ==> filter by event name
    
    .all() ==> all posts with 
    
    price = BikePrices.query.filter_by(cost = "2000").all()
    
    """
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/mockplacement')
def mockplacement():
    posts = Posts.query.filter_by(event='MOCK PLACEMENT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/softwaredocumentation')
def softwaredocumentation():
    posts = Posts.query.filter_by(event='SOFTWARE DOCUMENTATION').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/technohunt')
def technohunt():
    posts = Posts.query.filter_by(event='TECHNOHUNT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/blindcode')
def blindcode():
    posts = Posts.query.filter_by(event='BLIND CODE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/chemshala')
def chemshala():
    posts = Posts.query.filter_by(event='CHEMSHALA').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/techexpo')
def techexpo():
    posts = Posts.query.filter_by(event='TECH EXPO').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/protoype')
def prototype():
    posts = Posts.query.filter_by(event='PROTOTYPE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/technicalpaperpresentation')
def technicalpaperpresentation():
    posts = Posts.query.filter_by(event='TECHNICAL PAPER PRESENTATION').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/technicalquiz')
def technicalquiz():
    posts = Posts.query.filter_by(event='TECHNICAL QUIZ').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/pubg')
def pubg():
    posts = Posts.query.filter_by(event='PUBG').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/livecs')
def livecs():
    posts = Posts.query.filter_by(event='LIVE CS').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/fifa')
def fifa():
    posts = Posts.query.filter_by(event='FIFA').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/langaming')
def langaming():
    posts = Posts.query.filter_by(event='LAN GAMING').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/solodance')
def solodance():
    posts = Posts.query.filter_by(event='SOLO DANCE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/groupdance')
def groupdance():
    posts = Posts.query.filter_by(event='GROUP DANCE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/duet')
def duet():
    posts = Posts.query.filter_by(event='DUET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/solosinging')
def solosinging():
    posts = Posts.query.filter_by(event='SOLO SINGING').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/duetsinging')
def duetsinging():
    posts = Posts.query.filter_by(event='DUET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/instrumental')
def instrumental():
    posts = Posts.query.filter_by(event='INSTRUMENTAL').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/bandwars')
def bandwars():
    posts = Posts.query.filter_by(event='BAND WARS').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/filmz')
def filmz():
    posts = Posts.query.filter_by(event='FILMZ').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/picturesque')
def picturesque():
    posts = Posts.query.filter_by(event='PICTURESQUE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/storyandpoetry')
def storyandpoetry():
    posts = Posts.query.filter_by(event='STORY & POETRY').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/facepainting')
def facepainting():
    posts = Posts.query.filter_by(event='FACE PAINTING').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/teeshart')
def teeshart():
    posts = Posts.query.filter_by(event='TEESH ART').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/csimurdermystery')
def csimurdermystery():
    posts = Posts.query.filter_by(event='CSI(MURDER MYSTERY)').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/escapetheroom')
def escapetheroom():
    posts = Posts.query.filter_by(event='ESCAPE THE ROOM').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/elocution')
def elocution():
    posts = Posts.query.filter_by(event='ELOCUTION').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/scavengerhunt')
def scavengerhunt():
    posts = Posts.query.filter_by(event='SCAVENGER HUNT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/waterwarrior')
def waterwarrior():
    posts = Posts.query.filter_by(event='WATER WARRIOR').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/fashionshow')
def fashionshow():
    posts = Posts.query.filter_by(event='FASHIONSHOW').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/debate')
def debate():
    posts = Posts.query.filter_by(event='DEBATE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/wolfofthewallstreet')
def wolfofthewallstreet():
    posts = Posts.query.filter_by(event='WOLF OF THE WALL STREET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/saltact')
def saltact():
    posts = Posts.query.filter_by(event='SALT ACT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/inquisitive')
def inquisitive():
    posts = Posts.query.filter_by(event='INQUISITIVE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/treasurehunt')
def treasurehunt():
    posts = Posts.query.filter_by(event='TREASURE HUNT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/boxcricket')
def boxcricket():
    posts = Posts.query.filter_by(event='BOX CRICKET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/3asidefutsal')
def threeasidefutsal():
    posts = Posts.query.filter_by(event='3 A-SIDE FUTSAL').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/fieldcricket')
def fieldcricket():
    posts = Posts.query.filter_by(event='FIELD CRICKET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/chess')
def chess():
    posts = Posts.query.filter_by(event='CHESS').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/footballleague')
def footballleague():
    posts = Posts.query.filter_by(event='FOOTBALL LEAGUE').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/neoncricket')
def neoncricket():
    posts = Posts.query.filter_by(event='NEON CRIKET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/carromduet')
def carromduet():
    posts = Posts.query.filter_by(event='CARROM(DUET)').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/interdepartmentalfootball')
def interdepartmentalfootball():
    posts = Posts.query.filter_by(event='INTERDEPARTMENTAL FOOTBALL').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/1on1cricket')
def oneononecricket():
    posts = Posts.query.filter_by(event='ONE ON ONE CRICKET').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/carrom')
def carrom():
    posts = Posts.query.filter_by(event='CARROM(SINGLES)').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/antichess')
def antichess():
    posts = Posts.query.filter_by(event='ANTI CHESS').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/badminton')
def badminton():
    posts = Posts.query.filter_by(event='BADMINTON').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/athletics')
def athletics():
    posts = Posts.query.filter_by(event='ATHLETICS').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/kabbadi')
def kabaddi():
    posts = Posts.query.filter_by(event='KABBADI').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/khokho')
def khokho():
    posts = Posts.query.filter_by(event='KHO-KHO').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/tugofwar')
def tugofwar():
    posts = Posts.query.filter_by(event='TUG OF WAR').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/mudrakala')
def mudrakala():
    posts = Posts.query.filter_by(event='MUDRAKALA').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/cresendo')
def cresendo():
    posts = Posts.query.filter_by(event='CRESENDO').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/crew5678')
def crew5678():
    posts = Posts.query.filter_by(event='CREW 5678').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/theliteratureclub')
def theliteratureclub():
    posts = Posts.query.filter_by(event='THE LITERATURE CLUB').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/nautanki')
def nautanki():
    posts = Posts.query.filter_by(event='NAUTANKI').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/camera')
def camera():
    posts = Posts.query.filter_by(event='CAMERA').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/computer')
def computer():
    posts = Posts.query.filter_by(department='COMPUTER').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/mechanical')
def mechanical():
    posts = Posts.query.filter_by(department='MECHANICAL').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/it')
def it():
    posts = Posts.query.filter_by(department='IT').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/extc')
def extc():
    posts = Posts.query.filter_by(department='EXTC').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/instrumentation')
def instrumentation():
    posts = Posts.query.filter_by(department='INSTRUMENTATION').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/chemical')
def chemical():
    posts = Posts.query.filter_by(department='CHEMICAL').all()
    return render_template('blogcategory.html', posts=posts, params=params)


@app.route('/tradtionalday2019')
def traditionalday2019():
    posts = Posts.query.filter_by(event='BAND WARS').all()
    return render_template('traditionalday2019.html')


app.run(debug=True)

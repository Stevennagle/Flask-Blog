# Flask-Blog

Based off of a tutorial by Corey Schafer (15 videos) :

     1) https://youtu.be/MwZwr5Tvyxo -- Complete
     2) https://youtu.be/QnDWIZuWYW0 -- Complete
     3) https://youtu.be/UIJKdCIEXUQ -- Complete
     4) https://youtu.be/cYWiDiIUxQc -- Complete
     5) https://youtu.be/44PvX0Yv368 -- Complete
     6) https://youtu.be/CSHx6eCkmv0 -- Complete
     7) https://youtu.be/803Ei2Sq-Zs -- Complete
     8) https://youtu.be/u0oDDZrDz9U -- Complete
     9) https://youtu.be/PSWf2TjTGNY -- Complete
     10)https://youtu.be/vutyTx7IaAI -- Complete
     11)https://youtu.be/Wfx4YBzg16s -- Complete
     12)https://youtu.be/uVNfQDohYNI -- 3min
----------------------------------------------------------------------


Issues, Video 9:


1) Username displays as file location :  e.g.  /user/Steven 2019-05-22
2) Email secure login info needs to be configured.



Issues, Video 11; 20:30min:


>>Searching 29 files for "url_for("
--should be 30




----------------------------------------------------------------------
Python installation issue :

	Error 0x80072efd: Cache thread exited unexpectedly.

	Solution : De-select "Download debugging symbols" or "Download debug binaries"

----------------------------------------------------------------------

CLI

     <CTRL>+`
     pip install flask

      export set FLASK_APP=flaskblog.py
     //$env:FLASK_APP = "run.py"
     http://127.0.0.1:5000/
     export set FLASK_DEBUG=1
     python flaskblog.py

     pip install flask-wtf

     <CTRL>+<SHIFT>+r : clear the browser cache and reload

     $ python
     >>> import secrets
     >>> secrets.token_hex(16)

     $ pip install flask-sqlalchemy

     python

     >>> from flaskblog import db
     >>> db.create_all()
     >>> from flaskblog import User, Post

     $ pip install flask-login
     $ pip install Pillow
     >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

     $ pip install flask-mail





----------------------------------------------------------------------

DB :

     >>> user_1 = User(username='Steven', email='sa@gmail.com', password='tempPassword')
     >>> db.session.add(user_1)
     >>> db.session.commit()
     >>> User.query.all()

     >>> User.query.first()
     >>> User.query.filter_by(username='John').all()
     >>> user = User.query.filter_by(username='John').first()
     >>> user.id

     >>> User.query.get(2)
     >>> post_2 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
     >>> db.session.add(post_2)
     >>> db.session.commit()

     >>> user.posts
     >>> for post in user.posts:
     ...     print (post.title)
     >>> post = Post.query.first()

     >>> post
     >>> post.user_id
     >>> post.author
     >>> db.drop_all()

     >>> User.create_all()
     >>> User.query.all()

----------------------------------------------------------------------

Hashing Passwords :

     $ pip install flask-bcrypt
     >>>from flask_bcrypt import Bcrypt
     >>>bcrypt = Bcrypt()

     >>> bcrypt.generate_password_hash('testing')
     b'$2b$12$gNtuAJE0/E3f2xYrP85MV.K1nGhQNXqekNC3zn.VX/eO0EmLkYram'

     >>> bcrypt.generate_password_hash('testing').decode('utf-8')
     '$2b$12$rQ7LfXiQbn2uQ8.WpoAtVO/Scuf2h2la20M49G2B8Ft9St7P107AG'

     >>> bcrypt.check_password_hash()
     >>> bcrypt.check_password_hash(hashed_pw, 'testing')



----------------------------------------------------------------------

Dependencies :

     BootStrap : https://getbootstrap.com/docs/4.3/getting-started/introduction/
     Flask : http://flask.pocoo.org/
     Flask Forms : https://flask-wtf.readthedocs.io/en/latest/index.html#
     sqlalchemy
     flask-bcrypt
     flask-login
     Pillow
     itsdangerous TimedJSONWebSignatureSerializer
     flask-mail
     Blueprint


----------------------------------------------------------------------

Email functionality :

  Using env vars to hide sensitive data (vid 10 - 26:45min)

     Environment Variables (Windows): https://youtu.be/IolxqkL7cD8
     Environment Variables (Mac and Linux): https://youtu.be/5iWhQWVXosU


----------------------------------------------------------------------

  Find and replace in SublimeText3:

     >>Find in Files

          Find:<Phrase> url_for(

          Where:
               >>...
               >>navigate to project folder

          Replace:

               >>Find
               >>Double click highlighted text to open relevent file

----------------------------------------------------------------------

Vid 11 -> 27:30min : env var setup
     $subl ~/.bash_profile
       add:
          app.config['SECRET_KEY']='7cd18ff261d5dbe21f54af94fb3a78cc'
          app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'


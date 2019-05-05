# Flask-Blog

Based off of a tutorial by Corey Schafer (15 videos) :

1) https://youtu.be/MwZwr5Tvyxo -- Complete
2) https://youtu.be/QnDWIZuWYW0 -- Complete
3) https://youtu.be/UIJKdCIEXUQ -- Complete
4) https://youtu.be/cYWiDiIUxQc -- Complete
5) https://youtu.be/44PvX0Yv368 --



----------------------------------------------------------------------
Python installation issue :

	Error 0x80072efd: Cache thread exited unexpectedly.

	Solution : De-select "Download debugging symbols" or "Download debug binaries"

----------------------------------------------------------------------
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


     >>> from flaskblog.models import User, Post


















----------------------------------------------------------------------
Issues :


----------------------------------------------------------------------

Dependencies :


BootStrap : https://getbootstrap.com/docs/4.3/getting-started/introduction/

Flask : http://flask.pocoo.org/

Flask Forms : https://flask-wtf.readthedocs.io/en/latest/index.html#


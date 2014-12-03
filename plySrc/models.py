import MySQLdb
from _mysql import OperationalError
from plySrc import app

try:
    db = MySQLdb.connect("localhost", "root", "", "plypress")
except OperationalError:
    app.logger.error("Database server might be down")
    exit()
finally:
    app.logger.debug("database connection established")

try:
    cursor = db.cursor()
    app.logger.debug("cursor fetched")
except:
    app.logger.error("cursor object not fetched")


def disconnect():
    try:
        db.close()
    except:
        app.logger.error("couldn't tear down db connection")

def fetch_posts():
    try:
        cursor.execute('select * from post_master')
        data = cursor.fetchall()
    except:
        app.logger.error("Couldn't execute fetch_posts")
    posts = []
    
    if posts == None:
        return None
    else:
        for i in data:
            posts.append({
                          'title':i[1],
                          'subtitle':i[2],
                          'date':i[4],
                          'username':i[5],
                          'text':i[3]})
    return posts

def fetch_post_by_id(id):
    try:
        
        cursor.execute("select * from post_master where post_id='%d'" % (id))
        data = cursor.fetchone()
    except:
        app.logger.error("Couldn't execute fetch_posts")

    post = {
           'title':data[1],
           'subtitle':data[2],
           'date':data[4],
           'username':data[5],
           'text':data[3]
           }
    return post
    
def insert_post(post):
    try:
        
        cursor.execute("select max(post_id) from post_master")
        post_id = cursor.fetchone()+1
        sql= "insert into post_master values (?,?,?,?,?,?)\
           [(post_id, post['title'], post['subtitle'], post['text'], post['date'], post['username'])]"
        cursor.execute(sql)
        cursor.commit()
    except:
        app.logger.error("Couldn't execute insert_posts")
    
    if post_id is None:
        return 0
    
    return post_id

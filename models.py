import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "plypress")
cursor = db.cursor()


def disconnect():
    db.close()

def fetch_posts():
    cursor.execute('select * from post_master')
    data = cursor.fetchall()
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
    cursor.execute("select * from post_master where post_id='%d'" % (id))
    data = cursor.fetchone()
    post = {
           'title':data[1],
           'subtitle':data[2],
           'date':data[4],
           'username':data[5],
           'text':data[3]
           }
    return post
    
def insert_post(post):
    cursor.execute("select max(post_id) from post_master")
    post_id = cursor.fetchone()+1
    sql= "insert into post_master values ('%d', '%s', '%s', '%s','%s','%s')\
       %(post_id, post['title'], post['subtitle'], post['text'], post['date'], post[username])"
    
    cursor.execute(sql)
    cursor.commit
    return post_id
    
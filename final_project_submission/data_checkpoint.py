# First data source
'''
YELP Fusion: We can sequentially ask users questions which will lead to a specific URL for yelp
several questions could included
1. Location
2. Price
3. type of food
4. distance
'''
#
import requests
from flask import Flask, render_template, request, Blueprint, redirect, url_for
import json
import sqlite3
conn = sqlite3.connect('user_temp.db', check_same_thread=False)
cur = conn.cursor()



app_data = Blueprint('check_point_file', __name__)

headers = {'Authorization': 'Bearer %s' % 'iwGMY9elHMjQqzt7rjlN9nerHSEYL-7zB0wvuMaRsOsgw_ntKrpjVlzWBwsmezjnNpaz8ypTnlEIvieJnnRAKbB3WrrVL2DSa2vE6KzElWCn_pVu6lUha7luToQ3YnYx'}
@app_data.route('/')
def home():
    return render_template('home_page.html')


@app_data.route('/form_category_and_user_location')
def form_user_category():
    return render_template('auto-complete.html') # just the static HTML

@app_data.route('/handle_form_category_and_user_location', methods=['POST'])
def generate_url():
    # user_pickup_or_delivery = request.form["options"]
    user_price = request.form["price"]

    user_category_list = request.form.getlist('option')
    user_location = request.form["user_address"]
    user_location_val_temp = user_location.split(',')[0].split()
    user_location_val = "_".join(user_location_val_temp)

    user_category = ",".join(user_category_list)
    #
    baseurl = "https://api.yelp.com/v3/businesses/search?categories=" + user_category + "&location=" + user_location + "&limit=50&sort_by=distance"
    response = requests.get(baseurl, headers=headers)
    all_info = json.loads(response.text)['businesses']

    field_names = ('name', 'rating', 'distance', 'price', 'transactions', 'image_url', 'categories', 'url')
    global table_name
    table_name = 'user_table' + user_location_val
    conn.execute('DROP TABLE IF EXISTS ' + table_name)
    conn.execute(
        'CREATE TABLE ' + table_name + ' (name_id integer primary key AUTOINCREMENT, name TEXT, rating REAL, distance REAL, price REAL, transactions TEXT, image_url TEXT, categories TEXT, url TEXT)')
    for ele in all_info:
        if 'price' not in ele:
            ele['price'] = ''
        insert_data = (
        ele['name'], str(ele['rating']), str(ele['distance']), str(ele['price']), ",".join(ele['transactions']),
        ele['image_url'], ",".join(e['alias'] for e in ele['categories']), ele['url'])
        conn.execute('INSERT INTO ' + table_name +  '(' + ','.join(field_names) + ') VALUES (' + ','.join('?' * len(insert_data)) + ')',
            insert_data)

    conn.commit()


    return redirect(url_for('check_point_file.process_data'))



def isLeaf(tree):
    parent = tree[0]
    left_child = tree[1]
    right_child = tree[2]
    if left_child is None and right_child is None:
        return True
    else:
        return False

def playLeaf(tree):
    parent = tree[0]
    left_child = tree[1]
    right_child = tree[2]
    return parent

def simplePlay(tree):
    parent = tree[0]
    left_child = tree[1]
    right_child = tree[2]
    if isLeaf(tree) is False:
        print(parent)
        ans = input("Your answer: ")
        if ans.lower() == "yes":
            return simplePlay(left_child)
        if ans.lower() == "no":
            return simplePlay(right_child)
    else:
        return playLeaf(tree)



# @app_data.route('/temp')
# def temp():
#     return render_template('response_add.html')


@app_data.route('/process_data')
def process_data():
    flag = True
    conn1 = sqlite3.connect('user_temp.db', check_same_thread=False)
    cur = conn1.cursor()
    temp = table_name
    a = cur.execute('SELECT name FROM {} LIMIT 1'.format(temp)).fetchall()[0][0]
    while flag:
        mediumTree = \
            ("Do you want to select a restaurant here?",
             ("Is it " + a + "?",
              ('I got it', None, None),
              ('Need to go a little further?',
               ('Adjusting distance for you', None, None),
               ('Need to get a higher rating restaurant?', ('Adjusting rating for you', None, None),
                ('Want to find a cheaper restaurant?', ('Adjusting price for you', None, None),
                 ('Do you want to deliver the food for you?', ('selecting delivery for you', None, None), ('selecting pickup for you', None, None)))))),
             (redirect('/form_category_and_user_location'), None, None))

        output = simplePlay(mediumTree)
        if output == 'I got it':
            t = table_name
            return redirect(cur.execute('SELECT url FROM {} ORDER BY distance LIMIT 1 '.format(t)).fetchall()[0][0])
        elif output.split()[1] == 'distance':
            t = table_name
            cur.execute('DELETE FROM {} WHERE name = ?'.format(t), (a,))
            t1 = table_name
            a = cur.execute('SELECT name FROM {} LIMIT 1'.format(t1)).fetchall()[0][0]
            conn1.commit()

        elif output.split()[1] == 'rating':
            t = table_name
            cur.execute('DELETE FROM {} WHERE name =?'.format(t), (a,))
            t1 = table_name
            query1 = '''
                        SELECT name
                        FROM {}
                        ORDER BY rating DESC, distance
                    '''
            a = cur.execute(query1.format(t1)).fetchall()[0][0]
            conn1.commit()
        elif output.split()[1] == 'price':
            t = table_name
            cur.execute('DELETE FROM {} WHERE name =?'.format(t), (a,))
            t1 = table_name
            query1 = '''
                        SELECT name
                        FROM {}
                        ORDER BY price, distance
                    '''
            a = cur.execute(query1.format(t1)).fetchall()[0][0]
            conn1.commit()

        elif output.split()[1] == 'delivery':
            print(output)
            t = table_name
            cur.execute('DELETE FROM {} WHERE name =?'.format(t), (a,))
            t1 = table_name
            query1 = '''
                        SELECT name
                        FROM {}
                        WHERE transactions = 'delivery' or transactions = 'delivery,pickup'
                    '''
            a = cur.execute(query1.format(t1)).fetchall()[0][0]
            conn1.commit()

        elif output.split()[1] == 'pickup':
            print(output)
            t = table_name
            cur.execute('DELETE FROM {} WHERE name =?'.format(t), (a,))
            t1 = table_name
            query1 = '''
                            SELECT name
                            FROM {}
                            WHERE transactions = '' or transactions = 'delivery,pickup'
                        '''
            a = cur.execute(query1.format(t1)).fetchall()[0][0]
            conn1.commit()


            


            # print(cur.execute('SELECT * FROM user_table1697_Broadway_Street').fetchall())

    return str(temp), str(type(temp))


# @app.route('/handle_form', methods=['POST'])
# def handle_the_form_user():
#
#     # response = requests.get("https://api.yelp.com/v3/businesses/search?categories=french,wine_bars&location=NYC",
#     #                         headers=headers)
#
#     # print(type(response.text))
#
#     json_str = response.text
#
#     user_location = request.form["user_address"]
#     # user_pickup_or_delivery = request.form["options"]
#     # user_min_price = request.form["min_price"]
#     # user_max_price = request.form["max_price"]
#     # user_category = request.form["category"]
#     user_location_list = user_location.split(",")
#     # stree = user_location_list[0]
#     # city = user_location_list[1]
#     # state = user_location_list[2]
#     country = user_location_list[3].strip()
#     if country != "USA":
#
#         return render_template("country_error.html")
#     else:
#         baseurl = 'https://api.yelp.com/v3/businesses/search?location=' + user_location + "&limit=50"
#         response = requests.get(baseurl, headers=headers)
#         json_str = response.text
#         all_info_list = json.loads(json_str)["businesses"]





    # return render_template('response_add.html', user_loc = user_location, user_pickup_or_delivery=user_pickup_or_delivery,
    #                        min_price = user_min_price, max_price = user_max_price, category = user_category)



#
if __name__ == '__main__':
    app_data.run(debug=True)
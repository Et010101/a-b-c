from flask import Flask, render_template

app = Flask(__name__)
GROUPS = [{
    'id': 1,
    'name': 'Popular Academic Subjects',
    's1': 'Science',
    's2': 'Computer cience',
    's3': 'Engineering'
}, {
    'id': 2,
    'name': 'Hobbies & Interests',
    's1': 'Creative Writing',
    's2': 'Cooking',
    's3': 'Fitness & Wellness'
},
 {
   'id': 3,
 'name': 'Support & Networking',
 's1': 'Mental Health Support',
 's2': 'LGBTQ Support',
 's3': 'Women In Area'
 },
#{ 'id': 4,
 # 'name': 'Miscellaneous',
 # 's1': 'Books Clubs',
 # 's2': 'Study Techniques',
 # 's3': 'Research Groups'}]


@app.route("/")
def hello_world():
  return render_template('home.html', groups=GROUPS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

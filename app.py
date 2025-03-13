from flask import Flask, render_template, request, redirect, session, jsonify
app = Flask(__name__)

likes = 0

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/api/link', methods=['POST'])
def like():
  global likes
  newlike = request.get_json()
  print(newlike)
  likes = likes + 1
  return 'Success', 200

@app.route('/apple/orange/', methods=['GET'])
def cow():
    print(jsonify(likes))
    return jsonify(likes)


if __name__ == '__main__':
  app.run()

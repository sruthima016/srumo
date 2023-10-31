from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/profile/<username>')
def profile(username):

    return render_template('profile.html',username=username,isActive=True)


@app.route('/books')
def book():

    books=[{'name':'book1','author':'abc1','cover':'https://momentaldesigns.com/wp-content/uploads/2017/05/TPW.jpg' },{'name':'book2','author':'abc','cover':'https://momentaldesigns.com/wp-content/uploads/2017/05/TPW.jpg'},
    {'name':'book3','author':'abc3','cover':'https://momentaldesigns.com/wp-content/uploads/2017/05/TPW.jpg'}]
    return render_template('book.html',books=books)
app.run(debug=True)
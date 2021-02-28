from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<li_type>')
def list_prof(li_type):
    li_prof = ['Проф.1', 'Проф.2', 'Проф.3']
    return render_template('list_prof.html', **{'li_type': li_type, 'li_prof': li_prof})


if __name__ == '__main__':
    app.run(port=5000, host='localhost')

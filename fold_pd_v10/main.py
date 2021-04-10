import flask

application = flask.Flask(__name__, template_folder='./')


@application.route('/')
def index():
    response = flask.render_template(
        template_name_or_list='add_user_form.html',
        title='Index',
    )
    return response


@application.route('/add_user/', methods=['GET', 'POST'])
def hello():
    if flask.request.method == 'GET':
        return flask.render_template('add_user_form.html')

    elif flask.request.method == 'POST':
        user_name = flask.request.form['user_name']
        email = flask.request.form['email']
        return flask.render_template('add_user_response.html', user_name=user_name, email=email)

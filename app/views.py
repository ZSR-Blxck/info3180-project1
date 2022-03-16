"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from .forms import createForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Zavier Rattray")


@app.route('/properties/create')
def createTemplate(error=None, error_msg=None, form=form):
    """Render the website's create page."""
    return render_template('create.html',error=error,error_msg=error_msg, form=form, title='Create Property')

if request.method != "POST": 
        return createTemplate()

    if 'photo' not in request.files: # Checking if image was sent with request
        return createTemplate('alert-warning', 'No photo uploaded!')

    _file = request.files['photo']

    # Validation of form data 
    # Checks that a file was submitted
    # Checks that file does not contain empty string
    # as filename

    if not (form.validate() or _file or _file.filename):
        return createTemplate(error='alert-danger', error_msg='Failed to Create Property!')

    filterUserData = dict(filter(lambda attr: attr[0] in User.attrs, form.data.items())) 
    photo = secure_filename(_file.filename)
    _file.save(os.path.join(app.config['UPLOAD_FOLDER'], photo))  

    # Updating filtered user data dictionary with property photo
    # filename, as well as, save the new user data to database

    filterUserData['profileImage'] = profileImage 
    save_user(filterUserData) 

    flash('Success!', 'alert-success')
    return redirect(url_for('properties'))

@app.route('/properties')
def properties():
    properties=property.query.all()
    return render_template(properties.html)

@app.route('/properties/ <propertyid>')
def getProperty(propertyid):
    prop= property.query.get(propertyid)
    propertyName=f'{property.title}'
    return render_template('property.html',property=property, title=propertyName)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash
from app.forms import CreateForm
from app.models import PropertyInfo


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


@app.route('/properties/create/', methods=['GET','POST'])
def create():
    """Render the website's create page."""
    #return render_template('createProperty.html')
    form=CreateForm()
    
    if request.method == 'POST':
    #     if form.validate_on_submit():
        p1= PropertyInfo(request.form['propTitle'],request.form['descr'],request.form['rooms'],request.form['btroom'],request.form['price'],request.form['pType'], request.form['location'])
        db.session.add(p1)
        db.session.commit()
        flash('Success!')
        return redirect(url_for('properties')) 
    #     else:            
    #         flash('Errror!') 
    #         return redirect(url_for("home"))  
    return render_template('create.html',form=form)
    

@app.route('/properties/')
def properties():
    #propertys= db.session.query(PropertyInfo).all()
    return render_template('properties.html')

@app.route('/properties/ <propertyid>')
def getProperty(propertyid):
    prop= db.session.query.get(propertyid)
    propertyName=f'{db.session.propTitle}'
    return render_template('properties.html',property=prop, title=propertyName)
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

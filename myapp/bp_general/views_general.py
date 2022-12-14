from myapp.bp_general import bp_general
from flask import render_template, url_for, redirect, request, flash, abort

@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    return render_template('general/home.html', title='GriGriVerse')

@bp_general.route('/forum')
def do_forum():
    return render_template('general/forum.html', title='Forum')

@bp_general.route('/tutorials')
def do_tutorials():
    return render_template('general/tutorials.html', title='Tutorials')

@bp_general.route('/contact')
def do_contact():
    return render_template('general/contact.html', title='Contact')

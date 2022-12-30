from myapp.bp_tutorials import bp_tutorials
from flask import render_template, url_for, redirect, request, flash, abort


@bp_tutorials.route('/tutorials/minecraft_version')
def do_tutorials_minecraft_version():
    return render_template('tutorials/minecraft_version.html', title='Minecraft version')

@bp_tutorials.route('/tutorials/join_server')
def do_tutorials_join_server():
    return render_template('tutorials/join_server.html', title='Join server')

@bp_tutorials.route('/tutorials/server_commands')
def do_tutorials_server_commands():
    return render_template('tutorials/server_commands.html', title='Server commands')

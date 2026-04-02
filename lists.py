from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from dbstruct import db, movielist

lists = Blueprint('lists', __name__)

@lists.route('/create_list', methods=['POST'])
def createList():
    if 'userID' not in session:
        flash("must be logged in")
        return redirect(url_for('auth.login'))

    listName = request.form.get('name')
    if not listName:
        flash("list name cannot be empty")
        return redirect(request.referrer or url_for('movies.my_lists'))

    newList = movielist(name=listName, userID=session['userID'])
    db.session.add(newList)
    db.session.commit()
    flash(f"created list: {listName}")
    return redirect(url_for('movies.my_lists'))

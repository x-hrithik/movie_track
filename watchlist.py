from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from dbstruct import db, movie, movielist

movies = Blueprint('movies', __name__)

@movies.route('/add_movie', methods=['POST'])
def addMovie():

    if 'userID' not in session:
        flash("must be logged in")
        return redirect(url_for('auth.login'))

    movieTitle = request.form.get('title')
    moviePoster = request.form.get('poster')
    movieTmdbId = request.form.get('tmdb_id')
    listIds = request.form.getlist('list_id')

    if not listIds:
        flash("select at least one list")
        return redirect(request.referrer or url_for('home'))

    existing_movie = movie.query.filter_by(
        userID=session['userID'], 
        tmdbID=movieTmdbId
    ).first()

    if existing_movie:
        new_movie = existing_movie
    else:
        new_movie = movie(
            title=movieTitle,
            posterURL=moviePoster,
            tmdbID=movieTmdbId,
            userID=session['userID']
        )
        db.session.add(new_movie)
        db.session.commit()

    added_to = []
    for list_id in listIds:
        listObj = movielist.query.filter_by(id=list_id, userID=session['userID']).first()
        if listObj:
            if new_movie not in listObj.movies:
                listObj.movies.append(new_movie)
                added_to.append(listObj.name)

    if added_to:
        db.session.commit()
        flash(f"added {movieTitle} to {', '.join(added_to)}")
    else:
        flash(f"{movieTitle} is already in those lists")

    return redirect(request.referrer or url_for('home'))

@movies.route('/remove_movie/<int:movieId>', methods=['POST'])
def removeMovie(movieId):
    if 'userID' not in session:
        return redirect(url_for('auth.login'))
    
    listId = request.form.get('list_id')
    movieRemove = movie.query.filter_by(id=movieId, userID=session['userID']).first()
    
    if movieRemove:
        listObj = movielist.query.filter_by(id=listId, userID=session['userID']).first()
        if listObj and movieRemove in listObj.movies:
            listObj.movies.remove(movieRemove)
            db.session.commit()
            flash(f"removed {movieRemove.title} from {listObj.name}")
            if not movieRemove.lists:
                db.session.delete(movieRemove)
                db.session.commit()
        else:
            flash("list not found")
    else:
        flash("movie not found")
        
    return redirect(request.referrer or url_for('home'))

@movies.route('/my_lists')
def my_lists():

    if 'userID' not in session:
        return redirect(url_for('auth.login'))

    userId = session['userID']
    userLists = movielist.query.filter_by(userID=userId).all()

    return render_template('watchlist.html', lists=userLists)
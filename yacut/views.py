from flask import flash, redirect, render_template

from settings import LOCAL_URL

from . import app, db
from .forms import YacutForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        short_link = form.custom_id.data
        if URLMap.query.filter_by(short=short_link).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        if form.custom_id.data:
            short_link = form.custom_id.data
        else:
            short_link = get_unique_short_id()
        url_map_object = URLMap(
            original=form.original_link.data,
            short=short_link,
        )
        db.session.add(url_map_object)
        db.session.commit()
        flash('Ссылка была успешно сгенерирована')
        return render_template('index.html', form=form, short_link=LOCAL_URL + short_link)
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>')
def redirect_view(custom_id):
    """View-функция переадресации на исходный адрес."""
    return redirect(
        URLMap.query.filter_by(short=custom_id).first_or_404().original
    )

from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import check_custom_id
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    custom_id = data.get('custom_id')
    if custom_id and custom_id != '':
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
        if not check_custom_id(custom_id):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST)
    else:
        custom_id = get_unique_short_id()
    data['custom_id'] = custom_id
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    short = URLMap.query.filter_by(short=short_id).first()
    if short is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': short.original}), HTTPStatus.OK

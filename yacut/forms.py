from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


class YacutForm(FlaskForm):
    original_link = URLField(
        'Введите длинное название ссылки',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Некорректный URL')]
    )
    custom_id = StringField(
        'Введите короткое название ссылки',
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField('Создать')

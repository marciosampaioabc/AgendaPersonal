from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, DecimalField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    valor = DecimalField('Valor', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()], format='%Y-%m-%d')
    hora = TimeField('Hora', validators=[DataRequired()], format='%H:%M')
    submit = SubmitField('Submit')
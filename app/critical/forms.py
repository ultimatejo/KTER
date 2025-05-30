from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import  DataRequired


class CritVelForm(FlaskForm):
    tunWid = DecimalField('Tunnel width (m)', validators=[DataRequired()])
    tunHei = DecimalField('Tunnel height (m)', validators=[DataRequired()])
    blkAra = DecimalField('Blockage area (m²)', validators=[DataRequired()])
    ambTmp = DecimalField('Ambient temperature (°C)', validators=[DataRequired()])
    submit = SubmitField('Calculate')
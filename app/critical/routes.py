from datetime import datetime
from flask import render_template, flash, make_response
from flask_login import current_user, login_required
from app import db
from app.critical.forms import CritVelForm
from app.critical.critVel import main as cv
from app.critical import bp


#@bp.before_request
#def before_request():
#    if current_user.is_authenticated:
#        current_user.last_seen = datetime.utcnow()
#        db.session.commit()


@bp.route('/critVel', methods=['GET','POST'])
def critVel():
    form = CritVelForm()
    if form.validate_on_submit():
        # Check inputs to ensure that they are reasonable
        if float(form.tunWid.data) < 0:
            flash('Tunnel width must be greater than zero')
            return render_template('critical/critVel.html', title='Critical Velocity',form=form)
        if float(form.tunHei.data) < 0:
            flash('Tunnel height must be greater than zero')
            return render_template('critical/critVel.html', title='Critical Velocity',form=form)
        if float(form.blkAra.data) < 0:
            flash('Blockage area must be greater than zero')
            return render_template('critical/critVel.html', title='Critical Velocity',form=form)
        if 50 < float(form.ambTmp.data) or float(form.ambTmp.data) < -15:
            flash('Ambient temperature must be between -15 and 50°C')
            return render_template('critical/critVel.html', title='Critical Velocity',form=form)

        #flash('Input correct')
        dict_key = [1,2,3,4]
        dData = {}
        dData[dict_key[0]] = {'label':'Tunnel width','value':form.tunWid.data,'units':'m'}
        dData[dict_key[1]] = {'label':'Tunnel height','value':form.tunHei.data,'units':'m'}
        dData[dict_key[2]] = {'label':'Blockage area','value':form.blkAra.data,'units':'m²'}
        dData[dict_key[3]] = {'label':'Ambient temperature','value':form.ambTmp.data,'units':'°C'}
        cv(float(form.tunWid.data),float(form.tunHei.data),float(form.blkAra.data),float(form.ambTmp.data))
        response = make_response(render_template('critical/critVel.html', title='Critical Velocity',form=form,dData=dData,dict_key=dict_key))
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
        response.headers["Pragma"] = "no-cache" # HTTP 1.0.
        response.headers["Expires"] = "0" # Proxies.
        return response
    else:
        return render_template('critical/critVel.html', title='Critical Velocity',form=form)

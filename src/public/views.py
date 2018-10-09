"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash
from .forms import LogUserForm, secti,masoform,RychlostForm
from ..data.database import db
from ..data.models import LogUser,Rychlost
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/rychlost', methods=['GET'])
def rychlost():
    form =RychlostForm()
    if form.is_submitted():
        Rychlost.create(**form.data)
        flash('ulozeno')
        print(form.rychlost.data)
    return render_template('public/rychlost.tmpl',form=form)

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)






@blueprint.route('/pole',methods=['GET'])
def indexpole():
    pole = [[1, 'x'], [2,'y'],[3,'z']]
    return render_template("public/vystup1.tmpl",pole = pole)









@blueprint.route('/dph', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.vyrobek.data,hod2=form.ks.data,hod3=form.cena.data,hod4=form.DPH.data,suma=form.ks.data*form.cena.data*form.DPH.data)
    return render_template('public/secti.tmpl', form=form)






















@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

from flask import Blueprint, render_template, request, redirect, url_for, redirect, session, current_app, jsonify

from .forms import InsertForm, ChangeForm, SearchForm

from lager import db
from .models import Ware
from .db import searchQuery


ROWS_PER_PAGE = 10
ware_bp = Blueprint('ware', __name__)

@ware_bp.route("/", methods=['GET', 'POST'])
def indexpage(page=1):
    currentpage = request.args.get('page', 1, type=int)
    daten = Ware.query.paginate(page=currentpage, per_page=ROWS_PER_PAGE, )
    return render_template('start/index.html', daslager=daten, thisurl="ware.indexpage", currentpage=currentpage, totalpages=daten.pages)



@ware_bp.route("/item", methods=['GET', 'POST'])
def itempage():
    currentitem = request.args.get('currentid', 1, type=int)
    current = Ware.query.get(int(currentitem))
    return render_template('items/item.html', current=current)


@ware_bp.route("/searchresults", methods=['GET', 'POST'])
def searchresultspage():
    if request.method == 'GET':
        currentpage = request.args.get('page', 1, type=int) 
        
        
        lastpage = session['currentpage']
        rowsperpage = session['rowsperpage']
        nritemstotal = session['nritemstotal']
        totalpages = session['totalpages']
        
        if(currentpage == lastpage):
            currentitems = session['paginationobj_current']
        else:
            ## TODO iterate throu allitems until current selection
            currentitems = session['paginationobj_all'][rowsperpage * (currentpage-1):rowsperpage * (currentpage-1) + rowsperpage]

        return render_template('/search/searchresults.html', daslager = currentitems, thisurl="ware.searchresultspage", currentpage=currentpage, totalpages=totalpages)
    else:
        currentid = request.args.get('currentid', 1, int)
        return redirect(f'/item?currentid={currentid}')
    
    

@ware_bp.route("/search", methods=['GET', 'POST'])
def searchpage():
    form = SearchForm(request.form)

    if request.method == 'GET':
        return render_template('search/search.html', form=SearchForm())
    else:
        lagerplatz=form.lagerplatz.data
        produktname=form.produktname.data
        kategorie=form.kategorie.data if form.kategorie.data != "default" else None
        preismin=round(float(form.preismin.data), 2) if form.preismin.data else None
        preismax=round(float(form.preismax.data), 2) if form.preismax.data else None
        designer=form.designer.data
        label=form.label.data
        ausziehbar=form.ausziehbar.data if form.ausziehbar.data else None
        klappbar=form.klappbar.data if form.klappbar.data else None
        
        results = searchQuery(lagerplatz=lagerplatz, 
                              produktname=produktname, 
                              kategorie=kategorie, 
                              preismax=preismax, 
                              preismin=preismin, 
                              designer=designer, 
                              label=label, 
                              ausziehbar=ausziehbar, 
                              klappbar=klappbar,
                              rpp=ROWS_PER_PAGE)
        
        session["paginationobj_all"] =results['allitems']
        session["paginationobj_current"] = results['currentitems']
        session["currentpage"] = results['currentpage']
        session["rowsperpage"] = results['rowsperpage']
        session["nritemstotal"] = results['nritemstotal']
        session["totalpages"] = results['totalpages']

        
        return redirect('/searchresults')
    
   
        



@ware_bp.route("/modify", methods=['GET', 'POST'])
def modifypage():
    currentpage = request.args.get('page', 1, type=int)
    daten = Ware.query.paginate(page=currentpage, per_page=ROWS_PER_PAGE, )
    return render_template('modify/modify.html', daslager=daten, thisurl="ware.modifypage", currentpage=currentpage, totalpages=daten.pages)



@ware_bp.route("/changeitem", methods=['GET', 'POST'])
def changeitempage():
    currentid = request.args.get('currentid', 1, type=int)
    current = Ware.query.get(currentid)
    form = ChangeForm()
    if request.method == 'GET':
        form.lagerplatz.data = current.lagerplatz
        form.produktname.data = current.produktname

        form.kategorie.data = current.kategorie
        form.preis.data = current.preis
        form.designer.data = current.designer
        form.label.data = current.label
        form.ausziehbar.data = current.ausziehbar
        form.klappbar.data = current.klappbar
        
        return render_template('modify/changeitem.html', current=current, form=form)
    else:
         ## delete old
        todelete = current
        db.session.delete(todelete)
        db.session.commit()
        
        ## add new
        stueck = Ware(
            lagerplatz=form.lagerplatz.data,
            produktname=form.produktname.data,
            kategorie=form.kategorie.data if form.kategorie.data != "default" else None,
            preis=round(float(form.preis.data), 2)  if form.preis.data else None,
            designer=form.designer.data,
            label=form.label.data,
            ausziehbar = form.ausziehbar.data if form.ausziehbar.data else None,
            klappbar = form.klappbar.data if form.klappbar.data else None,
            
        )
        
        db.session.add(stueck)
        db.session.commit()
        
        return redirect('/change')

    
    
    


@ware_bp.route("/change", methods=['GET', 'POST'])
def changepage(page=1):
    if request.method == 'GET':
        currentpage = request.args.get('page', 1, type=int)
        daten = Ware.query.paginate(page=currentpage, per_page=ROWS_PER_PAGE, )
        return render_template('modify/change.html', daslager=daten, thisurl="ware.changepage", currentpage=currentpage, totalpages=daten.pages)
    else:
        
        
        if 'radiobttn' in request.form:
            return redirect(url_for('changeitempage', currentid=str(request.form['radiobttn'])))
        else:
            return redirect('/change')

        # alldata = Ware.query.all()
        
        # for i in alldata:
        #     if request.form.get(str(i.id)):
        #         return redirect(url_for('changeitempage', currentid=i.id))
        # else:
        #     return redirect('/change')
        
           


@ware_bp.route("/delete", methods=['GET', 'POST'])
def deletepage(page=1):
    if request.method == 'GET':
        currentpage = request.args.get('page', 1, type=int)
        daten = Ware.query.paginate(page=currentpage, per_page=ROWS_PER_PAGE)
        return render_template('modify/delete.html', daslager=daten, currentpage=currentpage, totalpages=daten.pages, thisurl="deletepage")
    else:
        ## TO BE EXTENDED TO GETTING MORE THAN ONE 

        
        alldata = Ware.query.all()
        
        for i in alldata:
            if request.form.get(str(i.id)):
                todelete = Ware.query.get(i.id)
                db.session.delete(todelete)
                db.session.commit()
        
        return redirect('/')




@ware_bp.route("/insert", methods=['GET', 'POST'])

def insertpage():
    form = InsertForm(request.form)
    if request.method == 'POST':
        stueck = Ware(
            lagerplatz=form.lagerplatz.data,
            produktname=form.produktname.data,
            kategorie=form.kategorie.data if form.kategorie.data != "default" else None,
            preis=round(float(form.preis.data), 2) if form.preis.data else None,
            designer=form.designer.data,
            label=form.label.data,
            ausziehbar = form.ausziehbar.data if form.ausziehbar.data else None,
            klappbar = form.klappbar.data if form.klappbar.data else None,
        )
        
        db.session.add(stueck)
        db.session.commit()
        daten = Ware.query.paginate(page=1, per_page=ROWS_PER_PAGE)
        return redirect('/')
    daten = Ware.query.all()    
    return render_template('modify/insert.html', daslager=daten, form=InsertForm())

        
    
        
        




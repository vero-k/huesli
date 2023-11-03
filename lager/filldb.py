
from re import T
from lager import db, ma, Ware

import sqlite3

import click
from flask import current_app, g


def insert_Ware(db):

    stuck1 = Ware(
    lagerplatz=1,
    produktname='Sofa Maria',
    kategorie='Sofa',
    preis=34,
    designer='Klaudia',
    label='tt',
    )

    stuck2 = Ware(
        lagerplatz=2,
        produktname='Sofa Blau',
        kategorie='Sofa',
        preis=32.1
        
    )

    stuck3 = Ware(
        lagerplatz=3,
        produktname='Gelber Stuhl',
        kategorie="Stuhl",
        preis=11,
        klappbar=True,
    )

    stuck4 = Ware(
        lagerplatz=4,
        produktname='N Tisch',
        kategorie="Tisch",
        preis=100,
        ausziehbar=True,
        designer="Rose"
    )


    stuck5 = Ware(
        lagerplatz=54,
        produktname='Jeff',
        kategorie="Tisch",
        preis=2433,
        klappbar=True,
    )


    stuck6 = Ware(
        lagerplatz=63,
        produktname='Regalite',
        kategorie="Regal",
        preis=123,
    )


    stuck7 = Ware(
        lagerplatz=7,
        produktname='blauessofa'
    )


    stuck8 = Ware(
        lagerplatz=82,
        produktname='Blaues Sofa'
    )



    stuck9 = Ware(
        lagerplatz=111,
        produktname='Schweres Sofa',
        kategorie='Sofa',
        preis=34,
        designer='jemand',
        label='tt',
    )

    stuck10 = Ware(
        lagerplatz=21,
        produktname='Leichtes Sofa',
        kategorie='Sofa',
        preis=32.1
        
    )

    stuck11 = Ware(
        lagerplatz=33,
        produktname='Hellblauer Stuhl'
    )

    stuck12 = Ware(
        lagerplatz=40,
        produktname='Expedite'
    )


    stuck13 = Ware(
        lagerplatz=59,
        produktname='Jeff Nr1'
    )


    stuck14 = Ware(
        lagerplatz=3465,
        produktname='Sessel TV'
    )


    stuck15 = Ware(
        lagerplatz=322,
        produktname='Grosses Bucherregal'
    )


    stuck16 = Ware(
        lagerplatz=3452,
        produktname='Abstelltisch'
    )



    db.session.add(stuck1)
    db.session.add(stuck2)
    db.session.add(stuck3)
    db.session.add(stuck4)
    db.session.add(stuck5)
    db.session.add(stuck6)
    db.session.add(stuck7)
    db.session.add(stuck8)
    db.session.add(stuck9)
    db.session.add(stuck10)
    db.session.add(stuck11)
    db.session.add(stuck12)
    db.session.add(stuck13)
    db.session.add(stuck14)
    db.session.add(stuck15)
    db.session.add(stuck16)
    db.session.commit()




            
def searchQuery(lagerplatz=None, produktname=None, kategorie=None, preismax=None, preismin=None, designer=None, label=None, ausziehbar=None, klappbar=None, currentpage=1, rpp=10):
    
    
    prelimQ = None
    
    if lagerplatz:
        prelimQ = db.session.query(Ware).filter(Ware.lagerplatz == lagerplatz)
    
    
    if produktname:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.produktname.contains(produktname))
        else:
            prelimQ = db.session.query(Ware).filter(Ware.produktname.contains(produktname))
            
    if kategorie:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.kategorie == kategorie)
        else:
            prelimQ = db.session.query(Ware).filter(Ware.kategorie == kategorie)
            
    
    if preismax:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.preis <= preismax)
        else:
            prelimQ = db.session.query(Ware).filter( Ware.preis <= preismax)
    
    
    if preismin:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.preis >= preismin)
        else:
            prelimQ = db.session.query(Ware).filter(Ware.preis >= preismin)
    
    
    if designer:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.designer.contains(designer))
        else:
            prelimQ = db.session.query(Ware).filter(Ware.designer.contains(designer))
    
            
    if label:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.label.contains(label))
        else:
            prelimQ = db.session.query(Ware).filter(Ware.label.contains(label))
    
    
    if ausziehbar != None:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.ausziehbar == ausziehbar)
        else:
            db.session.query(Ware).filter(Ware.ausziehbar == ausziehbar)
    
    
    if klappbar != None:
        if prelimQ:
            prelimQ = prelimQ.filter(Ware.klappbar == klappbar)
        else:
            db.session.query(Ware).filter(Ware.klappbar == klappbar)
            
    
    # TODO 
           
    allitemsarray = prelimQ.all()
    allitems = []
    for w in allitemsarray:
        thisdict = {}
        thisdict['id'] = w.id
        thisdict['produktname'] = w.produktname
        thisdict['preis'] = w.preis
        thisdict['kategorie'] = w.kategorie
        thisdict['desginer'] = w.designer
        thisdict['label'] = w.label 
        thisdict['ausziehbar'] = w.ausziehbar
        thisdict['klappbar'] = w.klappbar
        thisdict['laberplatz'] = w.lagerplatz
        allitems.append(thisdict)
        
        
        
    currentitems = allitems[0:rpp]
    
   
    
    return {
        "currentitems": currentitems,
        "currentpage": currentpage,
        "rowsperpage": rpp,
        "nritemstotal": len(allitemsarray),
        "allitems": allitems,
        "totalpages": 1,
    }
    
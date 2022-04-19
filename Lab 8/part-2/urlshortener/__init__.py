# Carson Carpenter
# CPSC 223P-03
# 2020-12-1
# carson.carpenter7@csu.fullerton.edu
#
from flask import Flask, redirect, url_for, flash, render_template, request
from .config import Config
from .models import db, ShortUrl
from .cli import create_db
import datetime
import math as m
from collections import deque
import numpy as np


app = Flask(__name__)
app.config.from_object(Config)
app.cli.add_command(create_db)
db.init_app(app)
#print('Done: http://127.0.0.1:5000/home')

ALPHABET_62 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')


@app.route('/list', methods=['GET', 'POST'])
def listing():
    if request.method == 'POST':
        if request.form['tpl_do'] == 'View Short URL':
            queried_data = ShortUrl.query.all()
            return render_template('list.html', tplt_url = queried_data)
    else:
        return redirect(url_for('home'))


def urlshortener(ENCODED):
        out_64 = deque()
        next = int(ENCODED)
        while (next > 0):
            quotient = m.floor(next/62)
            remainder = next if quotient == 0 else next % 62
            out_64.appendleft(ALPHABET_62[remainder])
            next = quotient
        return ''.join(i for i in out_64)


def originalurl(KEY):
        key_obj = KEY
        ar = np.arange(0,len(str(key_obj)))[::-1]
        s = list(zip(key_obj,ar))
        out_10 = sum(ALPHABET_62.index(i)*m.pow(62,j) for i,j in s )
        return out_10


@app.route('/shortening', methods=['GET', 'POST'])
def shortening():
    o_url_raw = str()
    if request.method == 'POST':
        temp = request.form['tplt_url']
        o_url_raw = temp
    temp_new_url = ShortUrl(original_url=o_url_raw, short_url=o_url_raw+"dummy")
    created_at=datetime.datetime.now()
    db.session.add(temp_new_url)
    db.session.commit()
    key_obj = ShortUrl.query.order_by(-ShortUrl.id).first()
    key_obj.short_url = urlshortener(key_obj.id)
    db.session.commit()
    return render_template('show.html', tplt_short=key_obj.short_url)


@app.route('/find/<shortcode>')
def searchURL(shortcode):
    p_key = originalurl(shortcode)
    found_user = ShortUrl.query.get(int(p_key))
    if found_user is None:
        flash("There is currently no record associated with that short url.")
        return redirect(url_for('home'))
    else:
        return render_template('search.html', tplt_original_url = found_user.original_url)


@app.route('/f', methods=['GET', 'POST'])
def searchURL_onscreen():
    if request.method == 'POST':
        key_obj = request.form['tplt_findurl']
        return redirect(url_for('searchURL', shortcode = key_obj))
    else:
        return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    rec = ShortUrl.query.get(int(id))
    db.session.delete(rec)
    db.session.commit()
    return redirect(url_for('listing'))

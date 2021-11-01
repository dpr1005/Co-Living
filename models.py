#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    models.py
# @Author:      Daniel Puente Ramírez
# @Time:        1/11/21 17:46

import sqlite3
from os import path

ROOT = path.dirname(path.relpath(__file__))


def create_post(name, content):
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()


def get_post():
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    con.commit()
    con.close()
    return posts

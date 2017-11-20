# coding: utf-8

import os
import pymysql
import json
import pandas as pd


def connect_to_db():
    """
    Connect to the public enwiki db using quarry.wmflabs.org credentials
    """
    conn = pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USERNAME'],
        password=os.environ['MYSQL_PASSWORD'],  # don't print me!

        database='enwiki_p',
        charset='utf8',
        use_unicode=True
    )
    return conn


conn = connect_to_db()


f = open('mid-level-wp.json', 'r')
wps = json.loads(f.read())['wikiprojects']
f.close()


i = 0
results = []
skipped = []
for wp in wps:
    wikiprojects = wps[wp]
    w_processed = list(map(lambda k: "'{}'".format(k[10:].replace(' ', '_')),
                           wikiprojects))
    query = """SELECT tl_from, tl_title, tl_namespace, page.page_title
        FROM templatelinks INNER JOIN page
        ON templatelinks.tl_from=page.page_id
        WHERE tl_title IN ( {} )
        AND tl_namespace = 10 AND page.page_namespace = 1
        AND page.page_is_redirect = 0
        ORDER BY RAND() LIMIT 2000""".format(','.join(w_processed))
    print("processing {}".format(wp))
    try:
        with conn.cursor() as cur:
            cur.execute('use enwiki_p;')
            cur.execute(query)
            result = cur.fetchall()
            with open('wp-pairs', 'a') as fin:
                for tup in result:
                    new_tup = (tup[0], tup[1].decode('utf-8'),
                               tup[2], tup[3].decode('utf-8'))
                    results.append((*new_tup, wp))
    except:
        skipped.append(wp)
        print("skipping {}".format(wp))

df = pd.DataFrame(results)
df.to_csv('wp-pairs', sep='\t', header=['talk_page_id', 'wikiproject',
                                        'namespace', 'talk_page_title',
                                        'category'])

f = open('skipped', 'w')
f.write(json.dumps(skipped))
f.close()

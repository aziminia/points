# -*- coding: utf-8 -*-

from django.shortcuts import render
import requests
import json
from .models import Points, Logo, Rates, Guilds, Knots, Filters
from time import sleep


def index(request):
    # r = requests.get(
    #     'http://ibartar.com/api/v1.1/page/search?order_by=random&has_logo=1&guild=1&area=%D8%AA%D9%87%D8%B1%D8%A7%D9%86&chanel=menu&s_id=9fa89e0b-2c1a-4abc-a922-a708557bf749&device_type=desktop')
    r = requests.get(
        'http://ibartar.com/api/v1.1/page/search?page=1&area=%D8%AA%D9%87%D8%B1%D8%A7%D9%86')
    c = r.content
    all = json.loads(c)
    for alls in range(1, all['last_page']):
        sleep(0.05)
        req = requests.get(
            'http://ibartar.com/api/v1.1/page/search?page=1&area=%D8%AA%D9%87%D8%B1%D8%A7%D9%86&page=' + str(
                alls))
        req_content = req.content
        req_all = json.loads(req_content)

        for l in req_all['data']:
            logo = None
            if 'logo' in l:
                if 'FullSize' in l['logo']:
                    fullsize = l['logo']['FullSize']
                else:
                    fullsize = None
                if 'small' in l['logo']:
                    small = l['logo']['small']
                else:
                    small = None

                logo = Logo(full_size=fullsize, small=small)
                logo.save()

            rates = None
            if 'rates' in l:
                rates = Rates(count=l['rates']['count'],
                              credibility=l['rates']['credibility'],
                              popularity=l['rates']['popularity'],
                              reliability=l['rates']['reliability'],

                              )
                rates.save()

            if 'slogan' in l:
                slogan = l['slogan']
            else:
                slogan = None

            if 'tel_1' in l:
                tel_1 = l['tel_1']
            else:
                tel_1 = None
            points = Points(address=l['address'],
                            has_active_contract=l['has_active_contract'],
                            point_id=l['id'],
                            lat=l['lat'],
                            lng=l['lng'],
                            slogan=slogan,
                            slugged_title=l['slugged_title'],
                            status=l['status'],
                            tel_1=tel_1,
                            title=l['title'],
                            uuid=l['uuid'],
                            )
            points.save()
            if logo:
                points.logo = logo
            if rates:
                points.rates = rates
            points.save()

            for g in l['guilds']:
                guilds = Guilds(g_id=g['id'], title=g['title'])
                guilds.save()
                points.guilds.add(guilds)

            for k in l['knots']:
                knots = Knots(k_id=k['id'])
                knots.save()
                points.knots.add(knots)

        for f in req_all['filters']:
            filter = Filters(doc_count=f['doc_count'], key=f['key'], title=f['title'])
            filter.save()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response

import bs4
import json
from django.shortcuts import render
from bs4 import BeautifulSoup as soup
import requests


def index(request):

	my_url = "https://www.iproperty.com.my/rent/all-residential/?q=bangsar"
	request_page = requests.get(my_url)
	page_soup = soup(request_page.text,"html.parser")
	containers = page_soup.findAll("div",{"class":"RTdSn"})
    	result_list = []
    	results = []
    	data = []

    	for contain in containers:
        	title = contain.find("h3",{"class":"cgiArp"})
        	price = contain.find("div",{"class":"kOgHVE"})
        	address = contain.find("div",{"class":"cjKwZF"})
        	bathroom = contain.find("li",{"class":"bathroom-facility"})
        	bedrrom = contain.find("li",{"class":"bedroom-facility"})

        	try:
            		try:
                		temp = contain.find("li",{"class":"builtUp-attr"})
                		square = temp.find("a",{"class":"attrs-price-per-unit-desktop"})
                		success = True
            		except:
                		success = False
                		pass
            		try:
                		temp2 = contain.find("li",{"class":"furnishing-attr"})
                		furnish = temp2.find("a",{"class":"attrs-price-per-unit-desktop"})

                		if not success:
                    			data = [title,price,address,bathroom,bedroom,furnish]
                		else:
                    			data = [title,price,address,bathroom,bedroom,square,furnish]
            		except:
                		pass
        	except:
            		data = [title,price,address,bathroom,bedroom]

        	for x in data:
            		result_list.append(x.text)

        	results.append(result_list)

	
    	return render_to_response(request,"index.html",results)


# Create your views here.

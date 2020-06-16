from bs4 import BeautifulSoup as bsf
import requests
import urllib 
import re
import csv

header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
fp = open("amazon.html","a")
page = requests.get("https://www.amazon.in/s?k=detroit+become+human&crid=ZE5VZO2SN8JD&sprefix=detroit+become+humans%2Caps%2C-1&ref=nb_sb_ss_sc_1_9",headers = header)
# fp.writelines(str(page.content))
page = str(page.content)
soup = bsf(page,'html.parser')
item_list = soup.findAll('div',{'class':"sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"}) 
final_list=[]
for i in item_list:
    content_dict =dict()
    image = i.findAll("img",{'class': 's-image'})
    image= image[0]
    img_link = image['src']

# ---------------------------
    content = i.findAll("a",{"class":"a-link-normal a-text-normal"})
    content = content[0]
    link_content = content['href']
    title_content = content.text
    title_content = title_content.replace(r"\n"," ").strip()

# ------------------------

    rating = i.findAll('span',{"class":"a-icon-alt"})
    rating = rating[0]
    rating_content = rating.text

    content_dict["image"] = img_link
    content_dict["title"] = title_content
    content_dict["title_link"] = link_content
    content_dict["rating"] = rating_content
    final_list.append(content_dict)
# fp.write("""<html><head>
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
#     </head>
    
#     <body><table class="table table-bordered table-dark">""")

for items in final_list:
    fp.write("<tr>")
    for key , item in items.items():
        if key == "image":
            fp.write("<td><img src = '"+ item+"'></td>")
        else:
            fp.write("<td>"+ item +"</td>")
    fp.write("</tr>")

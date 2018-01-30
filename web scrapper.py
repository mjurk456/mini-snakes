import requests, os, bs4
url='https://www.boredpanda.com/funny-pet-jerks/'
os.makedirs("/home/maria/Pictures/downloaded/", exist_ok=True)

while True:
    print("Downloading page %s" % url)
    res=requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    imgElement=soup.select(".image-size-full")

    for element in imgElement:
        imgUrl=element.get('src')
        print("Downloading image %s" % imgUrl)
        res=requests.get(imgUrl)
        res.raise_for_status()
        imageFile=open(os.path.join('/home/maria/Pictures/downloaded/', \
								os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    nextLink=soup.find("a", class_="pagination")
    if nextLink:
        url=nextLink.get('href')
    else:
        break
print("Done")

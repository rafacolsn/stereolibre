import xml.etree.ElementTree as ET
from scrape import datas


tree = ET.parse('stereolibre.xml')
root = tree.getroot()


# Add a title to the channel
root[1][0].text = 'Stereo Libre'

domain = "https://www.mixcloud.com"
for key, value in datas.items():
    item = ET.SubElement(root[1], 'item')
    title = ET.SubElement(item, 'title')
    link = ET.SubElement(item, 'link')
    descr = ET.SubElement(item, 'description')
    date = ET.SubElement(item, 'pubDate')
    author = ET.SubElement(item, 'author')
    guid = ET.SubElement(item, 'guid')

    title.text = key
    link.text = domain + value[0]
    descr.text = "STEREO LIBRE propose un mélange de 2 playlists confectionnées par 2 animateurs découvrant mutuellement la playlist de l’autre à chaque nouvelle émission. Le tout articulé autour d’un thème décidé à l’avance."
    date.text = value[1][1]
    author.text = "stereolibre@equinoxefm.be"
    guid.text = domain + value[0]

tree.write("stereolibre.xml", 'UTF-8')

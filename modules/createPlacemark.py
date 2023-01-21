from string import Template


def createPlacemark(id, name, founder, period, styleId, gpsE, gpsN):
    templatePoint = """
      <Placemark>
        <name>$id - $name</name>
        <description>$founder &lt;br/&gt;datowanie: $period</description>
        <styleUrl>#$styleId</styleUrl>
        <Point>
          <coordinates>$gpsE,$gpsN</coordinates>
        </Point>
      </Placemark>
    """
    template = Template(templatePoint)
    return template.substitute(
      id=id, 
      name=name, 
      founder=founder, 
      period=period, 
      styleId=styleId, 
      gpsE=gpsE, 
      gpsN=gpsN)


# print(createPlacemark('dupa', '1739111-BDBDBD', 'gpsE', 'gpsN'))

# def myfunc(**point):
#     print("I work with the follwoing people: ")
#     for people in point:
#         print (point[people])


# mydict = {'person1': "Faraz", 'person2': "Rukhshan", 'person3': "Muzammil"}

# myfunc(**mydict)


def getKMLstyleList(styleId, iconUrl):

    return [
        """<Style id="{styleId}">
            <IconStyle> <Icon> <href>{iconUrl}</href> </Icon></IconStyle>
            </Style>""".format(styleId=styleId, iconUrl=iconUrl),
    ]
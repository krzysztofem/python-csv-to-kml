def getKMLstyleList(styleId, iconUrl):

    return [
        """<Style id="{styleId}">
            <IconStyle> <Icon> <href>{iconUrl}</href> </Icon></IconStyle>
            </Style>""".format(styleId=styleId, iconUrl=iconUrl),
    ]
    # return """
    #     <Style id="icon-{iconId}-nodesc-normal">
    #         <IconStyle>
    #         <color>{color}</color>
    #         <scale>1</scale>
    #         <Icon>
    #             <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
    #         </Icon>
    #         </IconStyle>
    #         <LabelStyle>
    #         <scale>0</scale>
    #         </LabelStyle>
    #         <BalloonStyle>
    #         <text><![CDATA[<h3>$[name]</h3>]]></text>
    #         </BalloonStyle>
    #     </Style>
    #     <Style id="icon-{iconId}-nodesc-highlight">
    #         <IconStyle>
    #         <color>{color}</color>
    #         <scale>1</scale>
    #         <Icon>
    #             <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
    #         </Icon>
    #         </IconStyle>
    #         <LabelStyle>
    #         <scale>1</scale>
    #         </LabelStyle>
    #         <BalloonStyle>
    #         <text><![CDATA[<h3>$[name]</h3>]]></text>
    #         </BalloonStyle>
    #     </Style>
    #     <StyleMap id="icon-{iconId}-nodesc">
    #         <Pair>
    #         <key>normal</key>
    #         <styleUrl>#icon-{iconId}-nodesc-normal</styleUrl>
    #         </Pair>
    #         <Pair>
    #         <key>highlight</key>
    #         <styleUrl>#icon-{iconId}-nodesc-highlight</styleUrl>
    #         </Pair>
    #     </StyleMap>""".format(color=color, iconId=iconId)
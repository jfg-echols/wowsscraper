#! python3
import webbrowser
import sys
import bs4
import requests

rootSite = 'http://wiki.wargaming.net/en/World_of_Warships'
DDSite = 'http://wiki.wargaming.net/en/Ship:Destroyers'
CASite = 'http://wiki.wargaming.net/en/Ship:Cruisers'
BBSite = 'http://wiki.wargaming.net/en/Ship:Battleships'
CVSite = 'http://wiki.wargaming.net/en/Ship:Aircraft_Carriers'


#testing the root site

# rootres = requests.get(rootsite)
# rootres.raise_for_status()
# rootSoup = bs4.BeautifulSoup(rootres.text)


#get destroyer site
DDres = requests.get(DDSite)
DDres.raise_for_status()
DDsoup = bs4.BeautifulSoup(DDres.text, "html.parser")


#print japanese DD names
DDNationDivs = DDsoup.find_all("div",class_="wot-frame-1")

for nation in DDNationDivs:
    
    print('====================')
    print(nation.find("h2").text)
    print('====================')
    
    
    DDs = nation.find_all("div",class_="tleft")
    for DD in DDs:
        fulllink = 'http://wiki.wargaming.net'+(DD.find_all("a"))[1].attrs['href']
        name = (DD.find_all("a"))[1].text
    

        print('----- ' + name)
        # print(fulllink)
        thisDDpage = requests.get(fulllink)
        thisDDpage.raise_for_status()
        thisDDsoup = bs4.BeautifulSoup(thisDDpage.text, "html.parser")

        shiparray = {}

        #gets class, country, tier
        perfdiv = thisDDsoup.find('div',class_='b-performance_position')
        shiparray['shipclass'] = perfdiv.text.split(' | ')[0]
        shiparray['shipcountry'] = perfdiv.text.split(' | ')[1]
        shiparray['shiptier'] = perfdiv.text.split(' | ')[2]
        
        #gets general, armament, toobs, maneuverability, concealment
        shipstats = thisDDsoup.find_all('div',class_='gw-popup-card b-tech-nav_item__opened')
        for statgroup in shipstats:
            groupName = statgroup.find('div',class_='b-performance_title gw-popup-card_head js-tech-nav_head').text
            # print('--')
            # print(groupName)
            # print('--')
            stats = statgroup.find('div',class_='gw-popup-card_content').find_all('tr')
            for stat in stats:
               
               shiparray[stat.find_all('span')[0].text] = stat.find_all('span')[1].text
        
        
        
        
        
        
        print(shiparray)
        input("Press a key to continue...")        
        # researchprice = 
        # purchaseprice =
        # hitpoints = 
#DB data points
# ship name string
# country string
# tier int
# class string
# researchprice int
# purchaseprice int
# hitpoints int
# mbattery string
# mbatterycount string
# mrateoffire string
# mreloadtime 
# mrotationspeed
# m180degreeturntime
# mfiringrange
# mmaxdispersion
# mheshell
# mhemaxdamage
# mchanceoffire
# mheshellvelocity
# mheshellweight
# mapshell
# mapmaxdamage
# mapshellvelocity
#  mapshellweight
# torptype
# torprateoffire
# torpreload
# torprotationspeed
# torp180degreeturntime
# AAgun
# AAavgdps
# AAfiringrange
# MAxSpeed
# TurningCircleRadius
# RudderShiftTime
# SurfaceDetectability
# AirDetectability
# Battlelevels 
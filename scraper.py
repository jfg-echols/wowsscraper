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
        shipstats = thisDDsoup.find('div',class_='b-performance_border').find_all('div',class_='gw-popup-card b-tech-nav_item__opened')
        for statgroup in shipstats:
            groupName = statgroup.find('div',class_='b-performance_title gw-popup-card_head js-tech-nav_head').text
            print('--')
            print(groupName)
            print('--')
            stats = statgroup.find('div',class_='gw-popup-card_content').find_all('tr')
            
            ###GENERAL STAT GROUP

            if groupName == 'General':
                
                shipCurrency = ''
                shipCost = ''
                shipHitPoints = ''
                shipResearch = ''
                for stat in stats:
                    print('--------------')
                    ##TODO - strip whitespace from variables                    
                    if stat.find('span',class_='t-performance_left').text == 'Purchase price':
                        shipCurrency = stat.find('img')['alt']
                        shipCost = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Hit Points':
                        shipHitPoints = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Research price':
                        shipResearch = stat.find('span',class_='t-performance_right').text
                    
                if shipCost != 'promo':
                    print('Currency: '+shipCurrency)
                print('Cost: '+shipCost)
                print('HP: '+shipHitPoints)
                if shipResearch != '':
                    print('ResearchXP: '+shipResearch)
                #print(stats)
            
            ###MAIN BATTERY

            elif groupName == 'Main Battery':
                shipMainGun = ''
                shipMainGunCount = ''
                shipMainGunROF = ''
                shipMainGunReload = ''
                shipMainGunRotate = ''
                shipMainGun180 = ''
                shipMainGunRange = ''
                shipMainGunDispersion = ''
                shipMainGunHEShell = ''
                shipMainGunHEDam = ''
                shipMainGunHEFire = ''
                shipMainGunHEVel = ''
                shipMainGunHEWeight = ''
                shipMainGunAPShell = ''
                shipMainGunAPDam = ''
                shipMainGunAPVel = ''
                shipMainGunAPWeight = ''

                shipMainGun = stats[0].find('span',class_='t-performance_left').text
                shipMainGunCount = stats[0].find('span',class_='t-performance_right').text

                for stat in stats:
                    if stat.find('span',class_='t-performance_left').text == 'Rate of Fire':
                        shipMainGunROF = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Reload Time':
                        shipMainGunReload = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Rotation Speed':
                        shipMainGunRotate = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == '180 Degree Turn Time':
                        shipMainGun180 = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Firing Range':
                        shipMainGunRange = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Maximum Dispersion':
                        shipMainGunDispersion = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'HE Shell':
                        shipMainGunHEShell = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Maximum HE Shell Damage':
                        shipMainGunHEDam = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Chance of Fire on Target Caused by HE Shell':
                        shipMainGunHEFire = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Initial HE Shell Velocity':
                        shipMainGunHEVel = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'HE Shell Weight':
                        shipMainGunHEWeight = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'AP Shell':
                        shipMainGunAPShell = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Maximum AP Shell Damage':
                        shipMainGunAPDam = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'Initial AP Shell Velocity':
                        shipMainGunAPVel = stat.find('span',class_='t-performance_right').text
                    if stat.find('span',class_='t-performance_left').text == 'AP Shell Weight':
                        shipMainGunAPWeight = stat.find('span',class_='t-performance_right').text
                
                print(shipMainGun)
                print(shipMainGunCount)
                print(shipMainGunROF)
                print(shipMainGunReload)
                print(shipMainGunRotate)
                print(shipMainGun180)
                print(shipMainGunRange)
                print(shipMainGunDispersion)
                print(shipMainGunHEShell)
                print(shipMainGunHEDam)
                print(shipMainGunHEFire)
                print(shipMainGunHEVel)
                print(shipMainGunHEWeight)
                print(shipMainGunAPShell)
                print(shipMainGunAPDam)
                print(shipMainGunAPVel)
                print(shipMainGunAPWeight)
            ##TODO - Secondary Armament - multiple Secondaries

            elif groupName == 'Torpedo Tubes':
                shipTorpTube = ''
                shipTorpCount = ''
                shipTorpReload = ''
                shipTorpRorate = ''
                shipTorp180 = ''
                shipTorp = ''
                shipTorpDam = ''
                shipTorpSpeed = ''
                shipTorpRange = ''

            elif groupName == 'AA Defense':
                shipAA = ''
                shipAACount = ''
                shipAADps = ''
                shipAArange = ''

            ##TODO - multiple AA Defense
            elif groupName == 'Maneuverability':
                shipSpeed = ''
                shipTurnRadius = ''
                shipRudderShift = ''


            elif groupName == 'Concealment':
                shipSurfaceDetect = ''
                shipAirDetect = ''

        
        #     stats = statgroup.find('div',class_='gw-popup-card_content').find_all('tr')
        #     for stat in stats:
               
        #        shiparray[stat.find_all('span')[0].text] = stat.find_all('span')[1].text
        
        
        
        
        
        
        # print(shiparray)
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
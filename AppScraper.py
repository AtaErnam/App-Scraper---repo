from bs4 import BeautifulSoup as bs
import requests
import csv

Webpage = requests.get("https://play.google.com/store/apps").text
Websoup = bs(Webpage, 'lxml' )


selection = ""
while selection != "1" and selection != "2" and selection != "3":
    print("*---------------------------")
    print("[1] Word Search")
    print("[2] Genre selection")
    print("[3] Continue")

    selection = input("Please enter your selection: ")
    print("*---------------------------")

    if selection != "1" and selection != "2" and selection != "3":
        print("Invalid input!")


if selection == "1":
    Search_Word = input("Please enter the word you want to search: ")
    print("")

    Webpage = requests.get("https://play.google.com/store/search?q=" + Search_Word + "&c=apps").text
    Websoup = bs(Webpage, 'lxml' )   
    App_Cards = Websoup.find_all(class_= "ImZGtf mpg5gc")

    Webpage = requests.get("https://play.google.com/store/apps").text
    Websoup = bs(Webpage, 'lxml' )

    choice = input("Would like to pick a genre? Yes or No: ")
    print("")

    while choice != "Yes" and choice != "No":
        print("Incorrect input, please type Yes or No!")
        choice = input("Would like to pick a genre? Yes or No: ")


    if choice == "Yes":
        Genres = Websoup.find_all("li", class_= "KZnDLd")
        print(Genres)
        
        for genre in Genres:
            print("-",genre.text)
            print("")

        Genre_link = ""
        while Genre_link == "":
            g_choice = input("Please select a genre: ")
            print("")
            
            for genre in Genres:
                if g_choice == genre.text:
                    Genre_link = genre.a['href']
            
            if Genre_link == "":
                print("This genre doesn't exist!")
                print("")
        
        
elif selection == "2":
    Webpage = requests.get("https://play.google.com/store/apps").text
    Websoup = bs(Webpage, 'lxml' )

    choice = input("Would like to pick a genre? Yes or No: ")

    while choice != "Yes" and choice != "No":
        print("Incorrect input, please type Yes or No!")
        choice = input("Would like to pick a genre? Yes or No: ")
        


    if choice == "Yes":
        Genres = Websoup.find_all("li", class_= "KZnDLd")
        for genre in Genres:
            print("-",genre.text)
            print("")

        Genre_link = ""
        while Genre_link == "":
            g_choice = input("Please select a genre: ")
            print("")
            
            for genre in Genres:
                if g_choice == genre.text:
                    Genre_link = genre.a['href']
            
            if Genre_link == "":
                print("This genre doesn't exist!")
                print("")
            else:
                Webpage = requests.get("https://play.google.com" + Genre_link).text
                Websoup = bs(Webpage, 'lxml')
                App_Cards = Websoup.find_all(class_= "WHE7ib mpg5gc")
                
    else:
        App_Cards = Websoup.find_all(class_= "WHE7ib mpg5gc")
        print("")
        
elif selection == "3":
    choice = "No"
    App_Cards = Websoup.find_all("div", class_= "WHE7ib mpg5gc")


name_list = []
genre_list = []
version_list = []


def Scraper():

    App_Name = Appsoup.find("h1", attrs={"itemprop":"name"}).text

    #App_Publisher = Appsoup.find("span", class_ = "T32cc UAO9ie").text

    
    App_Info = Appsoup.find_all("span", class_ = "htlgb")

    App_Version = App_Info[6].text

    name_list.append(App_Name)
    version_list.append(App_Version)

      
    print(f"App Name: {App_Name}")
    print(f"App Genre: {App_Genre}")
    print(f"App Version: {App_Version}")
    print("")
    


for apps in App_Cards:
    App_Link = apps.find("a", href = True)
    App_Link = App_Link['href']

    Apppage = requests.get("https://play.google.com"+ App_Link).text
    Appsoup = bs(Apppage, 'lxml')


    App_Genre = Appsoup.find("a" , attrs={"itemprop":"genre"}).text

    genre_list.append(App_Genre)

    if choice == "Yes":
        if g_choice == App_Genre:
            Scraper()
    else:
        
        Scraper()
    

names = name_list
genres = genre_list
versions = version_list

with open(r'C:\Users\PC\Desktop\App Data.csv', 'w', encoding='UTF8') as f:

    writer = csv.writer(f)

    writer.writerow(names)

    writer.writerow(genres)
    
    writer.writerow(versions)







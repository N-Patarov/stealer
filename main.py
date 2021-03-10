from bs4 import BeautifulSoup
import requests
def main():
    urlinput=input("Type website url: ")
    url="https://"+urlinput+"/"
    link = requests.get(url)
    soup = BeautifulSoup(link.content,'html.parser')
    filename=input("Choose name to save your file: ")
    f= open(filename,"w+")
    f.write(BeautifulSoup.prettify(soup))
    f.close()








if __name__ == '__main__':
    main()
    
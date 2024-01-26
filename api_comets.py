import requests

def get_comets():
    global count
    print("::: COMETS INFORMATION :::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try:
        #Request to API
        response = requests.get(url)
        response.raise_for_status()       
        data = response.json()
        count=0
        
        print("::: SOLAR SYSTEM MENÚ :::")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Comets")
        opt = int(input("Choose an option: "))
        if opt == 1:
            body_type = "Planet"
        elif opt == 2:
            body_type = "Moon"
        elif opt == 3:
            body_type = "Star"
        elif opt == 4:
            body_type = "Asteroid"
        elif opt == 5:
            body_type = "Comet"
        else:
            print("::: INVALID OPTION :::")



        total = int(input("Cantidad de datos a mostrar: "))
        #planet = input("Digite el planeta a buscar: ")
        #Print all comets names
        for comet in data ["bodies"]:
            #if comet ["englishName"] == planet:
            #if comet["isPlanet"] == True:
            if comet ["bodyType"] == body_type:

                print("English Name: ", comet["englishName"])   
                #print("Moons: ", comet["moons"])  
                print("Gravity: ", comet["gravity"])  
                print("Is planet?: ", comet["isPlanet"])  
                print("Body Type: ", comet["bodyType"])  

                print("\n")
            
                count = count + 1 
            if count == total:
                break
        print(count)
 

    except requests.exceptions.RequestException as e: 
        print(f"API ERROR {e}")


#Call function
get_comets()

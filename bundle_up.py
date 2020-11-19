from tkinter import *  #Import all packages from tkinter
import tkinter.font #Import tkinter font library
from PIL import ImageTk,Image #Import pillow package for diplaying images
import requests #import request 
import json# JSON  library to 
import key #Import key class  with API key 
import tkinter.messagebox
import webbrowser 


def get_weather():#Create Weather function


     my_key = key.Key()#Create an instance of the key calss
     api_key = my_key.get_key() #Set API key from OpenWeatherMap.com and is stored in the key class
     base_url = "http://api.openweathermap.org/data/2.5/weather?" #Set variable to store URL
     city_name = self.city_entry.get()# Get city name from city entry box
     complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial" #Set variable to store complete url address and modified output to be in Fahrenheit
     response = requests.get(complete_url) #Get method returns a json object (JavaScript Object Notation)
     x = response.json() #Convert the weather object into python data
     
     if  x["cod"] != "404": #Check to  see if city was found or not
             y = x["main"]   # store the value of "main" key in variable y
             current_temperature = y["temp"] # store the value corresponding to the "temp" key of y
             current_pressure = y["pressure"] # store the value corresponding to the "pressure" key of y
             current_humidity = y["humidity"] # store the value corresponding to the "humidity" key of y
                            
             z = x["weather"] # store the value of "weather" key in variable z
             
             c = x["coord"]  #Holding the geolocation, longitude and latitude  for future map embedding. 
             lon = c["lon"]
             lat= c["lat"]
             
             weather_description = z[0]["description"] # store the value corresponding to the "description" key # at the 0th index of z
             
             self.temp_field.insert(30, str(current_temperature) + " Fahrenheit") #Insert the Results into text entry fields
             self.atm_field.insert(30, str(current_pressure) + " hPa")
             self.humidity_field.insert(30,str(current_humidity) + " %")
             self.condition_field.insert(30, str(weather_description) )
             self.recommended_clothing.insert(30, rec_clothing(current_temperature, weather_description))
     else: #If 404 (city not found)
             tkinter.messagebox.showerror("Error", "City Found\n" #Display message of 404
                                                             "Please eanter a valid city.")
             self.city_entry.delete(0, END) #Clear the city field for new entry
             
def rec_clothing(current_temperature, weather_description):#Get recommended clothing based on temperature and conditions

    while weather_description != "rain":
            if current_temperature >= 95:
                return str("Break out the swim suit and head to the beach!")
            if current_temperature >= 85:
                return str("Shorts, t-shirt and sandels")
            if current_temperature >= 75:
                return str("Shorts and a t-shirt")
            if current_temperature >= 65:
                return str("Shorts, t-shirt and light jacket.")
            if current_temperature >= 55:
                return str("Jeans, sweatshirt and or jacket. ")
            if current_temperature >= 45:
                 return str("Jeans, fall coat and warm socks. ")
            if current_temperature >= 35:
                return str("Jeans, winter jacket and warm boots.")
            if current_temperature >= 25:
                 return str("Winter jacket, mittens and warm boots. ")
            if current_temperature >= 10:
                return str("Break out the long underwear\n"" and all your winter gear!")
            if current_temperature >= -10:
                return str("Too cold to go outside!")
    while weather_description == "rain": #If the conditions are rain recommend an umbrella or 
        return str("Use an umbrella or a rain Coat. ")
    
def display_map():

    webbrowser.open_new(r"https://www.wunderground.com/wundermap") #Create method for hyper link to weather map
    
def clear_fields() : #Set function for clearing fields
    self.city_entry.delete(0, END) 
    self.temp_field.delete(0, END) 
    self.atm_field.delete(0, END) 
    self.humidity_field.delete(0, END) 
    self.condition_field.delete(0, END)
    self.recommended_clothing.delete(0,END)

	
    self.city_entry.focus_set() # set focus on the city_field entry box 
	
if __name__=="__main__":   #Define the initializer for the window
        
        self = tkinter.Tk() #Create the main window
        myfont = tkinter.font.Font(family='Awesome', size=16, weight='bold')
        background_img = ImageTk.PhotoImage(Image.open("emotion-motion-trees-foggy-wallpaper.jpg"))#Set the background image from file
        bg_label =Label( image=background_img)
        bg_label.place(x=0, y=0,relwidth=1, relheight=1)
        self.title("Bundle Up") #Add tiltle to window
        self.iconbitmap('weather.ico')# Added a custom icon
        
     
        #This code will open the program in the center of the screen
        app_width = 1000   #Set height and 
        app_height = 800 #width of the progarm
        screen_width  = self.winfo_screenwidth() #Get the size of the screen width
        screen_height = self.winfo_screenheight()#and height
        x =(screen_width / 2) - (app_width / 2)#Get the x coord of the width
        y = (screen_height / 2) - (app_height /2)    #Get the y coord of the height
        self.geometry( f"{app_width}x{app_height}+{int(x)}+{int(y)}")#Set the size of the window and center on screen
        
        self.head_label = tkinter.Label(self, text= "Get current weather conditions for any city and recommended clothing.", font= myfont, fg= 'white', bg= "#4F5B66")
        self.promt_label = tkinter.Label(self,  text= "Enter a city: ", font= myfont, fg= 'white', bg= "#4F5B66") #Create label for city entry
        self.city_entry = tkinter.Entry(self,  font= myfont, fg= 'white', bg= "#65737e") #create entry  field for city name
        
        self.head_label.grid(row=0, column=0, columnspan=2, sticky ="NSEW", padx=10, pady= 5)
        self.promt_label.grid(row=1, column=0,  sticky ="NSEW", padx=10, pady= 5) #Set label and entry for city name with grid system
        self.city_entry.grid(row=1, column=1, sticky ="NSEW", padx=10, pady=5)#Set entry for city name with grid system

       
        self.label2 = tkinter.Label(self, text= "Temperature:" , anchor="center", font=myfont ,fg= 'white',bg= "#4F5B66")#Set label for temperatur
        self.label3 = tkinter.Label(self, text= "Atmospheric Pressure:",anchor="center",   font= myfont, fg= 'white',bg= "#4F5B66")#Set label for Atmospheric pressure
        self.label4 = tkinter.Label(self, text= "Humidity:", anchor="center",  font= myfont ,fg= 'white', bg= "#4F5B66")#Set label for Humidity
        self.label5 = tkinter.Label(self, text= "Current Conditions:", anchor="center",  font= myfont,fg= 'white', bg= "#4F5B66")#Set label for CXurrent CFonditions
        self.label6 = tkinter.Label(self, text= "Recommended Clothing:", anchor="center",  font= myfont ,fg= 'white', bg= "#4F5B66")#Set label for Recommended Clothing


      #Set Labels in window relative to grid postion. 
        self.label2.grid(row = 3, column = 0,  sticky ="NSEW", padx=10, pady= 5)  
        self.label3.grid(row = 4, column = 0, sticky ="NSEW", padx=10, pady= 5)  
        self.label4.grid(row = 5, column = 0, sticky ="NSEW", padx=10, pady= 5)  
        self.label5.grid(row = 6, column = 0, sticky ="NSEW", padx=10, pady= 5)
        self.label6.grid(row = 7, column = 0, sticky ="NSEW", padx=10, pady= 5)


        
        self.temp_field = tkinter.Entry(self, font= myfont, fg= 'white', bg= "#65737e") 
        self.atm_field = tkinter.Entry(self, font= myfont, fg= 'white', bg= "#65737e") 
        self.humidity_field = tkinter.Entry(self, font= myfont, fg= 'white', bg= "#65737e") 
        self.condition_field = tkinter.Entry(self, font= myfont, fg= 'white', bg= "#65737e")
        self.recommended_clothing =  tkinter.Entry(self, font=myfont, fg= 'white', bg= "#65737e")
                                    
      
        self.temp_field.grid(row = 3, column = 1, sticky ="NSEW", padx=10, pady= 5) 
        self.atm_field.grid(row = 4, column = 1, sticky ="NSEW", padx=10, pady= 5) 
        self.humidity_field.grid(row = 5, column = 1,sticky ="NSEW", padx=10, pady= 5) 
        self.condition_field.grid(row = 6, column = 1, sticky ="NSEW", padx=10, pady= 5)
        self.recommended_clothing.grid(row = 7, column = 1, sticky ="NSEW", padx=10, pady= 5)

        self.submit_button = tkinter.Button(self, text="Submit",  anchor="center", font= myfont , command = get_weather,fg= '#ffffff', bg= "#99aab5")#Create label for Submit button
        self.clear_button = tkinter.Button( text= "Clear" , anchor="center",  font= myfont, command= clear_fields, fg= '#ffffff', bg= "#99aab5")#Create label for clear button
        self.link_button =tkinter.Button(text= "Weather Map", anchor="center",  font= myfont, command= display_map, fg= '#ffffff', bg= "#99aab5")
        
        self.submit_button.grid(row =2 , column = 1, sticky ="NEW", padx=10, pady=5) #Set  buttons in window to relative postion
        self.clear_button.grid(row = 8, column = 1 , sticky ="NEW", padx=10, pady= 5)
        self.link_button.grid(row = 8, column = 0 , sticky ="NEW", padx=10, pady= 5)                      


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2 ,weight=1)
       
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,weight=1)
        self.grid_rowconfigure(9,weight=1)

            
        tkinter.mainloop()


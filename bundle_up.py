from tkinter import *  #results in importing everything that exists in tkinter module
from PIL import ImageTk,Image #Import pillow package for diplaying images
import requests,json,key, webbrowser,tkinter.messagebox,tkinter.font   #import modules



#Create Weather function
def get_weather():

     #Create an instance of the key class
     #Set API key from OpenWeatherMap.com and is stored in the key class
     my_key = key.Key()
     api_key = my_key.get_key()
     
     #Set variable to store URL
     # Get city name from city entry box
     #Set variable to store complete url address and modified output to be in Fahrenheit
     #Convert the weather object into python data
   
     base_url = "http://api.openweathermap.org/data/2.5/weather?" 
     city_name = self.city_entry.get()
     complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial" 
     response = requests.get(complete_url) 
     x = response.json()

     
     #Check to  see if city was found or not
     # store the value of "main" key in variable y
     if  x["cod"] != "404": 
          
             y = x["main"]  
             
            # store the value corresponding to the "temp" key of y
            # store the value corresponding to the "pressure" key of y
             # store the value corresponding to the "humidity" key of y
             current_temperature = y["temp"] 
             current_pressure = y["pressure"] 
             current_humidity = y["humidity"] 
             
            # store the value of "weather" key in variable z                
             z = x["weather"] 
             #Holding the geolocation, longitude and latitude  for future map embedding. 
             c = x["coord"]  
             lon = c["lon"]
             lat= c["lat"]
             # store the value corresponding to the "description" key # at the 0th index of z
             weather_description = z[0]["description"] 
              #Insert the Results into text entry fields
             self.temp_field.insert(30, str(current_temperature) + " Fahrenheit")
             self.atm_field.insert(30, str(current_pressure) + " hPa")
             self.humidity_field.insert(30,str(current_humidity) + " %")
             self.condition_field.insert(30, str(weather_description) )
             self.recommended_clothing.insert(30, rec_clothing(current_temperature, weather_description))

             #Display message of 404, If (city not found)
     else: 
             tkinter.messagebox.showerror("Error", "City Found\n" 
                                                             "Please eanter a valid city.")
              #Clear the city field for new entry
             self.city_entry.delete(0, END)

             #Get recommended clothing based on temperature and conditions
             #If the conditions are rain recommend an umbrella or raincoat
def rec_clothing(current_temperature, weather_description):

    while weather_description != "rain":
            if current_temperature >= 95:
                return str("Break out the swim suit and head to the beach")
            if current_temperature >= 85:
                return str("Shorts, t-shirt and sandels")
            if current_temperature >= 75:
                return str("Shorts and a t-shirt")
            if current_temperature >= 65:
                return str("Shorts, t-shirt and light jacket")
            if current_temperature >= 55:
                return str("Jeans, sweatshirt and or jacket")
            if current_temperature >= 45:
                 return str("Jeans, fall coat and scarf")
            if current_temperature >= 35:
                return str("Jeans, winter coat and warm boots")
            if current_temperature >= 25:
                 return str("Winter coat, mittens and a knit hat")
            if current_temperature >= 15:
                return str("Winter coat, mittens, knit hat and boots")
            if current_temperature >= 5:
                return str("Long underwear and all your winter gear")
            if current_temperature >= -10:
                return str("Too cold to go outside!")
    while weather_description == "rain": 
        return str("Use an umbrella or a rain coat. ")

    
            #Create method for hyper link to weather map
def display_map():

    webbrowser.open_new(r"https://www.wunderground.com/wundermap")

    
        #Create function for clearing fields
def clear_fields() : 
    self.city_entry.delete(0, END) 
    self.temp_field.delete(0, END) 
    self.atm_field.delete(0, END) 
    self.humidity_field.delete(0, END) 
    self.condition_field.delete(0, END)
    self.recommended_clothing.delete(0,END)	
    self.city_entry.focus_set() 

         # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/	
if __name__=="__main__":  

        #Create the main window
        #Set the background image from file
        #Add tiltle to window
        # Added a custom icon
        self = tkinter.Tk() 
        myfont = tkinter.font.Font(family='Awesome', size=16, weight='bold')
        background_img = ImageTk.PhotoImage(Image.open("emotion-motion-trees-foggy-wallpaper.jpg"))
        bg_label =Label( image=background_img)
        bg_label.place(x=0, y=0,relwidth=1, relheight=1)
        self.title("Bundle Up") 
        self.iconbitmap('weather.ico')
        
        
     
        #This code will open the program in the center of the  monitor screen        
        #Set height andwidth of the progarm
        #Get the size of the screen width and height
        #Get the x coord of the width
        #Get the y coord of the height
        #Set the size of the window and center on screen
        app_width = 850    
        app_height = 500
        screen_width  = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight()
        x =(screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height /2)    
        self.geometry( f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        
        #Create frame for main window
        #Pack the frame
        mainframe = tkinter.Frame(self, width=1000, height=800, bg="#65737e")
        mainframe.pack(pady= 10, anchor= 'center', expand=True)
    
        
        #Create label for header
        #Create label for city entry
         #create entry  field for city name
        self.head_label = tkinter.Label( mainframe, text= "Get current weather conditions for any city and recommended clothing", font= myfont, fg= 'white', bg= "#65737e")
        self.promt_label = tkinter.Label( mainframe,  text= "Enter a city: ", font= myfont, fg= 'white', bg= "#65737e") 
        self.city_entry = tkinter.Entry( mainframe,  font= myfont, fg= 'white', bg= "#65737e")

        #Set  the header in grid position
        #Set label for city name with grid system
        #Set entry for city name with grid system
        self.head_label.grid(row=0, column=0, columnspan=2, sticky ="NSEW", padx=10, pady= 5)
        self.promt_label.grid(row=1, column=0,  sticky ="NSEW", padx=10, pady= 5) 
        self.city_entry.grid(row=1, column=1, sticky ="NSEW", padx=10, pady=5)

        #Set label for temperature
        #Set label for Atmospheric pressure
        #Set label for Humidity
        #Set label for Current Conditions
       #Set label for Recommended Clothing
        self.label2 = Label( mainframe, text= "Temperature:" , anchor="center", font=myfont ,fg= 'white',bg= "#65737e")
        self.label3 = Label( mainframe, text= "Atmospheric Pressure:",anchor="center",   font= myfont, fg= 'white',bg= "#65737e")
        self.label4 = Label( mainframe, text= "Humidity:", anchor="center",  font= myfont ,fg= 'white', bg= "#65737e")
        self.label5 = Label( mainframe, text= "Current Conditions:", anchor="center",  font= myfont,fg= 'white', bg= "#65737e")
        self.label6 = Label( mainframe, text= "Recommended Clothing:", anchor="center",  font= myfont ,fg= 'white', bg= "#65737e")


      #Set Labels in window relative to grid postion. 
        self.label2.grid(row = 3, column = 0,  sticky ="NSEW", padx=10, pady= 5)  
        self.label3.grid(row = 4, column = 0, sticky ="NSEW", padx=10, pady= 5)  
        self.label4.grid(row = 5, column = 0, sticky ="NSEW", padx=10, pady= 5)  
        self.label5.grid(row = 6, column = 0, sticky ="NSEW", padx=10, pady= 5)
        self.label6.grid(row = 7, column = 0, sticky ="NSEW", padx=10, pady= 5)


        #Create the entry boxes for results
        self.temp_field = Entry( mainframe, font= myfont, fg= 'white', bg= "#65737e") 
        self.atm_field = Entry( mainframe, font= myfont, fg= 'white', bg= "#65737e") 
        self.humidity_field = Entry( mainframe, font= myfont, fg= 'white', bg= "#65737e") 
        self.condition_field = Entry( mainframe, font= myfont, fg= 'white', bg= "#65737e")
        self.recommended_clothing =  Entry( mainframe, font=myfont, fg= 'white', bg= "#65737e")
                                    
        #Set the entry boxes relative  to grid positions
        self.temp_field.grid(row = 3, column = 1, sticky ="NSEW", padx=10, pady= 5) 
        self.atm_field.grid(row = 4, column = 1, sticky ="NSEW", padx=10, pady= 5) 
        self.humidity_field.grid(row = 5, column = 1,sticky ="NSEW", padx=10, pady= 5) 
        self.condition_field.grid(row = 6, column = 1, sticky ="NSEW", padx=10, pady= 5)
        self.recommended_clothing.grid(row = 7, column = 1, sticky ="NSEW", padx=10, pady= 5)
        
        #Create label for Submit button
        #Create label for clear button
        #Create button to link  map
        self.submit_button = Button( mainframe, text="Submit",  anchor="center", font= myfont , command = get_weather,fg= '#ffffff', bg= "#99aab5")
        self.clear_button = Button( mainframe, text= "Clear" , anchor="center",  font= myfont, command= clear_fields, fg= '#ffffff', bg= "#99aab5")
        self.link_button = Button( mainframe,text= "Weather Map", anchor="center",  font= myfont, command= display_map, fg= '#ffffff', bg= "#99aab5")
        
        #Set  buttons in window to relative postion
        self.submit_button.grid(row =2 , column = 1, sticky ="NEW", padx=10, pady=5) 
        self.clear_button.grid(row = 8, column = 1 , sticky ="NEW", padx=10, pady= 5)
        self.link_button.grid(row = 8, column = 0 , sticky ="NEW", padx=10, pady= 5)                      
      
            
        mainloop()


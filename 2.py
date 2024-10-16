from pywebio.input import *
from pywebio.output import *
import time

# Variables:
# Slogan - Slogan where ever the slogan appears
slogan = "It's good karma to use Carma"
# Name - User's Name
Name = ""
# Password - The user's password to the account
password = ""
# LocationChoice - The user's choice of location
LocationChoice = ""
# ChosenType - The user's chosen type of vehicle
ChosenType = ""
# ChosenCar - The user's choice of car in that set of category
ChosenCar = ""
# Credentials - Stores multiple variables, like email and phone number
Credentials = {}
# LoginGroup - Stores muiltiple variables
LoginGroup = {}
# DateData - The user's choice of start and end date for car hire
DateData = ""
# BasePrice - different base prices depending on the user's choice of vehicle type
BasePrice = ""

# function that clears the page and sends the user back to the login screen
def BackToMainPage():
    clear()
    main()

# Login Screen
@use_scope("Main_scope", clear = True )
def main():
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:150px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>")
    put_html(f"<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:300; color: #a6a6a6;'>{slogan}</p></div>")
    put_html("<div style='height:100px;'></div>")
    put_row([
        put_text(""),
        put_column([
            put_button("Sign in using Email", onclick=login),
            put_button("Sign in using Google", onclick=lambda: None),
            put_button("Login using example (skip sign up)", onclick=loginExample),
        ]),
    ], size='40% 50%'),
    put_column([
        put_html('<hr>').style("border: none; height: 1px; background-color: black;"),
        put_row([
            put_text(""),
            put_button("Sign up using Email", onclick=SignUp),
        ], size='40% 50%')
    ])

    put_html('<div style="height:500px;"></div>')

# Top banner for any login page
@use_scope('Main_scope', clear=True )
def topSignIn():
    clear()
    put_row([
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>"),
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'>Sign in</p></div>"),
        put_row([
            put_text(""),
            put_button("Back", onclick=BackToMainPage),
        ])
    ])

# Top banner for any signup page
@use_scope('Main_scope', clear=True )
def topSignUp():
    clear()
    put_row([
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>"),
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'>Create an account</p></div>"),
        put_row([
            put_text(""),
            put_button("Back", onclick=BackToMainPage),
        ])
    ])

# Top banner with no back button
@use_scope('Main_scope', clear=True )
def topNoButton():
    clear()
    put_row([
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>"),
    ])
    put_html("<div style='height:100px;'></div>")


# Top banner for any page for booking cars
@use_scope('Main_scope', clear=True )
def BookingTop():
    clear()
    put_row([
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>"),
        put_text(""),
        put_row([
            put_text(""),
            put_button("Back", onclick=ChooseCar()),
        ])
    ])

# user enters name in this page
@use_scope('Main_scope', clear=True )
def SignUp():
    global Name
    Name = None
    topSignUp()
    Name = input("What's your name?", type=TEXT, required=True)
    SignUpEmail()

# Sign Up email page
@use_scope('Main_scope', clear=True )
def SignUpEmail():
    global Credentials
    Credentials = {}
    topSignUp()
    Credentials = input_group("", [
        input('Input your email', name='Email', required=True),
        input('Input your phone number', name='PhoneNumber', type=NUMBER, required=True)
    ])
    print(Credentials)
    print("email")
    print(Credentials['Email'])
    print("#")
    print(Credentials['PhoneNumber'])
    SignUpPassword()

# checks the length of the password, if under 8 too short, if over 32 too long
def passwordcheck(password):
    if len(password) < 8:
        return "Password must be 8 or more characters!"
    if len(password) > 32:
        return "Password is too long!"

# page where the user can sign up
@use_scope('Main_scope', clear=True )
def SignUpPassword():
    global password
    password = None
    topSignUp()
    password = input('Input your password', type=PASSWORD, required=True, validate=passwordcheck)
    print(f" password: {password}")
    birthdate()

# checks the age of the user to see if they are too old or too young
def check_age(age):
    if age < 18:
        return 'You must be aged 18 or over to register!'
    elif age > 130:
        return 'You are to old to register!'

# checks the age of the user
@use_scope('Main_scope', clear=True )
def birthdate():
    global DOB
    DOB = None
    topSignUp()
    DOB = input("What's your age?", type=NUMBER, required=True, validate=check_age)
    LivingLocation()

# Living location of the user
@use_scope('Main_scope', clear=True )
def LivingLocation():
    global Location
    Location = None
    topSignUp()
    Location = input("Where do you live?", type=TEXT, required=True)
    ID()

# Page where the user has to submit an image of the ID
@use_scope('Main_scope', clear=True )
def ID():
    global ID
    ID = None
    topSignUp()
    ID = file_upload("Please upload a picture of your ID", accept="image/*", required=True)
    CreditCard()

# checks the CVV and card number of the users card info
def CheckCreditcardInfo(Number):
    if len(str(Number['CardNumber'])) != 12:
        return("CardNumber", "Card number is incorrect!")
    if len(str(Number['CVV'])) < 3 or len(str(Number['CVV'])) > 4:
        return("CVV", "CVV is incorrect!")

# Credit and Debit card info that the user can input
def CreditCard():
    global CreditCardInfo
    CreditCardInfo = input_group("test", [
    input("Card Number", name="CardNumber", type=NUMBER, required=True),
    input("Expiry Date", name="EXPDate", type=DATE, required=True),
    input("CVV", name="CVV", type=NUMBER, required=True)
    ], validate=CheckCreditcardInfo)
    TOS()

# Checks if TOS box is checked before making account
def CheckTOS(checked):
    if not checked:
        return "You must accept the terms of services to register!"


# Checks for TOS and newsletters
@use_scope('Main_scope', clear=True )
def TOS():
    global TOSGroup
    TOSGroup = None
    topSignUp()
    TOSGroup = input_group('Accept Terms and Services', [
        checkbox(options=['I accept regular newsletters and updates via email'], name="NEWS"),
        checkbox(options=['I agree to terms and conditions'], name="TOS", validate=CheckTOS),
    ])
    main()

# Checks the login info inputted to the info that the user created when signing up
@use_scope('Main_scope', clear=True )
def CheckLoginInfo(Creds):
    global password
    email = str(Credentials['Email']).lower()
    if Creds['email'].lower() != email or Creds['password'] != password:
        return('password', 'Incorrect email or password')


#Login page
@use_scope('Main_scope', clear=True )
def login():
    clear()
    topSignIn()
    input_group("Login", [
        input("Email", name='email', type="text", required=True),
        input("Password", name='password', type=PASSWORD, required=True)
    ], validate=CheckLoginInfo)
    clear()
    topNoButton()
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Login Successful! </p></div>")
    put_html("<div style='height:2000px;'></div>")
    time.sleep(2)
    ChooseCar()

# Login page with an example login
@use_scope('Main_scope', clear=True )
def loginExample():
    global password
    clear()
    topSignIn()
    Credentials['Email'] = "Test@Test.Test"
    password = "ExamplePassword"
    put_text("Email: Test@Test.Test")
    put_text("Password: ExamplePassword")
    input_group("Login", [
        input("Email", name='email', type="text", required=True),
        input("Password", name='password', type=PASSWORD, required=True)
    ], validate=CheckLoginInfo)
    clear()
    topNoButton()
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Login Successful! </p></div>")
    put_html("<div style='height:2000px;'></div>")
    time.sleep(2)
    ChooseCar()

# Book Car page
@use_scope('Main_scope', clear=True )
def ChooseCar():
    clear()
    topNoButton()
    put_row([
        put_text(""),
        put_column([
            put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Book now</p></div>"),
            put_html('<div style="height:50px;"></div>'),
            put_row([
                put_text(""),
                put_button("Book a car", onclick=ChoosePlace),
            ], size='32.5% 60%'),
        ]),
        put_text(""),
    ])
    put_html('<hr>').style("border: none; height: 1px; background-color: black;")
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/cars/VAUX_INSI_2014.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Cars </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/vans/SEAT_ALHAMBRA_2013.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> People Carriers </p></div>")])])
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/suvs/VOLV_XC60_2014.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> SUVs </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/vans/renault-kango-logo.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Vans </p></div>")])])
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/cars/MERC_ECLA_2018.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Luxury </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/ecom/utilitarian/common/exotics/car-thumbnails/Audi-E-TRON-55_HERO-THUMBNAIL_2048x1360.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Electric </p></div>")])])


# Top banner for any page for booking cars
@use_scope('Main_scope', clear=True )
def BookingTop():
    clear()
    put_row([
        put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> <span style='color: #007bff'>Car</span><span style='color: #296bb2'>ma</span></p></div>"),
        put_text(""),
        put_row([
            put_text(""),
            put_button("Back", onclick=ChooseCar),
        ])
    ])

# User chooses location in this page
@use_scope('Main_scope', clear=True )
def ChoosePlace():
    global LocationChoice
    clear()
    BookingTop()
    put_html("<div style='height:50px;'></div>")
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Choose a pickup location </p></div>")
    options = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5', 'Location 6', 'Location 7', 'Location 8', 'Location 9']
    LocationChoice = select("Please choose a location:", options)
    print(LocationChoice)
    DateChoice()

# start and end date of the hiring
@use_scope('Main_scope', clear=True )
def DateChoice():
    global DateData
    clear()
    BookingTop()
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Select hiring dates </p></div>")
    DateData = input_group("", [input('Select your start hiring date', name='StartHire', type=DATETIME, required=True), input('Select your end hiring date', name='EndHire', type=DATETIME, required=True)])
    print(DateData)
    UserPicksCar()

# user chooses a specific type of vehicle
@use_scope('Main_scope', clear=True )
def UserPicksCar():
    global ChosenType
    clear()
    BookingTop()
    TypeChoices = ['Cars', 'People Carriers', 'SUVs', 'Vans', 'Luxury', 'Electric']
    put_html('<hr>').style("border: none; height: 1px; background-color: black;")
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/cars/VAUX_INSI_2014.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Cars </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/vans/SEAT_ALHAMBRA_2013.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> People Carriers </p></div>")])])
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/suvs/VOLV_XC60_2014.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> SUVs </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/vans/renault-kango-logo.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Vans </p></div>")])])
    put_row([put_column([put_image("https://www.enterprise.co.uk/content/dam/global-vehicle-images/cars/MERC_ECLA_2018.png"), put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Luxury </p></div>")]),put_text(""), put_column([put_image("https://www.enterprise.co.uk/content/dam/ecom/utilitarian/common/exotics/car-thumbnails/Audi-E-TRON-55_HERO-THUMBNAIL_2048x1360.png"),put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700;'> Electric </p></div>")])])
    ChosenType = select("Please choose a vehicle:", TypeChoices)
    print(ChosenType)
    ChoiceAvailability()

# checks if there is any available car, location and cars unavailable are random just for unavailable page
def ChoiceAvailability():
    global BasePrice
    LocationUnavailable = ['Location 1', 'Location 3', 'Location 4', 'Location 8', 'Location 9']
    CarUnavailable = ['Vans', 'Luxury']
    global ChosenType
    if LocationChoice in LocationUnavailable:
        NoCarsAvailable()
    elif ChosenType in CarUnavailable:
        UnavailableCar()
    elif ChosenType == 'Cars':
        BasePrice = 14
        CarsPage()
    elif ChosenType == 'People Carriers':
        BasePrice = 35
        PCarrierPage()
    elif ChosenType == 'SUVs':
        BasePrice = 27
        VansPage()
    elif ChosenType == 'Electric':
        BasePrice = 18
        ElectricPage()
    else:
        NoCarsAvailable()

# No cars available page
def NoCarsAvailable():
    clear()
    BookingTop()
    put_html("<div style='height:100px;'></div>")
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> No vehicles available for this location. </p></div>")

# Unavailable car page
def UnavailableCar():
    clear()
    BookingTop()
    put_html("<div style='height:100px;'></div>")
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> This vehicle type is unavailable. </p></div>")

# Next 4 pages are choices for the user for each specific category
def CarsPage():
    global ChosenCar
    clear()
    BookingTop()
    CarChoices = ['Ford Focus', 'Vauxhall Insignia', 'Honda Civic', 'Vauxhall Corsa', 'Skoda Octavia']
    ChosenCar = select("Please choose a vehicle:", CarChoices)
    ConfirmPayment()

def PCarrierPage():
    global ChosenCar
    clear()
    BookingTop()
    CarChoices = ['Ford Galaxy', 'Volkswagen Sharan', 'Ford C-Max', 'Renault Scenic', 'Peugeot Rifter']
    ChosenCar = select("Please choose a vehicle:", CarChoices)
    ConfirmPayment()

def VansPage():
    global ChosenCar
    clear()
    BookingTop()
    CarChoices = ['Renault Kangoo ', 'Ford Transit', 'Vauxhall Combo', 'Renault Trafic', 'Ford Transit Connect']
    ChosenCar = select("Please choose a vehicle:", CarChoices)
    ConfirmPayment()

def ElectricPage():
    global ChosenCar
    clear()
    BookingTop()
    CarChoices = ['Toyota Prius', 'Tesla Model 3', 'Nissan Leaf', 'Renault Zoe', 'Mini Electric']
    ChosenCar = select("Please choose a vehicle:", CarChoices)
    ConfirmPayment()

# requests the user to confirm the payment
def ConfirmPayment():
    DateStart = str((DateData['StartHire'].replace("-", " ")).replace("T", " "))
    DateEnd = str((DateData['EndHire'].replace("-", " ")).replace("T", " "))
    clear()
    BookingTop()
    put_html("<div style='height:100px;'></div>")
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Confirm Payment. </p></div>")
    put_html(f"<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700; color: #757474;'> Hiring {ChosenCar}, at {LocationChoice} on {DateStart} and will end on {DateEnd}</P></DIV>")
    put_html("<div style='height:50px;'></div>")
    put_html(f"<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> £{BasePrice}/Per day </P></DIV>")
    put_row([
        put_text(""),
        put_button("Confirm Payment", onclick=PaymentFinalised),
    ], size='41% 60%')

# finalises the payment
def PaymentFinalised():
    DateStart = str((DateData['StartHire'].replace("-", " ")).replace("T", " "))
    DateEnd = str((DateData['EndHire'].replace("-", " ")).replace("T", " "))
    clear()
    BookingTop()
    put_html("<div style='height:100px;'></div>")
    put_html("<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:30px; font-weight:700;'> Payment Confirmed. </p></div>")
    put_html(f"<div style='display: flex; width: 100%; justify-content: center; margin: 0; padding: 0;'><p style='font-size:15px; font-weight:700; color: #757474;'> Hiring {ChosenCar}, at {LocationChoice} on {DateStart} and will end on {DateEnd}</P></DIV>")

main()


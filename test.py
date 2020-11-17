def weather():
    # create OWM object
    API_key = '3ca51794f7789141f0525a05d80a43b9'
    owm = OWM(API_key)

    theCity = "Seattle"
    theState = "WA"
    weatherCityState = theCity + ", " + theState
    weatherLocation = theCity + ",US"

    # get currently observed weather for Seattle, WA, US
    obs = owm.weather_at_place(weatherLocation)

    # get weather object for current Seattle weather
    w = obs.get_weather()

    # get current weather status and temperature in fahrenheit
    currStatus = w.get_detailed_status()
    tempF = w.get_temperature('fahrenheit')["temp"]

    # query the daily forcast for Seattle, WA, US, for the next 5 days
    fc = owm.daily_forecast('Seattle,US', limit=5)

    # get a forcaster object
    f = fc.get_forecast()

    return render_template('templateWeather.html', theLocation=weatherCityState, currStatus=currStatus, theTemp=tempF, forecast=f,
                           title="Weather", arrow=arrow)
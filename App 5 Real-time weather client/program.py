import collections
import requests

Location = collections.namedtuple("Location", "city state country")
Weather = collections.namedtuple("Weather", "location units temp condition")


def main():

    # Show the header
    show_header()
    # Get the location request
    location_text = input("Where do you want the weather report (e.g. Portland, US)")
    # Convert plaintext over to data we can use
    loc = convert_plaintext_location(location_text)
    # Get report from the API
    data = call_weather_api(loc)
    # Report the weather
    print("Hello from weather main!")


def call_weather_api(loc):
    # &state=OR
    url = f"https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=imperial"
    if loc.state:
        url += f"&state={loc.state}"
    # print(f"Would call {url}")
    resp = requests.get(url)
    if resp.status_code in {400, 404, 500}:
        print(f"Error: {resp.text}")
        return None
    data = resp.json()
    print(data)

    temp = data.get("forecast").get("temp")
    w = data.get("weather")
    condition=f"{w.get('category')}:{w.get('description').capitalize()}."

    weather = Weather(loc, "imperial", temp, condition)
    print(weather)
    return weather


def convert_plaintext_location(location_text):
    if not location_text or not location_text.strip():
        return None
    location_text = location_text.lower().strip()
    parts = location_text.split(",")
    city = ""
    state = ""
    country = "us"
    if len(parts) == 1:
        city = parts[0].strip()
        country = "us"
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()

        country = parts[2].strip()
    else:
        return None
    return Location(city, state, country)


def show_header():
    print("------------------------------------------------")
    print("               WEATHER CLIENT                   ")
    print("------------------------------------------------")
    print()


if __name__ == "__main__":
    main()

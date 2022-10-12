import requests


def main():
    data = """
<REQUEST>
    <LOGIN authenticationkey='""" + auth_key+"""' />
    <QUERY objecttype="TrafficFlow" schemaversion="1.4">
    <FILTER>
        <AND>
            <EQ name="CountyNo" value="1" />
        </AND>
        <OR>
            <EQ name="VehicleType" value="trailer" />
        </OR>
    </FILTER>
    </QUERY>
</REQUEST>
"""
    result = requests.post(
        "https://api.trafikinfo.trafikverket.se/v1/data.json", data=data)
    print(result.json())


def read_api_key():
    with open("src/apikey.txt") as f:
        auth_key = f.readline()
        return auth_key


if (__name__ == "__main__"):
    auth_key = read_api_key()
    main()

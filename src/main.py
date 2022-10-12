import requests


def main():
    #59.350331, 18.007853
    #59.305312, 18.114778
    data = """
<REQUEST>
    <LOGIN authenticationkey='""" + auth_key+"""' />
    <QUERY objecttype="TrafficFlow" schemaversion="1.4">
    <FILTER>
    <WITHIN name="Geometry.WGS84" shape="box" value="18.007853 59.350331, 18.114778 59.305312"/>
        <AND>
            <EQ name="CountyNo" value="1" />
        </AND>
        <OR>
            <EQ name="VehicleType" value="bus" />
            <EQ name="VehicleType" value="bicycle" />
            <EQ name="VehicleType" value="tram" />
            <EQ name="VehicleType" value="car" />
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

"""---------------------------------------------------------------------------------------------------------------------
Name: Aryaman Singh & Yunpenn Cheng
Email ID: asin0039@student.monash.edu & yche0049@student.monash.edu
Demonstrator: Najam Nazar
Unit: FIT 2107
COURSE: Software Engineering & Information Technology
--------------------------------------------------------UNIT TESTS------------------------------------------------------
"""

# import all the files
import unittest
import openweather
import argparse
from datetime import datetime
from unittest.mock import patch

# -------------------------------------------------------ALL CASES------------------------------------------------------


# this is a class to test all the cases
class TestParseResult(unittest.TestCase):

    @patch("openweather.send_request")
    def test_check_sunrise(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=True, sunset=False, temp=None, time=False, wind=False, humidity=False, pressure=None))
        assert "The sunrise time is 2019-10-12 06:00:00" in output_string, "Sunrise result string is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_sunset(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=True, temp=None, time=False, wind=False, humidity=False, pressure=None))
        assert "The sunset time is 2019-10-12 19:00:00" in output_string, "Sunset result string is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_temp_cel(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=True, sunset=False, temp='celsius', time=False, wind=False, humidity=False, pressure=None))
        assert "ranges from 20 - 35" in output_string, "Temperature is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_temp_fah(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=False, temp='fahrenheit', time=False, wind=False, humidity=False, pressure=False))
        assert "ranges from 20 - 35" in output_string, "Temperature is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_time(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=False, temp=None, time=True, wind=False, humidity=False, pressure=None))
        assert "2019-10-12 02:00:00" in output_string, "Time is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_pressure(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=False, temp=None, time=False, wind=False, humidity=False, pressure=True))
        assert "Pressure is 900hPa" in output_string, "Pressure is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_cloud(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=True,
                                                                                                sunrise=False, sunset=False, temp=False, time=False, wind=False, humidity=False, pressure=False))
        assert "Cloudness is 20%" in output_string, "Cloudiness is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_wind(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=False, temp=False, time=False, wind=True, humidity=False, pressure=False))
        assert "Wind speed of 3 from 92.619 degrees" in output_string, "Wind is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_humidity(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=None, city='Melbourne', cloud=False,
                                                                                                sunrise=False, sunset=False, temp=False, time=False, wind=False, humidity=True, pressure=False))
        assert "Humidity is 55%" in output_string, "Humidity is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_no_input(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = openweather.parse_result(send_request.return_value, argparse.Namespace(time=False, pressure=False, cloud=False, humidity=False, wind=False, sunset=False, sunrise=False,
                                                                                               temp=False))
        assert "Error: Add some feature!" in output_string, "This is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_cod(self, send_request):
        send_request.return_value = self.harcoded_response(200)
        output_string = send_request['cod']
        assert 200, "This is not as expected. It is " + output_string

    @patch("openweather.get_args")
    def test_check_city_name(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='melbourne',
                                                   cloud=True, gc='', help=False, humidity=False, pressure=True,
                                                   sunrise=False, sunset=False, temp='celsius', time=True, wind=False,
                                                   z='')
        output_url = openweather.compose_url(get_args.return_value)

        assert "melbourne" in output_url, "URL is not as expected. It is " + output_url

    @patch("openweather.get_args")
    def test_check_city_id(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=522, city='', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=False, z='')
        output_url = openweather.compose_url(get_args.return_value)

        assert "id=522" in output_url, "URL is not as expected. It is " + output_url

    @patch("openweather.get_args")
    def test_check_city_coordinates(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='', cloud=True,
                                                   gc='11', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=False, z='')
        output_url = openweather.compose_url(get_args.return_value)

        assert "lon=1&lat=1" in output_url, "URL is not as expected. It is " + output_url

    @patch("openweather.get_args")
    def test_check_city_zipcode(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=False, z='3168,au')
        output_url = openweather.compose_url(get_args.return_value)

        assert "zip=3168,au" in output_url, "URL is not as expected. It is " + output_url

    @patch("openweather.get_args")
    def test_check_wrong_temp(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='yoyo', time=True, wind=False, z='3168,au')
        output_url = openweather.compose_url(get_args.return_value)

        assert -2 == output_url, "Temperature scale is not as expected. It is " + str(output_url)

    @patch("openweather.get_args")
    def test_check_multiple_city_args(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=522, city='', cloud=True,
                                                   gc=None, help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=False, z='3168,au')
        output_url = openweather.compose_url(get_args.return_value)

        assert -1 == output_url, "Error occurred when url is unable to be made. The output url is " + str(output_url)

    @patch("openweather.send_request")
    def test_check_process_check(self, send_request):
        send_request.return_value = self.harcoded_response(300)
        output_string = openweather.process(send_request.return_value, argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=True, city=False, cloud=False,
                                                   gc=False, help=False, humidity=False, pressure=False, sunrise=False,
                                                   sunset=False, temp=True, time=False, wind=False, z=False))

        assert "300" in output_string, "This is not as expected. It is " + output_string

    @patch("openweather.send_request")
    def test_check_process_check2(self, send_request):
        send_request.return_value = self.harcoded_response(200)

        assert 200 == send_request.return_value['cod'], 'Cannot Connect error: ' + str(send_request.return_value['cod'])

    @patch("openweather.get_args")
    def test_check_process2_check(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=522, city='Melbourne', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=False, z='AU')
        output_url = openweather.process2(get_args.return_value)

        assert "You must specify only one of city name, city id, geographic coordinates or zip code" \
               in output_url, "Output is not as expected. It is " + output_url

    @patch("openweather.get_args")
    def test_check_process2_check2(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=-1, city='Melbourne', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=False, temp='yoyo', time=True, wind=False, z='')
        output_url = openweather.process2(get_args.return_value)

        assert "Unknown temperature unit" in output_url, "Unit is coming as " + output_url

    @patch("openweather.get_args")
    def test_check_url_cel(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=533, city='', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=True,
                                                   sunset=False, temp='celsius', time=False, wind=False, z='')
        output_url = openweather.compose_url(get_args.return_value)

        assert "http://api.openweathermap.org/data/2.5/weather?id=533&units=metric&appid=a61cbb04fbd6033b201358290286a8ed" \
               == output_url, "Error occurred when url is unable to be made. The output url is " + str(output_url)

    @patch("openweather.get_args")
    def test_check_url_fah(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=533, city='', cloud=True,
                                                   gc='', help=False, humidity=False, pressure=True, sunrise=False,
                                                   sunset=True, temp='fahrenheit', time=False, wind=False, z='')
        output_url = openweather.compose_url(get_args.return_value)

        assert "http://api.openweathermap.org/data/2.5/weather?id=533&units=imperial&appid=a61cbb04fbd6033b201358290286a8ed" \
               == output_url, "Error occurred when url is unable to be made. The output url is " + str(output_url)

    @patch("openweather.get_args")
    def test_check_url2(self, get_args):
        get_args.return_value = argparse.Namespace(api='a61cbb04fbd6033b201358290286a8ed', cid=533, city='', cloud=True,
                                                   gc='', help=False, humidity=True, pressure=True, sunrise=False,
                                                   sunset=False, temp='celsius', time=True, wind=True, z='')
        output_url = openweather.process2(get_args.return_value)

        assert "http://api.openweathermap.org/data/2.5/weather?id=533&units=metric&appid=a61cbb04fbd6033b201358290286a8ed" \
               == output_url, "Error occurred when url is unable to be made. The output url is " + str(output_url)

    def test_check_get_args(self):
        parser = openweather.get_args()
        parsed = parser.parse_args(['-api', 'a61cbb04fbd6033b201358290286a8ed', '-city', 'melbourne'])
        assert parsed.city

    def test_check_get_args3(self):
        parser = openweather.get_args()
        parsed = parser.parse_args(['-api', 'a61cbb04fbd6033b201358290286a8ed', '-z', '3168'])
        assert parsed.z

# -----------------------------------------------HARDCODED RESPONSE-----------------------------------------------------

    def harcoded_response(self, cod):
        date = datetime(2019,10,12,2,0).timestamp()
        sunrise = datetime(2019,10,12,6,0).timestamp()
        sunset = datetime(2019,10,12,19,0).timestamp()

        return {"coord": {"lon": 139,"lat": 35},
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "base": "stations",
                "main": {
                    "temp": 25,
                    "pressure": 900,
                    "humidity": 55,
                    "temp_min": 20,
                    "temp_max": 35,
                },
                "wind": {
                    "speed": 3,
                    "deg": 92.619
                },
                "clouds": {
                    "all": 20
                },
                "dt": date,
                "sys":{
                    "type": 3,
                    "id": 2019346,
                    "message": 0.0034,
                    "country": "AU",
                    "sunrise": sunrise,
                    "sunset": sunset
                },
                "timezone": 32400,
                "id": 1851632,
                "name": "Melbourne",
                "cod": cod
                }

# --------------------------------------------------------MAIN----------------------------------------------------------


if __name__ == '__main__':
    unittest.main()

# ---------------------------------------------------------END----------------------------------------------------------

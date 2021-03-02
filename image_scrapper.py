from bs4 import BeautifulSoup
import requests


url = 'https://www.reddit.com/r/Autos/'
header = {
    'Host': 'www.reddit.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': "csv=1; edgebucket=vSJIe7IykzimLuO46e; "
              "loid=00000000006qj2xof5.2.1591890731553"
              ".Z0FBQUFBQmU0bE1yNHlUQkRpUHJsY2VrZms0VkdfTnlNd2NHT3dRUUFxX093TmpuZEVNclBGUnpXSGZINVlmanNyeHRHT2lKazlGdHB"
              "yU0NTUWlnc1B1dE1nSVlpTFNNc0RGZGROM1l4aU1RRlpzbjFYbnpXXzNlelp1Y1BEOWJGYmE3SC1uUmpzckY; session_tracker=gf"
              "T4ENUZqncpgSTJIu.0.1591890741787.Z0FBQUFBQmU0bE0xZzdfM1NGVnhBUXNLeGNMVlhFM3U2QUl2Yk1ZdGllRnlVeEUwcVhUbXg"
              "3ODJ3cDdkb00xQk1rODhnZG14N0wzLTJPa21PN2Jyc05MWVRYR1V0UTdHbEZPZ2o2YWQyZV9kVUZrZGdWUnQwdFZsUF9Id29nVlVoU0o"
              "5azRqSGZISko; d2_token=3.ea7f5abcf907c7bd50ddfd6e488dcdd8ee014b1ded75845985818e230a96c639.eyJhY2Nlc3NUb2"
              "tlbiI6Ii1Cd3QzMlcxSTdjb1JudDVfTk5lcnl4Yzk4YzgiLCJleHBpcmVzIjoiMjAyMC0wNi0xMVQxNjo1MjoxMS4wMDBaIiwibG9nZ2"
              "VkT3V0Ijp0cnVlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19; eu_cookie_v2=3; mnet_session_depth=1%7C1591890735778; __"
              "aaxsc=2; recent_srs=t5_2r5qg%2C; reddaid=QXROTOGG36VPXCIB; __gads=ID=11850b28e4dac3a9:T=1591890742:S=ALN"
              "I_MZAL9mXBJ9NEI7QvIaPzPc2p271CA",
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
}
source = requests.get(url, headers=header)
soup = BeautifulSoup(source.content, 'html.parser')


images = soup.find_all("img", attrs={"alt": "Post image"})
for count, image in enumerate(images):
    image_src = image['src']
    source = requests.get(image_src)
    print(image_src)
    with open(str(count) + '.jpg', 'wb') as w:
        for chunk in source.iter_content(512):
            w.write(chunk)

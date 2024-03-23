import requests

RapidKey = ''  # Enter Here Your Rapid Api Key


def DoLike(
        LoginData:dict,
        MediaId:str,
        Proxy: str,
):
    global RapidKey

    querystring = {
          "Browserversion":LoginData['DeviceInfo']['BrowserVersion'],
          "Rollout": LoginData['Cookies']['x-instagram-rollout'],
          "Useragent": LoginData['DeviceInfo']['User-Agent'],
          "Proxy": Proxy,
          "Igdid":  LoginData['Cookies']['ig_did'],
          "Rur":  LoginData['Cookies']['rur'],
          "Xclaim":  LoginData['Cookies']['x-ig-set-www-claim'],
          "Mid":  LoginData['Cookies']['mid'],
          "Csrftoken":  LoginData['Cookies']['csrftoken'],
          "Appid":  LoginData['Cookies']['x-ig-app-id'],
          "Userid":  LoginData['Cookies']['ds_user_id'],
          "Datr":  LoginData['Cookies']['datr'],
          "Sessionid":  LoginData['Cookies']['sessionid'],
          "Mediaid": MediaId,
        }

    headers = {
        "X-RapidAPI-Key": RapidKey,
        "X-RapidAPI-Host": "namastegram.p.rapidapi.com"
    }

    return requests.get("https://namastegram.p.rapidapi.com/doLike", headers=headers, params=querystring).text


if __name__ == '__main__':

    LoginData={
            "Cookies": {
            "csrftoken": "GrHLSvBGwori5okhk6Eum2",
            "datr": "9yf_ZfVlokhkSt_gItvea605",
            "dpr": "1.25",
            "ds_user_id": "49078498762",
            "ig_did": "26DUJD72-A134-4249-BD4F-A0467A2503DD",
            "mid": "Zf8n9wAEAAFC2lVUCaxAVIxELyr_",
            "ps_l": "0",
            "ps_n": "0",
            "rur": "\"EAG\\05449078425082\\0541742756733:01f7f72489010d158cae5766f2eb88500e42b15319dbfa5f300092202a5c0a17e203dcac\"",
            "sessionid": "49078498762%3Ay5m90MaIv0987O%3A15%3AAYdCPP41zSDMxsBQyzwVgA0H94mgzrbXhUkljghSLg",
            "x-ig-app-id": "936619743392459",
            "x-ig-set-www-claim": "hmac.AR2qBB1GSfmt5oY6fMLgO9878HzqahJVd4PNtJrkLFuOXORy",
            "x-instagram-rollout": "1012271930"
          },
          "DeviceInfo": {
            "BrowserVersion": "84.0.4147.135",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
          },
          "Message": "LoginDone",
          "Status": {
            "authenticated": True,
            "oneTapPrompt": True,
            "status": "ok",
            "user": True,
            "userId": "49078498762"
          }
        }

    Proxy =''  # Enter Proxy Here In This Format ( username:password@host:port )
    MediaId='' #Enter Post MediaId Which One You Want To Like
    print(DoLike(LoginData,MediaId,Proxy))

    #Success Like Response

    '''{
  "Message": "{"status":"ok"}"
}'''


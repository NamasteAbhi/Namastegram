import requests
import base64

RapidKey = ''  # Enter Here Your Rapid Api Key


def UploadReel(
        LoginData:dict,
        ReelInBase64:str,
        ReelType:str,
        Caption:str,
        Proxy: str
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
        }

    Payload={
        "ReelInBase64": ReelInBase64,
        "ReelType": ReelType,
        "Caption": Caption
    }

    headers = {
        "X-RapidAPI-Key": RapidKey,
        "X-RapidAPI-Host": "namastegram.p.rapidapi.com"
    }

    return requests.post("https://namastegram.p.rapidapi.com/uploadReel", headers=headers, params=querystring,json=Payload,timeout=50).text


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

    with open('Reel.mp4','rb') as E:
        ReelInBase64=base64.b64encode(E.read()).decode()

    Proxy =''  # Enter Proxy Here In This Format ( username:password@host:port )
    ReelType='mp4' # Enter Video Format Here
    Caption='Nice' # Enter Caption Here
    print(UploadReel(LoginData,ReelInBase64,ReelType,Caption,Proxy))

    #Success Comment Response

    '''{
  "Message": {
    "media": {
      "taken_at": 1711224819,
      "pk": "3330317543635297144",
      "id": "3330317543635297144_49078425082",
      "comment_threading_enabled": false,
      "has_hidden_comments": false,
      "is_visual_reply_commenter_notice_enabled": true,
      "explore_hide_comments": false,
      "is_unified_video": true,
      "device_timestamp": 1711224809,
      "client_cache_key": "MzMzMDMxNzU0MzYzNTI5NzE0NA==.2",
      "filter_type": 0,
      "caption_is_edited": false,
      "like_and_view_counts_disabled": false,
      "strong_id__": "3330317543635297144_49078425082",
      "is_reshare_of_text_post_app_media_in_ig": false,
      "is_post_live_clips_media": false,
      "deleted_reason": 0,
      "integrity_review_decision": "pending",
      "has_shared_to_fb": 0,
      "should_request_ads": false,
      "commerciality_status": "not_commercial",
      "has_delayed_metadata": false,
      "view_state_item_type": 128,
      "logging_info_token": "AA==",
      "clips_delivery_parameters": {},
      "mezql_token": "",
      "commenting_disabled_for_viewer": false,
      "max_num_visible_preview_comments": 2,
      "has_more_comments": false,
      "preview_comments": [],
      "comments": [],
      "comment_count": 0,
      "can_view_more_preview_comments": false,
      "hide_view_all_comment_entrypoint": false,
      "is_comments_gif_composer_enabled": true,
      "comment_inform_treatment": {
        "should_have_inform_treatment": false,
        "text": "",
        "url": null,
        "action_type": null
      },
      "video_subtitles_enabled": false,
      "video_versions": [
        {
          "type": 101,
          "width": 576,
          "height": 1024,
          "url": "https://scontent-fra5-1.cdninstagram.com/v/t50.2886-16/420628187_1909691642778542_5552555536572611002_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6ImlnX3Byb2dyZXNzaXZlX3VybGdlbi5jbGlwcy5jMi5hc2ljX2hxMl9oZF9wcm9ncmVzc2l2ZSIsInFlX2dyb3VwcyI6IltcImlnX3Byb2dyZXNzaXZlX3VybGdlbi5wcm9kdWN0X3R5cGUuY2xpcHNcIl0ifQ\\u0026_nc_ht=scontent-fra5-1.cdninstagram.com\\u0026_nc_cat=102\\u0026_nc_ohc=0xnLhp1FufQAX_i5Zj-\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfBkhs2KYqlBhzcdmNMUBSKJlWcAu-YCxOezVGfYohVPIA\\u0026oe=66020E0D\\u0026_nc_sid=da5c95",
          "id": "932962814876182"
        },
        {
          "type": 102,
          "width": 360,
          "height": 640,
          "url": "https://scontent-fra3-2.cdninstagram.com/v/t50.2886-16/433083404_260137693827340_1640026501173051008_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6ImlnX3Byb2dyZXNzaXZlX3VybGdlbi5jbGlwcy5jMi5hc2ljX2hxMV9zZF9wcm9ncmVzc2l2ZSIsInFlX2dyb3VwcyI6IltcImlnX3Byb2dyZXNzaXZlX3VybGdlbi5wcm9kdWN0X3R5cGUuY2xpcHNcIl0ifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=QJ59LFoweeAAX_SAXTw\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDaNPiem3-CQGD1BlZ_tll0jMWgwfzk4Dij7YreOltDSg\\u0026oe=660256D9\\u0026_nc_sid=da5c95",
          "id": "926253332313916"
        },
        {
          "type": 103,
          "width": 360,
          "height": 640,
          "url": "https://scontent-fra3-2.cdninstagram.com/v/t50.2886-16/433083404_260137693827340_1640026501173051008_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6ImlnX3Byb2dyZXNzaXZlX3VybGdlbi5jbGlwcy5jMi5hc2ljX2hxMV9zZF9wcm9ncmVzc2l2ZSIsInFlX2dyb3VwcyI6IltcImlnX3Byb2dyZXNzaXZlX3VybGdlbi5wcm9kdWN0X3R5cGUuY2xpcHNcIl0ifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=QJ59LFoweeAAX_SAXTw\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDaNPiem3-CQGD1BlZ_tll0jMWgwfzk4Dij7YreOltDSg\\u0026oe=660256D9\\u0026_nc_sid=da5c95",
          "id": "926253332313916"
        }
      ],
      "video_duration": 9.033,
      "has_audio": true,
      "video_subtitles_translations_enabled": false,
      "sticker_translations_enabled": false,
      "shop_routing_user_id": null,
      "can_see_insights_as_brand": false,
      "is_organic_product_tagging_eligible": false,
      "has_liked": false,
      "has_privately_liked": false,
      "like_count": 0,
      "facepile_top_likers": [],
      "likers": [],
      "top_likers": [],
      "media_type": 2,
      "code": "C43qilBoiN4",
      "can_viewer_reshare": true,
      "caption": {
        "bit_flags": 0,
        "created_at": 1711224820,
        "created_at_utc": 1711224820,
        "did_report_as_spam": false,
        "is_ranked_comment": false,
        "pk": "18081139741449684",
        "share_enabled": false,
        "content_type": "comment",
        "media_id": "3330317543635297144",
        "status": "Active",
        "type": 1,
        "user_id": "49078425082",
        "text": "Nice",
        "user": {
          "allowed_commenter_type": "any",
          "fbid_v2": "17841448992474803",
          "feed_post_reshare_disabled": false,
          "full_name": "leila abbasi",
          "has_onboarded_to_text_post_app": true,
          "id": "49078425082",
          "is_private": false,
          "is_unpublished": false,
          "pk": "49078425082",
          "pk_id": "49078425082",
          "reel_auto_archive": "on",
          "show_account_transparency_details": true,
          "show_insights_terms": false,
          "strong_id__": "49078425082",
          "third_party_downloads_enabled": 0,
          "username": "namastebots",
          "account_badges": [],
          "can_boost_post": true,
          "can_see_organic_insights": true,
          "fan_club_info": {
            "fan_club_id": null,
            "fan_club_name": null,
            "is_fan_club_referral_eligible": null,
            "fan_consideration_page_revamp_eligiblity": null,
            "is_fan_club_gifting_eligible": null,
            "subscriber_count": null,
            "connected_member_count": null,
            "autosave_to_exclusive_highlight": null,
            "has_enough_subscribers_for_ssc": null
          },
          "has_anonymous_profile_picture": false,
          "hd_profile_pic_url_info": {
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDebATU7LDbfATkC6CPICPuTmV0LLQZ70zwv3tPzz0mtw\\u0026oe=66039785\\u0026_nc_sid=da5c95",
            "width": 612,
            "height": 612
          },
          "hd_profile_pic_versions": [
            {
              "width": 320,
              "height": 320,
              "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s320x320\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfC2L1yAyUdldh3HiEaevnWWe9nZb9daqV1zu3nqfAzdlA\\u0026oe=66039785\\u0026_nc_sid=da5c95"
            }
          ],
          "interop_messaging_user_fbid": "17847050108633083",
          "is_verified": false,
          "profile_pic_id": "3072383349709180799_49078425082",
          "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s150x150\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDAtGhkMRD8_JYytHceDFg-Sqw_Km-0udxtdfa8mZMW8A\\u0026oe=66039785\\u0026_nc_sid=da5c95",
          "transparency_product_enabled": false
        },
        "is_covered": false,
        "private_reply_status": 0
      },
      "clips_tab_pinned_user_ids": [],
      "sharing_friction_info": {
        "should_have_sharing_friction": false,
        "bloks_app_url": null,
        "sharing_friction_payload": null
      },
      "play_count": 0,
      "media_appreciation_settings": {
        "media_gifting_state": "not_applicable",
        "gift_count_visibility": "enabled"
      },
      "original_media_has_visual_reply_media": false,
      "fb_user_tags": {
        "in": []
      },
      "invited_coauthor_producers": [],
      "can_viewer_save": true,
      "is_in_profile_grid": true,
      "profile_grid_control_enabled": true,
      "highlights_info": {
        "added_to": []
      },
      "media_cropping_info": {
        "square_crop": {
          "crop_left": 0,
          "crop_right": 0,
          "crop_top": 0,
          "crop_bottom": 0
        }
      },
      "product_suggestions": [],
      "user": {
        "allowed_commenter_type": "any",
        "fbid_v2": "17841448992474803",
        "feed_post_reshare_disabled": false,
        "full_name": "leila abbasi",
        "has_onboarded_to_text_post_app": true,
        "id": "49078425082",
        "is_private": false,
        "is_unpublished": false,
        "pk": "49078425082",
        "pk_id": "49078425082",
        "reel_auto_archive": "on",
        "show_account_transparency_details": true,
        "show_insights_terms": false,
        "strong_id__": "49078425082",
        "third_party_downloads_enabled": 0,
        "username": "namastebots",
        "account_badges": [],
        "can_boost_post": true,
        "can_see_organic_insights": true,
        "fan_club_info": {
          "fan_club_id": null,
          "fan_club_name": null,
          "is_fan_club_referral_eligible": null,
          "fan_consideration_page_revamp_eligiblity": null,
          "is_fan_club_gifting_eligible": null,
          "subscriber_count": null,
          "connected_member_count": null,
          "autosave_to_exclusive_highlight": null,
          "has_enough_subscribers_for_ssc": null
        },
        "has_anonymous_profile_picture": false,
        "hd_profile_pic_url_info": {
          "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDebATU7LDbfATkC6CPICPuTmV0LLQZ70zwv3tPzz0mtw\\u0026oe=66039785\\u0026_nc_sid=da5c95",
          "width": 612,
          "height": 612
        },
        "hd_profile_pic_versions": [
          {
            "width": 320,
            "height": 320,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s320x320\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfC2L1yAyUdldh3HiEaevnWWe9nZb9daqV1zu3nqfAzdlA\\u0026oe=66039785\\u0026_nc_sid=da5c95"
          }
        ],
        "interop_messaging_user_fbid": "17847050108633083",
        "is_verified": false,
        "profile_pic_id": "3072383349709180799_49078425082",
        "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s150x150\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDAtGhkMRD8_JYytHceDFg-Sqw_Km-0udxtdfa8mZMW8A\\u0026oe=66039785\\u0026_nc_sid=da5c95",
        "transparency_product_enabled": false
      },
      "image_versions2": {
        "candidates": [
          {
            "width": 612,
            "height": 1088,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.29350-15/434346433_291196113998596_2663483248957352683_n.jpg?stp=dst-jpg_e15\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42MTJ4MTA4OC5zZHIifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=wsmL9YzZIMIAX_xY1yL\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026ig_cache_key=MzMzMDMxNzU0MzYzNTI5NzE0NA%3D%3D.2-ccb7-5\\u0026oh=00_AfBgEN4DMaMylvbWMWzCBNtYQcjOTf61ZCm_ysRBJgIm1A\\u0026oe=66026B7B\\u0026_nc_sid=da5c95"
          },
          {
            "width": 480,
            "height": 853,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.29350-15/434346433_291196113998596_2663483248957352683_n.jpg?stp=dst-jpg_e15_p480x480\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42MTJ4MTA4OC5zZHIifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=wsmL9YzZIMIAX_xY1yL\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026ig_cache_key=MzMzMDMxNzU0MzYzNTI5NzE0NA%3D%3D.2-ccb7-5\\u0026oh=00_AfBRN7OAkG8896vamS9kbhaMJuL81H_mSdYE8vdH7teu8w\\u0026oe=66026B7B\\u0026_nc_sid=da5c95"
          },
          {
            "width": 320,
            "height": 569,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.29350-15/434346433_291196113998596_2663483248957352683_n.jpg?stp=dst-jpg_e15_p320x320\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42MTJ4MTA4OC5zZHIifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=wsmL9YzZIMIAX_xY1yL\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026ig_cache_key=MzMzMDMxNzU0MzYzNTI5NzE0NA%3D%3D.2-ccb7-5\\u0026oh=00_AfByloS_abQJkJOcX5b6KknY0MfcO58I_y3IsuliryOl3Q\\u0026oe=66026B7B\\u0026_nc_sid=da5c95"
          },
          {
            "width": 240,
            "height": 427,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.29350-15/434346433_291196113998596_2663483248957352683_n.jpg?stp=dst-jpg_e15_p240x240\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42MTJ4MTA4OC5zZHIifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=wsmL9YzZIMIAX_xY1yL\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026ig_cache_key=MzMzMDMxNzU0MzYzNTI5NzE0NA%3D%3D.2-ccb7-5\\u0026oh=00_AfAzQcP38JtPKRQoCgR4Lr_Od1pifvbKyy_e93gNdEnrYA\\u0026oe=66026B7B\\u0026_nc_sid=da5c95"
          },
          {
            "width": 150,
            "height": 267,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.29350-15/434346433_291196113998596_2663483248957352683_n.jpg?stp=dst-jpg_e15_p150x150\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42MTJ4MTA4OC5zZHIifQ\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=wsmL9YzZIMIAX_xY1yL\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026ig_cache_key=MzMzMDMxNzU0MzYzNTI5NzE0NA%3D%3D.2-ccb7-5\\u0026oh=00_AfBzOLct2R2fhPw9sITJEgAqTHfmVIMZb8BhYFTuUmjGPA\\u0026oe=66026B7B\\u0026_nc_sid=da5c95"
          }
        ],
        "additional_candidates": {
          "igtv_first_frame": {
            "width": 640,
            "height": 1136,
            "url": "https://scontent-fra3-1.cdninstagram.com/v/t51.29350-15/433938710_428967329673925_4736615274457500641_n.jpg?stp=dst-jpg_e15\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42NDB4MTEzNi5zZHIifQ\\u0026_nc_ht=scontent-fra3-1.cdninstagram.com\\u0026_nc_cat=101\\u0026_nc_ohc=SVcI3QdXlRMAX99yC6E\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfBz5tdlu4zGeGx-O8DpwfZyvhbtYSd7WTBMwPBo34XyBg\\u0026oe=66041A26\\u0026_nc_sid=da5c95"
          },
          "first_frame": {
            "width": 640,
            "height": 1136,
            "url": "https://scontent-fra3-1.cdninstagram.com/v/t51.29350-15/433938710_428967329673925_4736615274457500641_n.jpg?stp=dst-jpg_e15\\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42NDB4MTEzNi5zZHIifQ\\u0026_nc_ht=scontent-fra3-1.cdninstagram.com\\u0026_nc_cat=101\\u0026_nc_ohc=SVcI3QdXlRMAX99yC6E\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfBz5tdlu4zGeGx-O8DpwfZyvhbtYSd7WTBMwPBo34XyBg\\u0026oe=66041A26\\u0026_nc_sid=da5c95"
          },
          "smart_frame": null
        },
        "smart_thumbnail_enabled": false
      },
      "original_width": 576,
      "original_height": 1024,
      "is_artist_pick": false,
      "enable_media_notes_production": false,
      "product_type": "clips",
      "is_paid_partnership": false,
      "inventory_source": "recommended_clips_chaining_model",
      "music_metadata": null,
      "social_context": [],
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZTA4NzQ3ZTZiZWU3NGU0MmFjNjA4YjM4MGE5Y2U0MTMzMzMwMzE3NTQzNjM1Mjk3MTQ0Iiwic2VydmVyX3Rva2VuIjoiMTcxMTIyNDgyMzUwMXwzMzMwMzE3NTQzNjM1Mjk3MTQ0fDQ5MDc4NDI1MDgyfGViM2IzOTNmNDlkNjE3ZWEyMGExMmQyMmM3YjhhMzc2ZjZlYzZjOGI3NWQ3MTViYTMyNTg0MWY5MDZjMjFkMTgifSwic2lnbmF0dXJlIjoiIn0=",
      "is_third_party_downloads_eligible": false,
      "ig_media_sharing_disabled": false,
      "are_remixes_crosspostable": false,
      "boosted_status": "not_boosted",
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "open_carousel_submission_state": "closed",
      "is_open_to_public_submission": false,
      "is_auto_created": false,
      "is_cutout_sticker_allowed": false,
      "is_reuse_allowed": false,
      "enable_waist": false,
      "owner": {
        "allowed_commenter_type": "any",
        "fbid_v2": "17841448992474803",
        "feed_post_reshare_disabled": false,
        "full_name": "leila abbasi",
        "has_onboarded_to_text_post_app": true,
        "id": "49078425082",
        "is_private": false,
        "is_unpublished": false,
        "pk": "49078425082",
        "pk_id": "49078425082",
        "reel_auto_archive": "on",
        "show_account_transparency_details": true,
        "show_insights_terms": false,
        "strong_id__": "49078425082",
        "third_party_downloads_enabled": 0,
        "username": "namastebots",
        "account_badges": [],
        "can_boost_post": true,
        "can_see_organic_insights": true,
        "fan_club_info": {
          "fan_club_id": null,
          "fan_club_name": null,
          "is_fan_club_referral_eligible": null,
          "fan_consideration_page_revamp_eligiblity": null,
          "is_fan_club_gifting_eligible": null,
          "subscriber_count": null,
          "connected_member_count": null,
          "autosave_to_exclusive_highlight": null,
          "has_enough_subscribers_for_ssc": null
        },
        "has_anonymous_profile_picture": false,
        "hd_profile_pic_url_info": {
          "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDebATU7LDbfATkC6CPICPuTmV0LLQZ70zwv3tPzz0mtw\\u0026oe=66039785\\u0026_nc_sid=da5c95",
          "width": 612,
          "height": 612
        },
        "hd_profile_pic_versions": [
          {
            "width": 320,
            "height": 320,
            "url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s320x320\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfC2L1yAyUdldh3HiEaevnWWe9nZb9daqV1zu3nqfAzdlA\\u0026oe=66039785\\u0026_nc_sid=da5c95"
          }
        ],
        "interop_messaging_user_fbid": "17847050108633083",
        "is_verified": false,
        "profile_pic_id": "3072383349709180799_49078425082",
        "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s150x150\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AA3Yet0BAAAA\\u0026ccb=7-5\\u0026oh=00_AfDAtGhkMRD8_JYytHceDFg-Sqw_Km-0udxtdfa8mZMW8A\\u0026oe=66039785\\u0026_nc_sid=da5c95",
        "transparency_product_enabled": false
      },
      "clips_metadata": {
        "achievements_info": {
          "show_achievements": true,
          "num_earned_achievements": 0
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "741241494800310"
        },
        "audio_type": "original_sounds",
        "branded_content_tag_info": {
          "can_add_tag": true
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "clips_creation_entry_point": "",
        "content_appreciation_info": {
          "enabled": false,
          "entry_point_container": null
        },
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "featured_label": null,
        "is_fan_club_promo_video": false,
        "is_public_chat_welcome_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "mashups_allowed": true,
          "can_toggle_mashups_allowed": true,
          "has_been_mashed_up": false,
          "is_light_weight_check": false,
          "formatted_mashups_count": null,
          "original_media": null,
          "privacy_filtered_mashups_media_count": null,
          "non_privacy_filtered_mashups_media_count": null,
          "mashup_type": null,
          "is_creator_requesting_mashup": false,
          "has_nonmimicable_additional_audio": false,
          "is_pivot_page_available": false
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18423264466042577",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": null,
        "professional_clips_upsell_type": 0,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": true,
        "show_tips": null,
        "template_info": null,
        "viewer_interaction_settings": null
      }
    },
    "upload_id": "1711224809",
    "status": "ok"
  }
}'''


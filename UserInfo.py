import requests

RapidKey = ''  # Enter Here Your Rapid Api Key


def GetUserInfo(
        LoginData:dict,
        VictimUserId:str,
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
          "VictimUserId": VictimUserId,
        }

    headers = {
        "X-RapidAPI-Key": RapidKey,
        "X-RapidAPI-Host": "namastegram.p.rapidapi.com"
    }

    return requests.get("https://namastegram.p.rapidapi.com/userInfo", headers=headers, params=querystring).text


if __name__ == '__main__':
    LoginData = {
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
    VictimUserId='49078425082' # Enter UserId To Get User Info
    print(GetUserInfo(LoginData,VictimUserId,Proxy))

    #Success Response

    '''{
  "Message": {
    "user": {
      "primary_profile_link_type": 0,
      "show_fb_link_on_profile": false,
      "show_fb_page_link_on_profile": false,
      "can_hide_category": true,
      "account_type": 3,
      "smb_support_partner": null,
      "current_catalog_id": null,
      "mini_shop_seller_onboarding_status": null,
      "about_your_account_bloks_entrypoint_enabled": true,
      "account_category": "",
      "aggregate_promote_engagement": true,
      "allowed_commenter_type": "any",
      "break_reminder_interval": 0,
      "can_add_fb_group_link_on_profile": false,
      "can_follow_hashtag": true,
      "can_see_support_inbox": false,
      "can_use_affiliate_partnership_messaging_as_creator": false,
      "can_use_affiliate_partnership_messaging_as_brand": false,
      "daily_time_limit": 0,
      "existing_user_age_collection_enabled": true,
      "fbid_v2": "17841448992474803",
      "feed_post_reshare_disabled": false,
      "full_name": "leila abbasi",
      "has_ig_profile": true,
      "has_onboarded_to_text_post_app": true,
      "has_public_tab_threads": true,
      "has_user_ever_set_break": false,
      "highlight_reshare_disabled": false,
      "include_direct_blacklist_status": true,
      "is_direct_roll_call_enabled": true,
      "is_hide_more_comment_enabled": true,
      "is_muted_words_custom_enabled": false,
      "is_muted_words_global_enabled": true,
      "is_muted_words_spamscam_enabled": false,
      "is_new_to_instagram": false,
      "is_new_to_instagram_30d": false,
      "is_parenting_account": false,
      "is_private": false,
      "is_quiet_mode_enabled": false,
      "is_secondary_account_creation": true,
      "last_seen_timezone": "",
      "pk": "49078425082",
      "pk_id": "49078425082",
      "profile_type": 0,
      "reel_auto_archive": "on",
      "show_account_transparency_details": true,
      "show_insights_terms": false,
      "show_post_insights_entry_point": true,
      "show_text_post_app_badge": true,
      "show_text_post_app_switcher_badge": true,
      "text_post_app_joiner_number": 43787332,
      "text_post_app_joiner_number_label": "43,787,332",
      "third_party_downloads_enabled": 0,
      "username": "namastebots",
      "usertag_review_enabled": false,
      "is_profile_picture_expansion_enabled": true,
      "is_opal_enabled": false,
      "strong_id__": "49078425082",
      "biography": "You're the sunshine that brightens my day. ☀️",
      "biography_with_entities": {
        "raw_text": "You're the sunshine that brightens my day. ☀️",
        "entities": []
      },
      "can_link_entities_in_bio": true,
      "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fwww.wwe.com%2F\u0026e=AT3_FFclZS7fJlxMF-BwXLO7wZqiK_Qa0_4GFitS0p1QjewnrUnr1sRFn4NeiH2Dav7P8sFLns6EDiQnWm144-re2ea_but_y_BKsqQ",
      "external_url": "http://www.wwe.com/",
      "can_hide_public_contacts": true,
      "category": "Community",
      "should_show_category": false,
      "category_id": "2612",
      "is_category_tappable": false,
      "should_show_public_contacts": false,
      "is_eligible_for_smb_support_flow": true,
      "is_eligible_for_lead_center": false,
      "lead_details_app_id": "com.bloks.www.ig.smb.services.lead_gen.all_leads",
      "is_business": false,
      "professional_conversion_suggested_account_type": 2,
      "direct_messaging": "",
      "can_claim_page": false,
      "can_crosspost_without_fb_token": false,
      "instagram_location_id": "",
      "address_street": "",
      "business_contact_method": "UNKNOWN",
      "city_id": "0",
      "city_name": "",
      "contact_phone_number": "",
      "is_profile_audio_call_enabled": false,
      "latitude": 0.0,
      "longitude": 0.0,
      "public_email": "",
      "public_phone_country_code": "",
      "public_phone_number": "",
      "zip": "",
      "displayed_action_button_partner": null,
      "smb_delivery_partner": null,
      "smb_support_delivery_partner": null,
      "displayed_action_button_type": "",
      "is_call_to_action_enabled": false,
      "num_of_admined_pages": null,
      "page_id": null,
      "page_name": null,
      "ads_page_id": null,
      "ads_page_name": null,
      "eligible_shopping_signup_entrypoints": [],
      "shopping_onboarding_state": "not_started",
      "is_shopping_revoked_for_seller": false,
      "can_merchant_use_shop_management": false,
      "shop_management_access_state": "none",
      "is_eligible_for_product_tagging_null_state": false,
      "eligible_catalog_management_entrypoints": [],
      "commerce_onboarding_config": {},
      "is_igd_product_picker_enabled": false,
      "eligible_shopping_formats": [],
      "is_shopping_settings_enabled": false,
      "is_shopping_community_content_enabled": false,
      "is_shopping_auto_highlight_eligible": false,
      "is_shopping_catalog_source_selection_enabled": false,
      "shopping_post_onboard_nux_type": null,
      "ads_incentive_expiration_date": null,
      "account_badges": [],
      "all_media_count": 242,
      "allow_automatic_previews_setting": true,
      "allow_mention_setting": "everyone",
      "allow_tag_setting": "everyone",
      "audio_go_dark_events": [],
      "auto_expand_chaining": false,
      "besties_count": 0,
      "bio_links":[{"link_id":"17843258781070986","url":"http://www.wwe.com/","lynx_url":"https://l.instagram.com/?u=http%3A%2F%2Fwww.wwe.com%2F\\u0026e=AT0EP9emfZhrK3WUOL0jW-CAbqrg10FroTVhXOZVF94s_DHSjom0iDxPcyWiZlnw6ViQb-O0gdHcE3DaOFF6_LqRXVspJP5lr3ebtts","link_type":"external","title":"","image_url":"","is_pinned":false,"open_external_url_with_in_app_browser":true}],"birthday_today_visibility_for_viewer":"NOT_VISIBLE","can_be_tagged_as_sponsor":true,"can_boost_post":true,"can_convert_to_business":false,"can_create_new_standalone_fundraiser":true,"can_create_new_standalone_personal_fundraiser":true,"can_create_sponsor_tags":true,"can_see_organic_insights":true,"can_tag_products_from_merchants":false,"can_see_support_inbox_v1":true,"can_use_branded_content_discovery_as_brand":false,"can_use_branded_content_discovery_as_creator":false,"can_use_paid_partnership_messaging_as_creator":false,"chaining_upsell_cards":[],"creator_shopping_info":{"linked_merchant_accounts":[]},"fan_club_info":{"fan_club_id":null,"fan_club_name":null,"is_fan_club_referral_eligible":null,"fan_consideration_page_revamp_eligiblity":null,"is_fan_club_gifting_eligible":null,"subscriber_count":null,"connected_member_count":null,"autosave_to_exclusive_highlight":null,"has_enough_subscribers_for_ssc":null},"follow_friction_type":0,"follower_count":2039,"following_count":504,"has_anonymous_profile_picture":false,"has_chaining":true,"has_collab_collections":false,"has_eligible_whatsapp_linking_category":true,"has_exclusive_feed_content":false,"has_fan_club_subscriptions":false,"has_guides":false,"has_highlight_reels":false,"has_music_on_profile":false,"has_placed_orders":false,"has_private_collections":false,"has_saved_items":true,"has_videos":false,"hd_profile_pic_url_info":{"url":"https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AEF8tYYBAAAA\\u0026ccb=7-5\\u0026oh=00_AfCYHFeXdqqXNnsyp09jkEbKAUc_8NwCaCbCWAeh1edrOw\\u0026oe=660591C5\\u0026_nc_sid=1e20d2","width":612,"height":612},"hd_profile_pic_versions":[{"width":320,"height":320,"url":"https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s320x320\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AEF8tYYBAAAA\\u0026ccb=7-5\\u0026oh=00_AfB6bajqibuljxMJxxoxPgqf7nLIlqhX4qW6MxWJohRXGQ\\u0026oe=660591C5\\u0026_nc_sid=1e20d2"}],"interop_messaging_user_fbid":"17847050108633083","is_allowed_to_create_standalone_nonprofit_fundraisers":false,"is_api_user":false,"is_eligible_for_meta_verified_links_in_reels":true,"is_eligible_for_meta_verified_enhanced_link_sheet":true,"is_eligible_for_meta_verified_enhanced_link_sheet_consumption":false,"is_eligible_for_meta_verified_multiple_addresses_creation":false,"is_eligible_for_meta_verified_multiple_addresses_consumption":false,"is_eligible_to_show_fb_cross_sharing_nux":true,"is_in_canada":false,"is_interest_account":true,"is_memorialized":false,"is_needy":false,"is_potential_business":false,"is_regulated_news_in_viewer_location":false,"is_remix_setting_enabled_for_posts":true,"is_remix_setting_enabled_for_reels":true,"is_profile_action_needed":false,"is_profile_broadcast_sharing_enabled":true,"is_regulated_c18":false,"is_stories_teaser_muted":false,"is_tooltip_disabled_param":false,"is_recon_ad_cta_on_profile_eligible_with_viewer":true,"is_supervision_features_enabled":true,"is_verified":false,"is_whatsapp_linked":false,"latest_besties_reel_media":0,"latest_reel_media":0,"limited_interactions_enabled":false,"linked_fb_info":{},"media_count":219,"merchant_checkout_style":"none","nametag":{"mode":0,"gradient":2,"emoji_color":-16777216,"selfie_sticker":0,"emoji":"😀"},"open_external_url_with_in_app_browser":true,"pinned_channels_info":{"pinned_channels_list":[],"has_public_channels":false},"profile_pic_id":"3072383349709180799_49078425082","profile_pic_url":"https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s150x150\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AEF8tYYBAAAA\\u0026ccb=7-5\\u0026oh=00_AfAzjXzr6mOMEOkDfRpyEbkJGf_4cygG_Qzxiyv5W2HiUg\\u0026oe=660591C5\\u0026_nc_sid=1e20d2","pronouns":[],"recon_features":{"enable_recon_cta":true},"relevant_news_regulation_locations":[],"seller_shoppable_feed_type":"none","show_besties_badge":true,"show_conversion_edit_entry":false,"show_ig_app_switcher_badge":true,"show_shoppable_feed":false,"supervision_info":{"fc_url":"https://familycenter.instagram.com/dashboard/","daily_time_limit_without_extensions_seconds":null,"has_guardian":false,"has_stated_age":true,"is_eligible_for_supervision":false,"is_guardian_of_viewer":false,"is_guardian_user":false,"is_quiet_time_feature_enabled":false,"is_supervised_by_viewer":false,"is_supervised_or_in_cooldown":false,"is_supervised_user":false,"latest_valid_time_limit_extension_request":null,"quiet_time_intervals":null,"screen_time_daily_limit_description":null,"screen_time_daily_limit_seconds":null},"text_post_app_badge_label":"namastebots","total_ar_effects":0,"total_clips_count":192,"total_igtv_videos":0,"transparency_product_enabled":false,"whatsapp_number":"","has_disallowed_media_notes_reshare":false},"status":"ok"}'}'''


class Translation(object):

    START_MSG = """[👋](https://i.imgur.com/wF1voFb.gif)  Hello **{}**

○ Url Uploader ○ Renamer ○ YouTube DL
"""
    HELP_USER = """Hi **{}** 👋

● **For URL Uploader** :
    
○ Send Url. [ Link|New Name With Extension ] (Optional)
○ Send Custom Thumbnail. (Optional)
○ Select The Button :

🎞+📸 SVideo - Give File As Video With Screenshots
📁+📸 DFile  - Give File With Screenshots

🎞 Video  - Give File As Video Without Screenshots
📁 File  - Give File Without Screenshots

● **For Renamer** :

○ Send Me The File To Be Renamed.
○ Send Me A Thumbnail.
○ Reply To That Message With /rename New Name.extension. (📁 Upload As File)
○ Reply to that message with /renamevideo New Name.extension (🎞 Upload As Video)

● **YouTube DL** :

○ Send Me A Tumbnail if required. It'll be saved permanently.💯
○ If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
○ Send Me Youtube Link To Be Uploaded To Telegram.
○ Press /deletethumbnail To Delete Your Current Custom Thumbnail

NB : It is Recommended To Use A Custom Thubnail Because, Some Time Bot Wont Upload The File Without a Custom Thumbnail.
"""

    ABOUT = """Hi {},

**📝 Language:** Python 3 

**🧰 Framework:** Pyrogram

**📮 Channel:** [@DamienSoukara](https://t.me/DamienSoukara)

**👥 Group:** [@DamienHelp](https://t.me/DamienHelp)

**👨‍💻 Developer:** [@AmineSoukara](t.me/AmineSoukara)

**©️ Source Code:** [Here](t.me/AmineSoukara)

"""
    CURENT_PLAN_DETAILS = """ℹ **Current Plan Details :**
Telegram ID: <code>{}</code>
Plan Name: #Free  User
Expires On: 01/01/2022"""

    FORMAT_SELECTION = "Select The Desired Format: <a href='{}'>File Size Might Be Approximate</a> \nIf You Want To Set Custom Thumbnail, Send Photo Before Or Quickly After Tapping On Any Of The Below Buttons.\nYou Can Use /deletethumbnail To Delete The Auto-Generated Thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If You Want To Download Premium Videos, Provide in The Following Format:
URL | filename | username | password"""
    DOWNLOAD_START = "✅ Trying To Download, Please Wait"
    UPLOAD_START = "☑ Trying To Upload, Please Wait"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 1.9GB Due To Telegram API Limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded In {} Seconds. \nJoin : @DamienSoukara \nUploaded In {} Seconds."
    SAVED_CUSTOM_THUMB_NAIL = "🖼 Custom Video / File Thumbnail Saved. This Image Will Be Used In The Video / File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "❌ Custom Thumbnail Cleared Succesfully."
    CUSTOM_CAPTION_UL_FILE = "@DamienSoukara"
    NO_VOID_FORMAT_FOUND = "❌ ERROR...\n<b>YouTubeDL</b> Said: {}"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail To A Media Album, To Generate Custom Thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album Should Contain Only Two Photos. Please Re-Send The Media Album, And Then Try Again, Or Send Only Two Photos In An Album."
    CANCEL_STR = "❌ Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} Files In {} Seconds"
    SLOW_URL_DECED = "Gosh That Seems To Be A very Slow URL. Since You Were Screwing My Home, I am In No Mood To Download This File. Meanwhile, Why Don't Tou Try This:==> https://shrtz.me/PtsVnf6 And Get Me A Fast URL So That I Can Upload To Telegram, Without Me Slowing Down For Other Users."

    MOREHELP = """[💬](https://i.imgur.com/z0gaQ0Y.jpg)
Extra Help : 
"""

    YTDL = """● YouTube DL

○ Send Me A Tumbnail if required. It'll be saved permanently.💯
○ If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
○ Send Me Youtube Link To Be Uploaded To Telegram.
○ Press /deletethumbnail To Delete Your Current Custom Thumbnail

NB : It is Recommended To Use A Custom Thubnail Because, Some Time Bot Wont Upload The File Without a Custom Thumbnail.
"""
    URLDL = """● For URL Uploader :
    
○ Send Url. [ Link|New Name With Extension ] (Optional)
○ Send Custom Thumbnail. (Optional)
○ Select The Button :

🎞+📸 SVideo - Give File As Video With Screenshots
📁+📸 DFile  - Give File With Screenshots

🎞 Video  - Give File As Video Without Screenshots
📁 File  - Give File Without Screenshots
"""
    RENAMERX = """● For Renamer :

○ Send Me The File To Be Renamed.
○ Send Me A Thumbnail.
○ Reply To That Message With /rename New Name.extension. (📁 Upload As File)
○ Reply to that message with /renamevideo New Name.extension (🎞 Upload As Video)
"""

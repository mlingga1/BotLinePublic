from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\nScript Bot Publik Beta Tester.\n")

creator = LineClient(authToken="Eyiqp43K4w5l6HaDxYma.etwUKT1PbwVkZ2+PE2hKoG.GKFeCYna46pgewS6zwmQOfc1Mx08zNDWNTjEkD8pkSI=")
creator.log("YOUR TOKEN : " + str(creator.authToken))
channel = LineChannel(creator)
creator.log("Channel Access Token : " + str(channel.channelAccessToken))

client = LineClient(authToken="EynTkhMWNYn8gjKL2H0d./Zi8vXvkUMBAeXN6W0hVVq.VD7PqHuQ4Xxw5H3tPIP1l1aANZyfE1t9s7750f7m4kw=")
client.log("YOUR TOKEN : " + str(client.authToken))
channel1 = LineChannel(client)
client.log("Channel Access Token : " + str(channel1.channelAccessToken))

print ("#######################{Success Login}######################")

clientProfile = creator.getProfile()
clientSettings = creator.getSettings()
creatorProfile = creator.getProfile()
creatorSettings = creator.getSettings()
poll = LinePoll(client)
call = client
mid = [client]
myMID = client.profile.mid
creatorMID = creator.profile.mid
Admin=[myMID,creatorMID]
Owner=["u1135ae92dd69056bcacf6fe97b61e43a","u635b2f79129251f9939f378a9cc464a4"]
Team = Admin + mid + Owner

contact = client.getProfile()
backup = client.getProfile()
contact1 = creator.getProfile()
backup1 = creator.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
backup.displayName = contact1.displayName
backup.statusMessage = contact1.statusMessage
backup.pictureStatus = contact1.pictureStatus

Connect_to = {
    "UnsendMessage":False,
    "SpamInvite":False,
    "limit": 10,
    "Contact":False,
    "GName":"Priv8-L1ng",
    "AutoRespon":False,
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"Thanks For Add Me",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":False,
    "AutoReject":False,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":False,
    "BackupBot":True,
    "WcText": "Welcome ^_^",
    "Leave":False,
    "LvText": "Papaiii..",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "likeOn":{},
    "comment": "autolike by L1ng",
    "Admin": {
        "u1135ae92dd69056bcacf6fe97b61e43a":True #MID ADMIN TARO DISINI
    },
}

Mozilla = {
    "manAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Connect_to['readTime']
mulai = time.time() 
msg_dict = {}

myProfile = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus

cctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""
「 Bot Publik Beta Tester 」
•Help
•Type1
•Type2
•Type3
•Type4
•Owner
•Note
•priv | Private Command, Just For Creator :) |

    | Thanks To |
*Creator : https://line.me/ti/p/~Priv8_L1ng
*Google
*Line

######
Version 1.0
######


Type `Note` For Check Command
"""
Help2 ="""
「 Profile 」
•Me
•My Name
•My Bio
•My Picture
•My Cover
•My Video
•Speed
•Cekmid: [mid]
"""

Help3 ="""
「 Other Command 」
•Top News
•maps:
•cekcuaca:
•jadwalshalat:
•idline [query]
•apakah:
•kapan:
•wikipedia:
•kalender
•image [query]
•Musik|[query]
•youtube|[query]
    | Google |
•say-id:
•say-en:
•say-jp:
•say-ar:
•say-ko:
•indonesian:
•english:
•korea:
•japan:
•thailand:
•arab:
•malaysia:
•jawa:
"""

Help4 ="""
「 Steal Command 」
•stealname [@]
•stealbio [@]
•stealpict [@]
•stealcover [@]
•stealvideo [@]
•stealmid [@]
•info [@]
•clone [@]
•steal on/off
•contact on/off
"""

Help5 ="""
「 Group Command」
•spamtag|(range)
•spamtag (mention)
•Gcall|(range)
•Gcall
•broadcast:
•contactbc:
•leaveall grup
•Cancelall [Group]
•mentionall
•memberlist
•mic:add-on
•mic:del-on
•mimic on/off
•mimiclist
•gurl
•gcreator
•invite gcreator
•ginfo
•groupid
•changeprofilegroup on/off
•announce
"""

Help6 ="""
「 ON/OFF Command」
•unsend on/off
•ChangeProfile on/off
•timeline on/off
•like post
•like (mention)
•autojoin on/off
•autoreject on/off
•auto jointicket on/off
•gift:on/off
•copy on/off
•invite on/off
•link on/off
•lurking on/off/reset
•lurking read
•sider on/off
•welcome on/off
•leave on/off
•changeprofilegroup on/off
"""

Help7 ="""
    ~| Nothing :( |~
"""

Help8 ="""
「 Private Command」
    | Profile |
•Myprofile
•Rename
•changename:
•changebio:
•changewelcome:
•changeleave:
•comeback
•my team
•Grouplist
•Friendlist
•Friendlist mid
•Pendinglist
•Rm -chat
•Status
•refresh
•runtime
•restart
•logout
    | Owner |
•admindel [@]
•adminadd [@]
•admin:add-on
•admin:del-on
•banlock [@]
•contact ban
•clear ban
•blocklist
•banlist
"""

Help9 ="""
[ KICKER ]
•spam on [jmlah teks]
•kick [on,off->kickall]
•kill on/off
•kick [@]
•vkick [@]
•spaminvite on/off
"""

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d Abad\n%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_image(url, file_path):
    print('downloading image %s into %s' % (url, file_path))
    try:
        urllib.request.urlretrieve(url, file_path)
        return True
    except:
        print('※link not found')
        return False

def mentionMembers(to, mids=[]):
    if myMID in mids: mids.remove(myMID)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention Members 」\n'
    mention = '@Priv8-L1ng\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 </> 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            client.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def LINE_OP_TYPE(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if myMID in op.param3:
              if Connect_to['autoJoin'] == True:               
                    client.acceptGroupInvitation(op.param1)
                    print ("Bot Publik Join Di Group")
                    pass

        if op.type == 13:
            if myMID in op.param3:
              if Connect_to['AutojoinTicket'] == True:               
                     link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                     links = link_re.findall(msg.text)
                     n_links=[]
                     for l in links:
                         if l not in n_links:
                             n_links.append(l)
                     for ticket_id in n_links:
                             group=client.findGroupByTicket(ticket_id)
                             client.acceptGroupInvitationByTicket(group.id,ticket_id)
                             print ("Bot Publik Join Di Group With Auto Join Ticket")
                             pass

        if op.type == 13:
            if myMID in op.param3:
              if Connect_to['AutoReject'] == True:
                if op.param2 not in Team and op.param2 not in Connect_to["Admin"]:
                    gid = client.getGroupIdsInvited()
                    for i in gid:
                        client.rejectGroupInvitation(i)
                        pass

        elif op.type == 55:
            try:
                if cctv['Point1'][op.param1]==True:
                    if op.param1 in cctv['Point2']:  
                        Name = client.getContact(op.param2).displayName
                        kopi = client.getContact(op.param2).picturePath
                        pait = client.getGroup(op.param1)
                        if Name in cctv['Point3'][op.param1]:
                            pass
                        else:
                            cctv['Point3'][op.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    client.priv8l1ng(op.param1,op.param2," Hii\n","" + "\n Terus aku harus gimana kak?" )
                                    client.sendContact(op.param1, op.param2)
                                    client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(kopi))
                                else:
                                    client.priv8l1ng(op.param1,op.param2," Nah\n","" + "\n Serius ga mau chat kak ??" )
                                    client.sendContact(op.param1, op.param2)
                                    client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(kopi))
                            else:
                                client.priv8l1ng(op.param1,op.param2," Hey\n","" + "\n Woy ngelamun aje lu... !!! awas kesurupan!" )
                                client.sendContact(op.param1, op.param2)
                                client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(kopi))
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if op.param1 in Connect_to['readPoint']:
                    if op.param2 in Connect_to['readMember'][op.param1]:
                        pass
                    else:
                        Connect_to['readMember'][op.param1] += op.param2
                    Connect_to['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except:
                pass   

        if op.type == 17:
            if Connect_to["Welcome"] == True:
                if op.param2 not in mid:
                    ginfo = client.getGroup(op.param1)
                    client.priv8l1ng(op.param1,op.param2," Hii","" + "\n " + str(Connect_to['WcText']))
                    client.sendMessage(op.param1, None, contentMetadata={'mid':op.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if op.type == 15:
            if Connect_to["Leave"] == True:
                if op.param2 not in mid:
                    ginfo = client.getGroup(op.param1)
                    client.priv8l1ng(op.param1,op.param2," Hii","" + "\n " + str(Connect_to['LvText']))
                    client.sendMessage(op.param1, None, contentMetadata={'mid':op.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

        if op.type == 46:
            if op.param2 in Admin:
                client.removeAllMessages()


        if op.type == [25,26]:
            msg = op.message
            text = msg.text
            msgText = msg.text
            msg_id = msg.id
            send = msg.to           
            man = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = send
                elif msg.toType == 2:
                    to = send
                if msg.contentType == 0:
                    if Connect_to["autoRead"] == True:
                        client.sendChatChecked(send, msg_id)
                    if send in Connect_to["readPoint"]:
                        if man not in Connect_to["ROM"][send]:
                            Connect_to["ROM"][send][man] = True
                    if man in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][man] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(send,text)
                    if Connect_to["UnsendMessage"] == True:
                        msg = op.message
                        if msg.toType == 0:
                            client.log(" {} - {} ".format(str(man), str(msgText)))
                        else:
                            client.log(" {} - {} ".format(str(send), str(msgText)))
                            msg_dict[msg.id] = {"rider": msgText, "pelaku": man, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Connect_to["Timeline"] == True:
                      if msg.contentType == 16:
                          ret_ = "[ INFORMASI TIMELINE ]\n"
                          if msg.contentMetadata["serviceType"] == "GB":
                              contact = client.getContact(man).displayName
                              auth = "\nPenulis : {}".format(str(contact.displayName))
                          else:
                              auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                              ret_ += auth
                          if "stickerId" in msg.contentMetadata:
                              stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                              ret_ += stck
                          if "mediaOid" in msg.contentMetadata:
                              object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                              if msg.contentMetadata["mediaType"] == "V":
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                  ret_ += murl
                              else:
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                              ret_ += ourl
                          if "text" in msg.contentMetadata:
                              dia = client.getContact(man)
                              zx = ""
                              zxc = ""
                              zx2 = []
                              xpesan = 'Pengirim: '
                              ardian = str(dia.displayName)
                              pesan = ''
                              pesan2 = pesan+"@Priv8-L1ng\n"
                              xlen = str(len(zxc)+len(xpesan))
                              xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                              zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                              zx2.append(zx)
                              kata = "\n\nText Type : {}".format(str(msg.contentMetadata["text"]))
                              purl = "\n\nLink Post : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                              ret_ += purl
                              ret_ += kata
                              zxc += pesan2
                              pesan = xpesan + zxc + ret_ + ""
                              client.sendMessage(send, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              url = msg.contentMetadata["postEndUrl"]
                              client.likePost(url[25:58], url[66:], likeType=1001)
                              client.createComment(url[25:58], url[66:], Connect_to["comment"])

        if op.type == 65:
          if Connect_to['UnsendMessage'] == True:
              try:
                  you = op.param1
                  msg.id = op.param2
                  man = msg._from
                  if msg.id in msg_dict:
                    if msg_dict[msg.id]["pelaku"]:
                        pelaku = client.getContact(msg_dict[msg.id]["pelaku"])
                        nama = pelaku.displayName
                        dia = "Detect Pesan Terhapus\n"
                        dia += "\n1. Name : " + nama
                        dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                        dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                        client.priv8l1ng(send,man," Nah","\n\n" +str(dia))
              except:
                  client.sendMessage(you, "Return")

        if op.type in [25,26]:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 7:
                if Connect_to['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    client.priv8l1ng(send,man,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if op.type == 25:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 1:
              if myMID in Connect_to['Upfoto'] == True:
                if man in Owner:
                    path = cl.downloadObjectMsg(msg_id)
                    del Connect_to["Upfoto"][myMID]
                    client.updateProfilePicture(path)
                    client.priv8l1ng(send,man," Update Picture Success ","")
                    client.sendMessage(send,man," Now Upload Your Video Here ","")
                    a = client.downloadObjectMsg(msg.id)
                    client.updateProfileVideoPicture(a)
                    client.priv8l1ng(send,man," Success ","")
                    Connect_to['Upfoto'] = False

        if op.type == 25:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 1:
              if Connect_to['UpfotoGroup'] == True:
                #if man in Team or man in Connect_to["Admin"]:
                    path = client.downloadObjectMsg(msg.id)
                    client.updateGroupPicture(send, path)
                    client.priv8l1ng(send,man," Update Picture Grup Success ","")
                    Connect_to['UpfotoGroup'] = False

        if op.type == 5:
            if Connect_to["autoAdd"] == True:
                if (Connect_to["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Connect_to["ContactAdd"][op.param2] = True
                    usr = client.getContact(op.param2)
                    client.sendMessage(op.param1, "Haii {} " + str(Connect_to["PesanAdd"]).format(usr.displayName))
                    client.sendMessage(op.param1, None, contentMetadata={'mid':myMID}, contentType=13)

        if op.type == 5:
            if Connect_to['autoBlock'] == True:
                try:
                    usr = client.getContact(op.param2)
                    client.sendMessage(op.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    client.talk.blockContact(0, op.param1)
                    Connect_to["Blacklist"][op.param2] = True
                except Exception as e:
                	print (e)

        if op.type in [25,26]:
          if Connect_to['Contact'] == True:
              msg = op.message
              man = msg._from
              send = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = client.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = client.getProfileCoverURL(man)
                    except:
                        cover = ""
                    client.sendMessage(send,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = client.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = client.getProfileCoverURL(man)
                    except:
                        cover = ""
                    client.sendText(send,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if op.type == 25:
          if Connect_to['Invite'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            client.sendText(send, _name + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                client.findAndAddContactsByMid(target)
                                client.inviteIntoGroup(send,[target])
                                client.sendText(send,"Invite " + _name + "\nSUCCESS..")
                                Connect_to['Invite'] = False
                                break
                            except:             
                                 client.sendText(send, 'Contact error')
                                 Connect_to['Invite'] = False
                                 break

        if op.type == 25:
          if Connect_to['Steal'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = client.getContact(target)
                                client.sendText(send,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                client.sendImageWithURL(send,image)
                                cover = client.getProfileCoverURL(target)
                                client.sendImageWithURL(send, cover)
                                Connect_to['Steal'] = False
                                break                     
                            except:             
                                 client.sendText(send, 'Contact error')
                                 Connect_to['Steal'] = False
                                 break

        if op.type == 25:
          if Connect_to['KillOn'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in Team:
                                try:
                                    client.kickoutFromGroup(send, man,[target])
                                    Connect_to['KillOn'] = False
                                    break
                                except:             
                                     client.sendText(send, man, 'Target Not Found')
                                     Connect_to['KillOn'] = False
                                     break

        if op.type == 25:
          if Connect_to['Gift'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                client.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Connect_to['Gift'] = False
                                break
                            except:             
                                 client.sendText(send, 'Target Error')
                                 Connect_to['Gift'] = False
                                 break

        if op.type == 25:
          if Connect_to["Mic"] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                client.sendText(send,"Target ditambahkan!")
                                Connect_to['Mic'] = False
                                break
                            except:             
                                 client.sendText(send, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if op.type == 25:
          if Connect_to["MicDel"] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                client.sendText(send,"Target is Dellete!")
                                Connect_to['MicDel'] = False
                                break
                            except:             
                                 client.sendText(send, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if op.type == 25:
          if Connect_to['Copy'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                #if man in Team or man in Connect_to["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                client.cloneContactProfile(target)
                                client.sendText(send, "Copy Contact Success")
                                Connect_to['Copy'] = False
                                break
                            except:             
                                 client.sendText(send, "Contact Error")
                                 Connect_to['Copy'] = False
                                 break
                                 
        if op.type == 25:
          if Connect_to['likeOn'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 16:
                #if man in Team or man in Connect_to["Admin"]:
                    url = msg.contentMetadata["postEndUrl"]
                    client.likePost(url[25:58], url[66:], likeType=1005)
                    client.createComment(url[25:58], url[66:], Connect_to["comment"])
                    client.sendText(send,"Like Success")                     
                    Connect_to['likeOn'] = False

#======= AUTO TAG & CHAT BATAS SCRIP ========
        if op.type == 26:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 0 and man not in myMID and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Connect_to['AutoRespon'] == True:
                        contact = client.getContact(man)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Connect_to['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in myMID:
                                  client.priv8l1ng(send,man,"","" +str(ret_))
                                  break

        if op.type == 26:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 0 and man not in Team or man not in Connect_to["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Connect_to['KickRespon'] == True:
                        contact = client.getContact(man)
                        cName = contact.displayName
                        balas = [cName + "Dont Tag Me","Sorry Dont Tag Me"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in myMID:
                                  client.priv8l1ng(send,man,"","" +str(ret_))
                                  client.kickoutFromGroup(send,[man])
                                  break

        if op.type == 25:
          if Connect_to['SpamInvite'] == True:
            msg = op.message
            man = msg._from
            send = msg.to
            if msg.contentType == 13:
                if man in Team or man in Connect_to["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = client.getGroup(send)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            client.sendText(send, korban + " Sudah Berada Di Group Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                client.findAndAddContactsByMid(target)
                                client.createGroup("Priv8-L1ng",[target]) 
                                client.createGroup("Priv8-L1ng",[target]) 
                                client.createGroup("Priv8-L1ng",[target])
                                client.sendText(send,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Connect_to['SpamInvite'] = False
                            except:             
                                 client.sendText(send, 'Contact error')
                                 Connect_to['SpamInvite'] = False
                                 break



        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msgText = msg.text
            msg_id = msg.id
            send = msg.to           
            man = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = send
                elif msg.toType == 2:
                    to = send
                if msg.contentType == 0:
                    if Connect_to["autoRead"] == True:
                        client.sendChatChecked(0, msg_id)
                    elif msgText is None:
                        return
                    else:               
                        if msgText.lower() == '_PYTHON3_':
                            client.sendMessage(0, man)

                        elif msgText.lower() == "me":
                            #if man in Team or man in Connect_to["Admin"]:
                                client.sendMessage(send, None, contentMetadata={'mid': man}, contentType=13)
                                client.priv8l1ng(send,man," Hay","")

                        elif msgText.lower() == "owner":
                                client.sendMessage(msg.to,"~My Owner :)~") 
                                ma = ""
                                for i in contact1:
                                    ma = client.getContact(i)

                                    client.sendMessage(msg.to, man, None, contentMetadata={'mid': i}, contentType=13)

                        elif msgText.lower() == "help":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help))

                        elif msgText.lower() == "type1":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help2))

                        elif msgText.lower() == "type2":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help3))

                        elif msgText.lower() == "type3":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help4))

                        elif msgText.lower() == "type4":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help5))

                        elif msgText.lower() == "type5":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help6))

                        elif msgText.lower() == "note":
                            #if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help7))

                        elif msgText.lower() == "priv":
                            if man in Team or man in Connect_to["Admin"]:
                                 client.sendReplyMessage(msg_id,send, str(Help8))

                        elif msgText.lower() == ".":
                            if man in Team or man in Connect_to["Admin"]:
                                 creator.sendReplyMessage(msg_id,send, str(Help9))

                        elif msgText.lower() == "speed":
                            #if man in Team or man in Connect_to["Admin"]:
                                no = time.time()
                                client.sendReplyMessage(msg_id,send, "Check Speed...")
                                elapsed_time = time.time() - no
                                client.sendReplyMessage(msg_id,send, "%s" % (elapsed_time))

                        elif msgText.lower() == "rename":
                            if man in Team or man in Connect_to["Admin"]:
                                team1 = client.getContact(myMID).displayName
                                client.priv8l1ng(send,myMID," Ready On ","" + str(" ("+team1+")"))

                        elif msgText.lower() == "my team":
                            if man in Team or man in Connect_to["Admin"]:
                                msg = ""
                                zxr_ = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    msg += str(wa) + ". " +client.getContact(m_id).displayName + "\n"
                                for m_id in Connect_to["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    zxr_ += str(wi) + ". " +client.getContact(m_id).displayName + "\n"
                                client.sendText(send,"Team\n\nOwner:\n"+msg+"\nAdmin:\n"+zxr_+"\n( %s ) ZXR Team" %(str(len(Owner)+len(Connect_to["Admin"]))))                                

                        elif msgText.lower() == "leaveall":
                            if man in Team or man in Connect_to["Admin"]:
                                gid = client.getGroupIdsJoined()
                                for i in gid:
                                    client.leaveGroup(i)
                                    print ("Success Leave All group")

                        elif msgText in ["kick on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["KickOn"] = True
                                client.sendText(send,"Status:\n{''cancel'':0,''kick'':1}")
                        elif msgText in ["kick off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["KickOn"] = False
                                client.sendText(send,"Status:\n{''cancel'':0,''kick'':0}")

                        elif "selow" in msgText:
                            if man in Team or man in Connect_to["Admin"]:
                              if msg.toType == 2:
                                if Connect_to["KickOn"]:
                                    _name = msg.text.replace("selow","")
                                    gs = client.getGroup(send)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        client.sendText(send,"Target Not found.")
                                    else:
                                        for target in targets:
                                          if target not in Team and target not in Connect_to["Admin"]:
                                            try:
                                                klist=[client]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(send,[target])
                                            except Exception as error:
                                                client.sendText(send, str(error))

                        elif msgText.lower().startswith("like "):
                            if msg._from in Owner:
                              try:
                                  typel = [1001,1002,1003,1004,1005,1006]
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  a = client.getContact(u).mid
                                  s = client.getContact(u).displayName
                                  receiver = msg.to
                                  sender = msg._from
                                  hasil = client.getHomeProfile(a)
                                  st = hasil['result']['feeds']
                                  for i in range(len(st)):
                                      test = st[i]
                                      result = test['post']['postInfo']['postId']
                                      client.likePost(str(sender), str(result), likeType=random.choice(typel))
                                      client.createComment(str(sender), str(result), 'Autolike by X̡̱̻n͓͡o̹̦ͬo̼̍̕b̞̐͝\nhttp://line.me/ti/p/SGoaBN0jvC\n\nSupport by Team DFB Bot')
                                  client.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                              except Exception as e:
                                  client.sendMessage(receiver, str(e))

                        elif msgText.lower().startswith("spam "):
                            if man in Team or man in Connect_to["Admin"]:
                                txt = msgText.split(" ")
                                jmlh = int(txt[2])
                                teks = msgText.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           client.sendText(send, teks)
                                    else:
                                       client.sendText(send, "Maksimal 500 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        client.sendText(send, tulisan)
                                    else:
                                        client.sendText(send, "Maksimal 500 SpamTeks!")

                        elif msgText.lower().startswith("spamtag|"):
                            if man in Team or man in Connect_to["Admin"]:
                                proses = text.split("|")
                                strnum = text.replace(proses[0] + "|","")
                                num =  int(strnum)
                                Connect_to["limit"] = num
                                client.sendMessage(msg.to,"SpamTag Change To " +strnum)

                        elif msgText.lower().startswith("spamtag "):
                            if man in Team or man in Connect_to["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Connect_to["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                client.sendMessage(msg)
                                            except Exception as e:
                                                client.sendMessage(send, str(e))
                                    else:
                                        client.sendMessage(msg.to,"KEBANYAKAN GOBLOK!")

                        elif msgText.lower().startswith("gcall|"):
                          if man in Team or man in Connect_to["Admin"]:
                                proses = text.split("|")
                                strnum = text.replace(proses[0] + "|","")
                                num =  int(strnum)
                                Connect_to["limit"] = num
                                client.sendMessage(msg.to,"Call Group To " +strnum)

                        elif msgText.lower().startswith("gcall"):
                            if man in Team or man in Connect_to["Admin"]:
                             if msg.toType == 2:
                                group = client.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Connect_to["limit"])
                                client.sendMessage(msg.to, "Success to invite {} Group Call invitations".format(str(Connect_to["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        client.sendMessage(msg.to,str(e))
                                else:
                                    client.sendMessage(msg.to,"KEBANYAKAN BANGSAT!")


                        elif "gift10 " in msg.text:
                            #if man in Team or man in Connect_to["Admin"]:
                              msg.contentType = 13
                              nk0 = msg.text.replace("gift10 ","")
                              nk1 = nk0.lstrip()
                              nk2 = nk1.replace("@","")
                              nk3 = nk2.rstrip()
                              _name = nk3
                              gs = client.getGroup(msg.to)
                              targets = []
                              for s in gs.members:
                                  if _name in s.displayName:
                                     targets.append(s.mid)
                              if targets == []:
                                  sendMessage(msg.to,"user does not exist")
                                  pass
                              else:
                                  for target in targets:
                                       try:
                                           client.sendText(msg.to,_name + " Check Your Gift")
                                           msg.contentType = 9
                                           msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                           msg.to = target
                                           msg.text = None
                                           client.sendMessage(msg)
                                       except:
                                           msg.contentMetadata = {'mid': target}

                            	
                        elif msgText.lower().startswith("cekmid: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                ardian = msgText.replace("Cekmid: ","")
                                client.sendMessage(send, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = client.getContact(ardian)
                                ganteng = client.getProfileCoverURL(ardian)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    client.sendText(send,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    client.sendText(send,"Profile Picture " + contact.displayName)
                                    client.sendImageWithURL(send,image)
                                    client.sendText(send,"Cover Picture " + contact.displayName)
                                    client.sendImageWithURL(send,path)
                                except:
                                    pass

                        elif ("Banlock " in msgText):
                            if man in Team or man in Connect_to["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Connect_to["Blacklist"][target] = True
                                        client.sendText(send,"Succes Banned ")
                                    except:
                                        pass

                        elif msgText.lower() == "banlist":
                            if man in Team or man in Connect_to["Admin"]:
                                if Connect_to["Blacklist"] == {}:
                                    client.sendText(send,"Nothing in Blacklist")
                                else:
                                    mc = "Daftar Blacklist "
                                    num=1
                                    ragets = client.getContacts(Connect_to["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n Total %i Blacklist " % len(ragets)
                                    client.sendText(send, mc)

                        elif msgText.lower().startswith("contact ban"):
                            if man in Team or man in Connect_to["Admin"]:
                              if Connect_to["Blacklist"] == {}:
                                  client.sendText(send,"Tidak Ada Blacklist")
                              else:
                                  client.sendText(send,"Contact Blacklist")
                                  h = ""
                                  for i in Connect_to["Blacklist"]:
                                      h = client.getContact(i)
                                      client.sendMessage(send, None, contentMetadata={'mid': i}, contentType=13)

                        elif msgText.lower().startswith("clear ban"):
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Blacklist"] = {}
                                client.sendText(send,"Succes clear Blacklist is nothing??")
                                print ("Clear Ban")

                        elif msgText.lower() == 'link on':
                            #if man in Team or man in Connect_to["Admin"]:
                                if msg.toType == 2:
                                    group = client.getGroup(send)
                                    group.preventedJoinByTicket = False
                                    client.updateGroup(group)

                        elif msgText.lower() == 'link off':
                            #if man in Team or man in Connect_to["Admin"]:
                                if msg.toType == 2:
                                    group = client.getGroup(send)
                                    group.preventedJoinByTicket = True
                                    client.updateGroup(group)

                        elif msgText.lower() == 'gurl':
                          #if man in Team or man in Connect_to["Admin"]:
                            if msg.toType == 2:
                                grup = client.getGroup(send)
                                if grup.preventedJoinByTicket == False:
                                    set = client.reissueGroupTicket(send)
                                    client.sendMessage(send, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    client.sendMessage(send, "Ketik Link on Dulu kaka")

                        elif msgText.lower() == 'gcreator':
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    group = client.getGroup(send)
                                    GC = group.creator.mid
                                    client.sendMessage(send, None, contentMetadata={'mid': GC}, contentType=13)
                                    client.priv8l1ng(send,GC,"Group Creator","")
                                    contact = client.getContact(GC.mid)
                                except:
                                    W = group.members[0].mid
                                    client.sendMessage(send, None, contentMetadata={'mid': W}, contentType=13)
                                    client.priv8l1ng(send,W,"Group Creator","")

                        elif "invite gcreator" == msgText:
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    group = client.getGroup(send)
                                    GC = group.creator.mid
                                    client.sendMessage(send, None, contentMetadata={'mid': GC}, contentType=13)
                                    client.priv8l1ng(send,GC,"Group Creator","")
                                    client.findAndAddContactsByMid(GC)
                                    client.inviteIntoGroup(send,[GC])
                                    client.priv8l1ng(send,man,"Invite Done","")
                                    contact = client.getContact(GC.mid)
                                except:
                                    W = group.members[0].mid
                                    client.sendMessage(send, None, contentMetadata={'mid': W}, contentType=13)
                                    client.priv8l1ng(send,W,"Group Creator","")
                                    client.findAndAddContactsByMid(W)
                                    client.inviteIntoGroup(send,[W])
                                    client.priv8l1ng(send,man,"Invite Done","")

                        elif msgText.lower() == 'ginfo':
                            #if man in Team or man in Connect_to["Admin"]:
                                group = client.getGroup(send)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                zxr = "INFO GRUP"
                                zxr += "\nNama Group : {}".format(str(group.name))
                                zxr += "\nID Group :\n? {}".format(group.id)
                                zxr += "\nPembuat : {}".format(str(gCreator))
                                zxr += "\nJumlah Member : {}".format(str(len(group.members)))
                                zxr += "\nJumlah Pending : {}".format(gPending)
                                zxr += "\nGroup Qr : {}".format(gQr)
                                zxr += "\nGroup Ticket : {}".format(gTicket)
                                client.sendMessage(send, str(zxr))

                        elif msgText in ["memberlist"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                kontak = client.getGroup(send)
                                group = kontak.members
                                num=1
                                msgs="LIST MEMBER\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTOTAL MEMBER ( %i )" % len(group)
                                client.sendText(send, msgs)

                        elif msgText in ["Blocklist"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="My Blocked\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                client.sendText(send, msgs)

                        elif msgText in ["friendlist mid"]: 
                            if man in Team or man in Connect_to["Admin"]:
                                gruplist = client.getAllContactIds()
                                kontak = client.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                client.sendText(send, msgs)

                        elif msgText in ["friendlist"]: 
                            if man in Team or man in Connect_to["Admin"]:
                                gruplist = client.getAllContactIds()
                                kontak = client.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                client.sendText(send, msgs)

                        elif msgText in ["pendinglist"]:
                            if man in Team or man in Connect_to["Admin"]:
                                group = client.getGroup(to)
                                ret_ = "[ Pending List ]"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                   return client.sendMessage(to, "There is no pending")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n> {}. {}".format(str(no), str(pending.displayName))
                                        ret_ += "\n[ Total {} Pending]".format(str(len(group.invitee)))
                                        client.sendMessage(to, str(ret_))

                        elif msg.text in ["accept pending"]:
                            if man in Team or man in Connect_to["Admin"]:
                                gid = client.getGroupIdsInvited()
                                _list = ""
                                for i in gid:
                                    if i is not None:
                                        gids = client.getGroup(i)
                                        _list += gids.name
                                        client.acceptGroupInvitation(i)
                                    else:
                                        break
                                if gid is not None:
                                    client.sendText(msg.to,"Success Invited Member From Pending :\n" + _list)
                                else:
                                    client.sendText(msg.to,"There is no pending")  
 
                        elif "groupid" in msgText:
                            #if man in Team or man in Connect_to["Admin"]:
                                saya = msgText.replace('Grup id','')
                                gid = client.getGroup(send)
                                client.sendText(send, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif msgText.lower() == 'lurking on':
                            #if man in Team or man in Connect_to["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if send in Connect_to['readPoint']:
                                        try:
                                            del Connect_to['readPoint'][send]
                                            del Connect_to['readMember'][send]
                                            del Connect_to['readTime'][send]
                                        except:
                                            pass
                                        Connect_to['readPoint'][send] = msg.id
                                        Connect_to['readMember'][send] = ""
                                        Connect_to['readTime'][send] = datetime.now().strftime('%H:%M:%S')
                                        Connect_to['ROM'][send] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Connect_to, fp, sort_keys=True, indent=4)
                                            client.sendMessage(send,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][send]
                                        del read['readMember'][send]
                                        del read['readTime'][send]
                                    except:
                                        pass
                                    Connect_to['readPoint'][send] = msg.id
                                    Connect_to['readMember'][send] = ""
                                    Connect_to['readTime'][send] = datetime.now().strftime('%H:%M:%S')
                                    Connect_to['ROM'][send] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Connect_to, fp, sort_keys=True, indent=4)
                                        client.sendMessage(send, "Set reading point:\n" + readTime)
                                        
                        elif msgText.lower() == 'lurking off':
                            #if man in Team or man in Connect_to["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if send not in Connect_to['readPoint']:
                                    client.sendMessage(send,"Lurking already off..")
                                else:
                                    try:
                                            del Connect_to['readPoint'][send]
                                            del Connect_to['readMember'][send]
                                            del Connect_to['readTime'][send]
                                    except:
                                          pass
                                    client.sendMessage(send, "Delete reading point:\n" + readTime)
                
                        elif msgText.lower() == 'lurking reset':
                            #if man in Team or man in Connect_to["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if send in Connect_to["readPoint"]:
                                    try:
                                        Connect_to["readPoint"][send] = True
                                        Connect_to["readMember"][send] = {}
                                        Connect_to["readTime"][send] = readTime
                                        Connect_to["ROM"][send] = {}
                                    except:
                                        pass
                                    client.sendMessage(send, "Reset reading point:\n" + readTime)
                                else:
                                    client.sendMessage(send, "Lurking on dulu kaka..")
                                    
                        elif msgText.lower() == 'lurking read':
                            #if man in Team or man in Connect_to["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if send in Connect_to['readPoint']:
                                    if Connect_to["ROM"][send].items() == []:
                                        client.sendMessage(send,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Connect_to["ROM"][send].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@Priv8-L1ng\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        client.sendMessage(send, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(send,"Lurking on dulu kaka ??")

                        elif msgText.lower() == 'sider on':
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    del cctv['Point2'][send]
                                    del cctv['Point3'][send]
                                    del cctv['Point1'][send]
                                except:
                                    pass
                                cctv['Point2'][send] = msg.id
                                cctv['Point3'][send] = ""
                                cctv['Point1'][send]=True
                                client.sendText(send,"Sider Set to On..")

                        elif msgText.lower() == 'sider off':
                            #if man in Team or man in Connect_to["Admin"]:
                                if send in cctv['Point2']:
                                    cctv['Point1'][send]=False
                                    client.sendText(send, cctv['Point3'][send])
                                else:
                                    client.sendText(send, "Off not Going")

                        elif msgText.lower().startswith("mentionall"):
                            #if man in Team or man in Connect_to["Admin"]:
                                gname = client.getGroup(send)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@Nisaaa\n'
                                            atas = '\n Halo {} '.format(str(gname.name))
                                            atas += '\n Halo {} Members'.format(str(len(local)))
                                        client.sendMessage(send, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    client.sendMessage(send, str(error))

                        elif msgText.lower().startswith("tagall"):
                            members = []
                            if msg.toType == 1:
                                room = client.getCompactRoom(send)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = client.getCompactGroup(send)
                                members = [mem.mid for mem in group.members]
                            else:
                                return client.sendMessage(send, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                mentionMembers(send, members)

                        elif msgText in ["Welcome on"]:
                          #if man in Team or man in Connect_to["Admin"]:
                            if man in Team:
                                Connect_to['Welcome'] = True
                                client.sendText(send,"Cek Welcome Already ON")
                        elif msgText in ["Welcome off"]:
                          #if man in Team or man in Connect_to["Admin"]:
                            if man in Team:
                                Connect_to['Welcome'] = False
                                client.sendText(send,"Cek Welcome Already Off")

                        elif msgText.lower().startswith("changewelcome "):
                            if man in Team or man in Connect_to["Admin"]:
                                teks = msgText.split(" ")
                                data = msgText.replace(teks[0] + " ","")
                                try:
                                    Connect_to["WcText"] = data
                                    client.sendText(send,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    client.sendText(send,"Name Error")

                        elif msgText in ["Leave on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Leave'] = True
                                client.sendText(send,"Cek Leave Already ON")
                        elif msgText in ["Leave off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Leave'] = False
                                client.sendText(send,"Cek Leave Already Off")

                        elif msgText.lower().startswith("changeleave "):
                            if man in Team or man in Connect_to["Admin"]:
                                teks = msgText.split(" ")
                                data = msgText.replace(teks[0] + " ","")
                                try:
                                    Connect_to["LvText"] = data
                                    client.sendText(send,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    client.sendText(send,"Name Error")

                        elif msgText.lower() == "runtime":
                            if man in Team or man in Connect_to["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                client.sendText(send,"Connect to Team\nBot Active\n" + opn)                

                        elif msgText.lower().startswith("broadcast "):
                            #if man in Team or man in Connect_to["Admin"]:
                                teks = msgText.split(" ")
                                bc = msgText.replace(teks[0] + " ","")
                                gid = client.getGroupIdsJoined()
                                for i in gid:
                                    client.priv8l1ng(i,man," [Broadcast From ","]\n\n#################" + str("\n"+bc+"\n#################"))

                        elif msgText.lower().startswith("friendbroadcast "):
                            #if man in Team or man in Connect_to["Admin"]:
                                teks = msgText.split(" ")
                                bc = msgText.replace(teks[0] + " ","")
                                gid = client.getAllContactIds()
                                for i in gid:
                                    client.priv8l1ng(i,man," [Broadcast From ","]\n\n#################" + str("\n"+bc+"\n#################"))

                        elif msgText.lower().startswith("adminadd "):
                            if man in Team:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Connect_to["Admin"]:
                                        client.sendText(send, "Sudah Terdaftar di Admin")
                                    else:
                                        try:
                                            Connect_to["Admin"][target] = True
                                            client.sendText(send, "Terdaftar Menjadi Admin ")
                                        except Exception as e:
                                            client.sendText(send, str(error))

                        elif msgText.lower().startswith("admindell "):
                            if man in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Connect_to["Admin"]:
                                        client.sendText(send, "Belum Terdaftar di Admin")
                                    else:
                                        try:
                                            del Connect_to["Admin"][target]
                                            client.sendText(send, "Succes Dihapus menjadi admin")
                                        except Exception as e:
                                            client.sendText(send, str(error))

                        elif msgText.lower().startswith("changename: "):
                            if man in Team:
                                name = msgText.split(": ")
                                change = msgText.replace(name[0] + ": ","")
                                cll = client.getProfile()
                                cll.displayName = change
                                client.updateProfile(cll)
                                owner = "uc721ad1f11fb7e128453ba5a27424998"
                                client.priv8l1ng(send,owner," Update Name Success","\n Change to " + str(change))

                        elif msgText.lower().startswith("changebio: "):
                            if man in Team:
                                proses = msgText.split(": ")
                                teks = msgText.replace(proses[0] + ": ","")
                                no1 = client.getProfile()
                                no1.statusMessage = teks
                                client.updateProfile(no1)
                                client.sendText(send,"My Bio Change To : " + teks)

                        elif msgText.lower() == "rm -chat":
                            if man in Team or man in Connect_to["Admin"]:
                                try:
                                    client.removeAllMessages(op.param2)
                                    ginfo = client.getGroup(send)
                                    client.priv8l1ng(send,man," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    client.priv8l1ng(send,"Can't Acces, Just For Admin/Creator :)")
                                    pass

                        elif msgText.lower() == "rm -chatall":
                            if man in Team or man in Connect_to["Admin"]:
                                try:
                                    client.removeAllMessages(op.param2)
                                    creator.removeAllMessages(op.param2)
                                    ginfo = client.getGroup(send)
                                    client.priv8l1ng(send,man," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    client.priv8l1ng(send,"Can't Acces, Just For Admin/Creator :)")
                                    pass

                        elif msgText.lower() == 'restart':
                            if man in Team:
                                client.sendReplyMessage(msg_id,send, 'Reboot Your Program..')
                                print ("Reboot Your Program...")
                                restart_program()

                        elif msgText.lower() == 'logout':
                            if man in Team:
                                client.priv8l1ng(send,man," Akses Off","")
                                print ("BOT PUBLIK Off")
                                exit(1)

                        elif msgText.lower().startswith("kick "):
                            if man in Team or man in Connect_to["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in myMID:
                                        pass
                                    else:
                                        try:
                                            klist=[client]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(send,[target])
                                            Connect_to["Blacklist"][target] = True
                                        except Exception as e:
                                            client.sendText(send, str(error))

                        elif msgText.lower().startswith("vkick "):
                           if man in Team or man in Connect_to["Admin"]:
                             if msg.toType != 2: return client.sendMessage(to, 'Failed vultra kick member, use this command only on group chat')
                             if 'MENTION' in msg.contentMetadata.keys():
                                 mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                 for mention in mentions['MENTIONEES']:
                                     mid = mention['M']
                                     if mid == myMID:
                                         continue
                                 try:
                                     client.kickoutFromGroup(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.cancelGroupInvitation(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.kickoutFromGroup(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.cancelGroupInvitation(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.cancelGroupInvitation(to, [mid])
                                     client.findAndAddContactsByMid(mid)
                                     client.inviteIntoGroup(to, [mid])
                                     client.cancelGroupInvitation(to, [mid])
                                 except Exception as error:
                                     return client.sendMessage(to, 'Failed vultra kick members, the reason is `%s`' % error)
                                     time.sleep(0.8)
                                 client.sendMessage(to, 'Success vultra kick members, totals %i members' % len(mentions['MENTIONEES']))
                             else:
                                 client.sendMessage(to, 'Failed vultra kick member, please mention user you want to kick')

                        elif msgText.lower() == 'grouplist':
                            if man in Team or man in Connect_to["Admin"]:
                                groups = client.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                client.sendText(send, str(ret_))

                        elif msgText.lower().startswith("cancelall"):
                            if man in Team or man in Connect_to["Admin"]:
                                ginvited = client.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        client.rejectGroupInvitation(gid)
                                    client.sendMessage(send, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    client.sendMessage(send, "Nothing Invited")

                        elif msgText.lower() == 'status':
                            if man in Team or man in Connect_to["Admin"]:
                                try:
                                    hasil = "╭──────────────"
                                    if Connect_to["autoAdd"] == True: hasil += "\n•Auto Add ( on )"
                                    else: hasil += "\n•Auto Add ( off )"
                                    if Connect_to["autoJoin"] == True: hasil += "\n•Auto Join ( on )"
                                    else: hasil += "\n•Auto Join ( off )"
                                    if Connect_to["AutoReject"] == True: hasil += "\n•Auto Reject Room ( on )"
                                    else: hasil += "\n•Auto Reject Room ( off )"
                                    if Connect_to["AutojoinTicket"] == True: hasil += "\n•Auto Join Ticket ( on )"
                                    else: hasil += "\n•Auto Join Ticket ( off )"
                                    if Connect_to["autoRead"] == True: hasil += "\n•Auto Read ( on )"
                                    else: hasil += "\n•Auto Read ( off )"
                                    if Connect_to["AutoRespon"] == True: hasil += "\n•Detect Mention ( on )"
                                    else: hasil += "\n•Detect Mention ( off )"
                                    if Connect_to["KickRespon"] == True: hasil += "\n•Detect Mention ( on )"
                                    else: hasil += "\n•Detect Kick Mention ( off )"
                                    if Connect_to["Contact"] == True: hasil += "\n•Check Contact ( on )"
                                    else: hasil += "\n•Check Contact ( off )"
                                    if Connect_to["Timeline"] == True: hasil += "\n•Check Post Timeline ( on )"
                                    else: hasil += "\n•Check Post ( off )"
                                    if Connect_to["IDSticker"] == True: hasil += "\n•Check Sticker ( on )"
                                    else: hasil += "\n•Check Sticker ( off )"
                                    if Connect_to["UnsendMessage"] == True: hasil += "\n•Unsend Message ( on )"
                                    else: hasil += "\n•Unsend Message ( off )"
                                    if Connect_to["KickOn"] == True: hasil += "\n•Kick All Member ( on )"
                                    else: hasil += "\n•Kick All Member ( off )"
                                    if Connect_to["SpamInvite"] == True: hasil += "\n•Spam contact ( on )"
                                    else: hasil += "\n•Spam Contact ( off )"
                                    if Connect_to["likeOn"] == True: hasil += "\n•Auto Like Post ( on )"
                                    else: hasil += "\n•Auto Like Post ( off )"
                                    hasil += "\n╰──────────────"
                                    client.sendMessage(send, str(hasil))
                                except Exception as error:
                                    client.sendMessage(send, str(error))

                        elif msg.text in ["like post"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["likeOn"] = True
                                client.sendText(send,"Share your post that you want to like!")      

                        elif msgText in ["Unsend on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['UnsendMessage'] = True
                                client.sendText(send,"Cek UnsendMessage Set to on..")

                        elif msgText in ["cek sticker on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['IDSticker'] = True
                                client.sendText(send,"Cek sticker Set to on..")

                        elif msgText in ["Unsend off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['UnsendMessage'] = False
                                client.sendText(send,"Cek UnsendMessage Set to off..")

                        elif msgText in ["changeprofile on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Upfoto'] = True
                                client.sendText(send,man,"Send Pict For UpPict")

                        elif msgText in ["changeprofile off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Upfoto'] = False
                                client.sendText(send,man,"Send Pict Already Off")

                        elif msgText in ["changeprofilegroup on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['UpfotoGrup'] = True
                                client.sendText(send,"Send Pict For Change Foto Grup")
                        elif msgText in ["changeprofilegroup off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['UpfotoGrup'] = False
                                client.sendText(send,"Send Pict Already Off")

                        elif msgText in ["Timeline on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Timeline'] = True
                                client.sendText(send,"Cek Post Set to on..")
                        elif msgText in ["Timeline off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Timeline'] = False
                                client.sendText(send,"Cek Post Set to off..")

                        elif msgText in ["Autojoin on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['autoJoin'] = True
                                client.sendText(send,"Join Set To On..")
                        elif msgText in ["Autojoin off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['autoJoin'] = False
                                client.sendText(send,"Join Set To Off..")

                        elif msgText in ["Autoreject on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['AutoReject'] = True
                                client.sendText(msg.to,"Reject Set To On..")
                        elif msgText in ["Autoreject off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['AutoReject'] = False
                                client.sendText(msg.to,"Reject Set To Off..")

                        elif msgText in ["Admin:add-on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Adminadd"] = True
                                client.sendText(send,"Send Contact to added Admin..")
                        elif msgText in ["Admin:add-off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Adminadd"] = False
                                client.sendText(send,"Send Contact to added Admin in Off..")

                        elif msgText in ["Admin:del-on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["AdminDel"] = True
                                client.sendText(send,"Send Contact to Dellete Admin..")
                        elif msgText in ["Admin:del-off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["AdminDel"] = False
                                client.sendText(send,"Send Contact to Dellete Admin in Off..")

                        elif msgText in ["Gift:on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Gift"] = True
                                client.sendText(send,"Send Contact to send Gift..")
                        elif msgText in ["Gift:off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Gift"] = False
                                client.sendText(send,"Send Contact to Gift in Off..")

                        elif msgText in ["Spaminvite on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["SpamInvite"] = True
                                client.sendText(send,"Send Contact to spam grup..")
                        elif msgText in ["Spaminvite off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["Gift"] = False
                                client.sendText(send,"Send Contact to send grup Off..")

                        elif msgText in ["Auto jointicket on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to["AutojoinTicket"] = True
                                client.sendText(send,"Join Ticket Set To On")
                        elif msgText in ["Auto jointicket off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to["AutojoinTicket"] = False
                                client.sendText(send,"Join Ticket Set To Off")
                        elif '/ti/g/' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Connect_to["AutojoinTicket"] == True:
                                        group=client.findGroupByTicket(ticket_id)
                                        client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        client.sendText(send,"Success Masuk %s" % str(group.name))

                        elif msgText in ["Copy on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Copy'] = True
                                client.sendText(send,"Send Contact For Copy User")
                        elif msgText in ["Copy off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Copy'] = False
                                client.sendText(send,"Send Contact Already Off")

                        elif msgText.lower().startswith("clone "):
                            #if man in Team or man in Connect_to["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendMessage(send, "Berhasil mengclone profile {}".format(contact.displayName))

                        elif msgText.lower() == 'comeback':
                            if man in Team or man in Connect_to["Admin"]:
                                try:
                                    clientProfiledisplayName = str(myProfile["displayName"])
                                    clientProfilestatusMessage = str(myProfile["statusMessage"])
                                    clientProfilepictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfilepictureStatus)
                                    client.updateProfile(clProfile)
                                    client.sendMessage(send, "Already back to my account")
                                except:
                                    client.sendMessage(send, "Error Come Back")

                        elif msgText in ["Steal on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Steal'] = True
                                client.sendText(send,"Send Contact For Cek Contact")
                        elif msgText in ["Steal off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Steal'] = False
                                client.sendText(send,"Send Contact Already Off")

                        elif msgText in ["Contact on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Contact'] = True
                                client.sendText(send,"Contact Set to on")
                        elif msgText in ["Contact off"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Contact'] = False
                                client.sendText(send,"Contact Already Off")

                        elif msgText in ["Invite on"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Invite'] = True
                                client.sendText(send,"Send Contact For Invite Target")
                        elif msgText in ["Invite off"]:
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to['Invite'] = False
                                client.sendText(send,"Send Contact Set Off")

                        elif msgText.lower() == 'kill on':
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["KillOn"] = True
                                client.sendMessage(man, "SendContact For Kick Taget")
                        elif msgText.lower() == 'kill off':
                            if man in Team or man in Connect_to["Admin"]:
                                Connect_to["KillOn"] = False
                                client.sendMessage(man, "SendContact For Kick Taget in Off")

                        elif msgText in ["Mic:add-on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Target["Mic"] = True
                                client.sendText(send,"Send Contact To Clone Message User")
                        elif msgText in ["Mic:del-on"]:
                            #if man in Team or man in Connect_to["Admin"]:
                                Target["MicDel"] = True
                                client.sendText(send,"Send Contact Dellete Clone Message User")
                        elif msgText.lower().startswith("mimic "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                mic = msgText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        client.sendText(send,"Mimic Set to on")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        client.sendText(send,"Mimic Message off")

                        elif msgText.lower() == 'mimiclist':
                            #if man in Team or man in Connect_to["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    client.sendText(send,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+client.getContact(mi_d).displayName
                                    client.sendText(send,mc + "\nFinish")

                        elif msgText.lower() == 'abort':
                            if man in Team or man in Connect_to["Admin"]:
                                try:
                                    Connect_to['Mic'] = False
                                    Connect_to['MicDel'] = False
                                    Connect_to['Gift'] = False
                                    Connect_to['Steal'] = False
                                    Connect_to['Invite'] = False
                                    Connect_to['Contact'] = False
                                    Connect_to['Copy'] = False
                                    Connect_to['autoJoin'] = False
                                    Connect_to['autoAdd'] = False
                                    Connect_to['AutojoinTicket'] = False
                                    Connect_to['UnsendMessage'] = False
                                    Connect_to['AutoReject'] = False
                                    Connect_to['Timeline'] = False
                                    Connect_to['Upfoto'] = False
                                    Connect_to['UpfotoGrup'] = False
                                    Connect_to['Adminadd'] = False
                                    Connect_to['AdminDel'] = False
                                    Connect_to['Welcome'] = False
                                    Connect_to['Leave'] = False
                                    Connect_to['Ban'] = False
                                    Connect_to['Unban'] = False
                                    Connect_to['KillOn'] = False
                                    Connect_to['KickOn'] = False
                                    Connect_to['SpamInvite'] = False
                                    Connect_to['IDSticker'] = False
                                    Connect_to['likeOn'] = False
                                    client.sendText(send,"Abort All Command.")
                                except Exception as e:
                                    client.sendText(send, str(error))

                        elif msgText.lower().startswith("my name"):
                            #if man in Team or man in Connect_to["Admin"]:
                                contact = client.getContact(man)
                                client.sendMessage(send, "MyName : {}".format(contact.displayName))
                        elif msgText.lower().startswith("my bio"):
                            #if man in Team or man in Connect_to["Admin"]:
                                contact = client.getContact(man)
                                client.sendMessage(send, "My Status : \n{}".format(contact.statusMessage))
                        elif msgText.lower().startswith("my picture"):
                            #if man in Team or man in Connect_to["Admin"]:
                                contact = client.getContact(man)
                                client.sendImageWithURL(send,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif msgText.lower().startswith("my video"):
                            #if man in Team or man in Connect_to["Admin"]:
                                contact = client.getContact(man)
                                client.sendVideoWithURL(send,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif msgText.lower().startswith("my cover"):
                            #if man in Team or man in Connect_to["Admin"]:
                                channel = client.getProfileCoverURL(man)          
                                path = str(channel)
                                client.sendImageWithURL(send, path)

                        elif msgText.lower().startswith("stealname "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = client.getContact(ls)
                                    client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                        elif msgText.lower().startswith("stealbio "):
                          #if man in Team or man in Connect_to["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = client.getContact(ls)
                                    client.sendMessage(send, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                        elif msgText.lower().startswith("stealpict "):
                          #if man in Team or man in Connect_to["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = client.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                    client.sendImageWithURL(send, str(path))
                        elif msgText.lower().startswith("stealvideo "):
                          #if man in Team or man in Connect_to["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = client.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    client.sendVideoWithURL(send, str(path))
                        elif msgText.lower().startswith("stealcover "):
                          #if man in Team or man in Connect_to["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        channel = client.getProfileCoverURL(ls)
                                        path = str(channel)
                                        client.sendImageWithURL(send, str(path))

                        elif msgText.lower().startswith("myprofile"):
                            contact = client.getContact(man)
                            cover = client.getProfileCoverURL(man)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : @!"
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Support By HTB Public ]"
                            client.sendImageWithURL(send, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            client.sendMention(send, result, [man])

                        elif msgText.lower().startswith("mid "):
                          #if man in Team or man in Connect_to["Admin"]:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = client.getContact(key1)
                               client.sendReplyMessage(msg_id, send, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               client.sendReplyMessage(msg_id, send, None, contentMetadata={'mid': key1}, contentType=13)

                        elif msgText.lower().startswith("info "):
                          #if man in Team or man in Connect_to["Admin"]:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = client.getContact(key1)
                               client.sendMessage(send, "»» Nama : "+str(mi.displayName)+"\n»» Mid : " +key1+"\n»» Status Message"+str(mi.statusMessage))
                               client.sendMessage(send, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(client.getContact(key1)):
                                   client.sendVideoWithURL(send, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   client.sendImageWithURL(send, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif msgText.lower().startswith("randomgrup: "):
                            #if man in Team or man in Connect_to["Admin"]:
                              if msg.toType == 2:
                                  strnum = msgText.replace("randomgrup: ","")
                                  source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                                  try:
                                      num = int(strnum)
                                      group = client.getGroup(send)
                                      for var in range(0,num):
                                          name = "".join([random.choice(source_str) for x in range(10)])
                                          time.sleep(0.01)
                                          group.name = name
                                          client.updateGroup(group)
                                  except Exception as e:
                                      client.sendText(send, str(e))

                        elif msgText.lower() == 'announce':
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    gett = client.getChatRoomAnnouncements(send)
                                    for a in gett:
                                        aa = client.getContact(a.creatorMid).displayName
                                        bb = a.contents
                                        cc = bb.link
                                        textt = bb.text
                                        client.sendText(send, 'Pemberitahuan Grup\n\nLink: ' + str(cc) + '\nPenulis: ' + str(aa) + '\nTeksnya: ' + str(textt))
                                        break
                                except Exception as e:
                                    client.sendText(send, "Pemberitahuan Grup Tidak Ditemukan")


                        elif msgText.lower().startswith("berita"):
                              #if man in Team or man in Connect_to["Admin"]:
                                  msg=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=msg.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  client.sendText(send, str(hasil))
                                  client.sendImageWithURL(send, str(path))

                        elif "sslink|" in msgText:
                            #if man in Team or man in Connect_to["Admin"]:
                                 website = msg.text.replace("sslink|","")
                                 response = requests.get("https://rest.farzain.com/api/webcheck.php?q="+website+"&apikey=tjfoPmtksGg222NdQdZypSqEV")
                                 data = response.json()
                                 pictweb = data['result']
                                 client.sendImageWithURL(send, pictweb)

                        elif msgText.lower().startswith("maps "):
                            #if man in Team or man in Connect_to["Admin"]:
                                proses = text.split(" ")
                                location = text.replace(proses[0] + " ","")
                                with requests.session() as web:
                                    web.headers["man-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    msg = web.get("https://rest.farzain.com/api/lokasi.php?id={}&apikey=0gcLIXSni40ViUu4tMqSh7kWS".format(urllib.parse.quote(location)))
                                    data = msg.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    client.sendText(send,str(ret_))

                        elif msgText.lower().startswith("cekcuaca: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                weather = msgText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["man-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    msg = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = msg.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    client.sendText(send, str(ret_))

                        elif msgText.lower().startswith("jadwalshalat: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                shalat = msgText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["man-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    msg = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = msg.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    client.sendText(send, str(ret_))

                        elif msgText.lower().startswith("mp4 "):
                          #if man in Team or man in Connect_to["Admin"]:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n• Author : ' + str(vid.author)
                                    durasi = '\n• Duration : ' + str(vid.duration)
                                    suka = '\n• Likes : ' + str(vid.likes)
                                    rating = '\n• Rating : ' + str(vid.rating)
                                    deskripsi = '\n• Deskripsi : ' + str(vid.description)
                                client.sendVideoWithURL(msg.to, me)
                                client.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                client.sendText(msg.to,str(e))

                        elif msgText.lower().startswith("musik|"):
                          #if man in Team or man in Connect_to["Admin"]:
                            try:
                                search = msg.text.replace("musik|","")
                                r = requests.get("https://rest.farzain.com/api/joox.php?apikey=tjfoPmtksGg222NdQdZypSqEV&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                client.sendImageWithURL(msg.to, str(data["gambar"]))
                                client.sendMessage(msg.to, str(hasil))
                                client.sendAudioWithURL(msg.to, str(audio["mp3"]))
                            except Exception as e:
                                client.sendMessage(msg.to, "Selamat Menikmati ")
                        elif "idline " in msgText:
                            #if man in Team or man in Connect_to["Admin"]:
                                 msgg = msgText.replace('idline ','')
                                 conn = client.findContactsByUserid(msgg)
                                 if True:
                                    client.sendText(send,"Link User : https://line.me/ti/p/~" + msgg)
                                    client.sendMessage(send, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = client.getContact(conn.mid)
                                    client.sendImageWithURL(send,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = client.getProfileCoverURL(conn.mid)
                                    client.sendImageWithURL(send, cover)
                                    client.priv8l1ng(send,conn.mid,"Tag User\n","")

                        elif 'say-id: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    isi = msgText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(send, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'say-en: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    isi = msgText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(send, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'say-jp: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    isi = msgText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(send, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'say-ar: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    isi = msgText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(send, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'say-ko: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    isi = msgText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(send, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'apakah: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(send, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif 'kapan: ' in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(send, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(send, str(e))

                        elif "wikipedia: " in msgText:
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    wiki = msgText.lower().replace("Wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    client.sendText(send, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        client.sendText(send, pesan)
                                    except Exception as e:
                                        client.sendText(send, str(e))

                        elif msgText.lower() == 'kalender':
                            #if man in Team or man in Connect_to["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                client.sendMessage(send, readTime)

                        elif "image " in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                separate = msg.text.split(" ")
                                search = msg.text.replace(separate[0] + " ","")
                                with requests.session() as web:
                                    web.headers["man-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = web.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=0gcLIXSni40ViUu4tMqSh7kWS".format(urllib.parse.quote(search)))
                                    data = response.json()
                                    pictweb = data['result']
                                    client.sendImageWithURL(send, pictweb)                              

                        elif "youtube|" in msgText.lower():
                            #if man in Team or man in Connect_to["Admin"]:
                                try:
                                    query = msgText.replace("youtube|", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(send, x)
                                except Exception as e:
                                    client.sendText(send, str(e))


                        elif msgText.lower().startswith("indonesian: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                client.sendMessage(send, "Translator Indonesian\n\n" + str(text))

                        elif msgText.lower().startswith("english: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                client.sendMessage(send, "Translator English\n\n" + str(text))

                        elif msgText.lower().startswith("korea: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                    sep = msgText.split(" ")
                                    isi = msgText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    client.sendMessage(send, "Translator Korea\n\n" + str(text))

                        elif msgText.lower().startswith("japan: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                client.sendMessage(send, "Translator Japan\n\n" + str(text))

                        elif msgText.lower().startswith("thailand: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                client.sendMessage(send, "Translator Thailand\n\n" + str(text))

                        elif msgText.lower().startswith("arab: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                client.sendMessage(send, "Translator Saudi Arabia\n\n" + str(text))

                        elif msgText.lower().startswith("malaysia: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                client.sendMessage(send, "Translator Malaysia\n\n" + str(text))

                        elif msgText.lower().startswith("jawa: "):
                            #if man in Team or man in Connect_to["Admin"]:
                                sep = msgText.split(" ")
                                isi = msgText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                client.sendMessage(send, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)



while True:
    try:
        Operation = poll.singleTrace(count=50)
        if Operation is not None:
            for op in Operation:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=LINE_OP_TYPE, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)

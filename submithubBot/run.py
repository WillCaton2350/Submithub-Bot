from Bot.main import webDriver
from Bot.JointFunction.login_auth import webDriverLogin
from Bot.JointFunction.song_Submission import webDriverSub
from Bot.JointFunction.songSelector import webDriverSelect
from Bot.JointFunction.artist_Info import webDriverArtist
from Bot.JointFunction.playlistSubs import webDriverPList
from Bot.JointFunction.artistSound import webDriverSound
from Bot.JointFunction.payment_auth import webDriverPayment

if __name__ == "__main__":
    func = webDriver()
    funct = webDriverLogin()
    functi = webDriverSub()
    functio = webDriverSelect()
    funcs = webDriverArtist()
    functs = webDriverPList()
    functis = webDriverSound()
    functios = webDriverPayment()
    func.startDriver()
    func.Browser()
    funct.login()
    functi.submitSong()
    functio.scrollView()
    funcs.artistInfo()
    functs.Playlist_submission()
    functis.Sound_Alike()
    functios.paymentAuth()
    func.close()
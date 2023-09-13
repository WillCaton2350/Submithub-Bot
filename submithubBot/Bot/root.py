from main import webDriver


if __name__ == "__main__":
    func = webDriver()
    func.startDriver()
    func.Browser()
    func.login()
    func.submitSong()
    func.scrollView()
    func.artistInfo()
    func.Playlist_submission()
    func.Sound_Alike()
    func.close()
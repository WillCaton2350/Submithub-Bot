from main import webDriver

if __name__ == "__main__":
    func = webDriver()
    func.start_driver()
    func.browser()
    func.login()
    func.submit_song()
    func.scroll_view()
    func.artist_info()
    func.playlist_submission()
    func.sound_a_like()
    func.close_driver()
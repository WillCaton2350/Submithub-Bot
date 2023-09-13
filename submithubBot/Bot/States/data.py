geckoDriverPath = '/Users/administrator/Desktop/Projects/SeleniumProjects/submithubBot/Bot/Driver/geckodriver'
loginBtn = '/html/body/div[2]/div/header/div/div/nav/div[2]/ul[1]/li[2]/div'
login_SubmitBtn = '/html/body/div[2]/div/header/div/div/nav/div[2]/div[1]/div/form/div[3]/button'
usernameField = '//*[@id="usernameOrEmail"]'
passwordField = '//*[@id="password"]'
url = "https://www.submithub.com/"

submitSongBtn = '/html/body/div[2]/div/div[1]/main/div[1]/div[1]/div/div/div/div/div/a'
song_link = '//*[@id="paste-source"]'
soundcloudWill = 'https://soundcloud.com/willcatonjr/mirror'
soundcloud = 'https://soundcloud.com/johnnyyukon/whatever-you-want'
spotify = ''
applemusic = ''

is_not_released = '//*[@id="private"]'
is_released = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/form/div[1]/div[1]/label[1]'
songReleased_Text = 'div.mrg-bottom-50:nth-child(1) > h5:nth-child(1) > span:nth-child(1)'
release_date = '//*[@id="datepicker"]'
date = 'November 13, 2023 12:00 AM'
date_container = []
premium_credits = '//*[@id="premium-credits"]/div[3]'
standardCreditsOption = 'div.btn.deep-purple.lighten-2'

artistName = 'KULUSER BAKER'
featureName = 'GUEANU VOY'
newArtist = '/html/body/div[2]/div/div[1]/main/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/label[1]'
save_artist_Btn = '//*[@id="save-similar-artists"]'
add_Genre = '//*[@id="choose-a-genre-popup"]'
close_genre_Btn = 'div.modal-action.btn.teal.lighten-2'
genre_Select = '/html/body/div[2]/div/div[1]/main/div[1]/div[4]/div[1]/div/div[2]/label[1]'
genre_input = '/html/body/div[2]/div/div[1]/main/div[1]/div[4]/div[1]/div/div[1]/div[1]'

newFeaturedArtist = '//*[@id="submit-container"]/form/div[2]/div[3]/div[4]/label[1]'
select_Country = '/html/body/div[2]/div/div[1]/main/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div/div/div/select'
select_Country2 = '//*[@id="additional_artist_1-country"]/select'
next_btn = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/form/div[1]/div[3]/div[2]'
nextBtn = '//*[@id="submit-container"]/form/div[2]/div[7]/div[2]'
artistNameField = '//*[@id="artistId"]'
curatorDashboard = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[1]'

featuredArtistsBtn = '/html/body/div[2]/div/div[1]/main/div[1]/div/div[1]/form/div[2]/div[3]/div'
featuredArtistsBtn2 = '//*[@id="submit-container"]/form/div[2]/div[3]/div[4]/label[2]'
featuredArtistsBtn3 = '/html/body/div[2]/div/div[1]/main/div[1]/div/div[1]/form/div[2]/div[3]/div[4]/label'
notA_newArtist = '//*[@id="submit-container"]/form/div[2]/div[2]/div[3]/label[1]'
next_Xpath = '//div[@class="right"]/div[@class="left btn teal lighten-2"]'
small_grey_text='/html/body/div[2]/div/div[1]/main/div[1]/div/div[1]/form/div[2]/div[3]/div[4]/label/span/div'

soundcloud_container = '/html/body/div/div[1]/div'
song_title_Field = '//*[@id="2"]'
song_title = 'SongTitle'
additional_Email_Confirmation = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[4]/div[1]/div[2]/label'
next_Btn_Xpath = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[4]/div[3]'
featuredArtistNameField = '//*[@id="additional_artist_1"]'
first_Curator = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/div[2]/label'
submit_toPlaylist = '//*[@id="complete-submission"]'
US = 'United States'
UK = 'United Kingdom'

similar_Hiphop_Artist_list = ['Drake',"Young Thug","MadeinTYO","Trippie Redd",
                              "T-Pain","Blxst","Yeat","Wale","A$AP Ferg",
                              "Travis Scott","Future","DaBaby","Lil Baby",
                              "Ty Dolla $ign","Schoolboy Q","Metro Boomin", 
                              "Reo Cragun","Migos","Blueface","Gunna"
                              ]
genre_List = ["Hip Hop","Rnb","Rap"]
genreType = 'Rap'
cardID = 'credit-card-number'
similar_artists = '//*[@id="spotify-artist-search"]'
add_ArtistBtn = '//*[@id="similar-search"]/div[3]/div[1]/div/div[3]'
paypal_Btn = 'div.paypal-button-row.paypal-button-number-0.paypal-button-layout-horizontal.paypal-button-shape-rect.paypal-button-number-single.paypal-button-env-production.paypal-button-color-gold.paypal-button-text-color-black.paypal-logo-color-blue'

moods_Opts='/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div[3]/div[1]/div[7]/div[2]/label[12]' 
next_payment='/html/body/div[2]/div/div[2]/div/div/div[3]'
next_payment_2 = '/html/body/div[2]/div/div[2]/div/div/div/div/form/div[4]/div[2]'
company_name_inputField = '//*[@id="1"]'
company_Name = 'AutoPlay LLC'
confirmPaymentBtn = '/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]'
paypal_Opt='/html/body/div[2]/div/div[2]/div/div/div/div/form/div[3]/label[2]'
artistSearch = '//*[@id="spotify-artist-search"]'

mainArtistOption = 'label.mrg-bottom-10:nth-child(3)'
lyrics_Option = '//*[@id="submit-container"]/form/div[3]/div[3]/div/div[1]/label[1]'
lyrics_Lang = '//*[@id="submit-container"]/form/div[3]/div[3]/div/div[2]/div[2]/label[4]'
explicit_Lyrics = '//*[@id="submit-container"]/form/div[3]/div[3]/div/div[2]/div[5]/div[2]/label[1]'
no_explicit_Lyrics = ''
no_clean_Version = '//*[@id="submit-container"]/form/div[3]/div[3]/div/div[3]/label[2]'
yes_clean_Version = ''
submit_A_SONG_TITLE = 'h1.teal-text'

cardNumInput='body > form:nth-child(3)'
cardNum='0000111122223333'
cvv_Input = '//*[@id="cvv"]'
CVV = '123'
exp_Date_Input = '//*[@id="expiration"]'
expDate = '01/01/2029'
zipCodeInput = '//*[@id="postal-code"]'
zipCode = '22010'

submitASong_sidebar_Btn = '//*[@id="sidebar"]/a[1]'
insert_Lyrics_textArea = '//*[@id="paste-lyrics"]'
finish_Upload = '//*[@id="submit-container"]/form/div[3]/button'
submit_toCurators = '//*[@id="submit-wrapper"]/div/div[1]/div[1]'
submit_toCurators_btn2 = '//*[@id="main-content"]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]'
lyrics_Text = """
So I just came out the booth to goddamn, to hear this
To hear this shit right here? And my niggas, niggas just sayin'
"Bruh I just told 'em the same shit"
The niggas just told these girls that he do it all by himself
It's crazy, cray-cray, I did though, you know what I'm sayin'?
With a golden shovel, iced out AP, plus a Rollie bezel on another level
I say bitch what is you thinkin', we Arthur Blankin'
Bitch ass on me and I got rank and I'm steady rankin'
Better stop listenin' to these hoes 'fore you start shrinkin'
I know I'm a blood, I'm a gang banger
I know where the bitch but I'm still singin'
Mothafuck the rest, they ain't really bangin'
I got the real hitters with me and they dangerous
You can't find 'em on no camera but they no namin'
Washin' powder bae on Tide, I've been up all night
Me and bae Bonnie Clyde, everything we do right
Love her vibe, love her vibe, she make me feel so nice
She 100, the first day we met she let me fuck all night
Ah-ah-ah, work
Do the work baby do the work
Tonight baby do the work baby do the work
Tonight I wanna chill all you gotta do is Perc
If you want it you gotta earn it
You gotta earn-earn-earn it
If you want it bae you gotta earn it
Alright, earn-earn-earn it, aye
I can tell that you want it baby, I can tell that you need it
I can tell that you suckin', fuckin', I can tell you a demon
I can tell you a Victoria baby, I can keep your secret
I'mma show you how to win without cheatin', I'mma show you how to beat it
Drop top in a RR with a big tall demon
I'mma let you defeat me, I'mma lead you to victory
Like shoutout to Stevie but these niggas not seein' me
I'm a big dinosaur B and these niggas not beatin' me
Aye, I'm scared to trust you, I'm scared you'll trick me
I done drive by in a foreign car but they're still tryna eat me
Put 60, 000 on my mama ring and it ain't even come out of Tiffany's
I can tell you how to get the money but you just gotta listen to me
Ah-ah-ah, work
Do the work baby do the work
Tonight baby do the work baby do the work
Tonight I wanna chill all you gotta do is Perc
If you want it you gotta earn it
You gotta earn-earn-earn it
If you want it bae you gotta earn it
Alright, earn-earn-earn it, aye
I picked my diamonds out a honey tree
I done made a couple millions off of BET
I got gangster bitch that ride and they gon' clap for me
I just signed a deal with Kevin baby clap for me
Won't catch me without hundreds on me
G check with I pull up on 'em
Peep that with my little homies
I see all these little clonies (Who?)
I see you lookin' homie
Apple Watch with them boogers on it
Turn down, upside, right baby girl like I'm cookin' on ya
I got 70, 000 for my last 30 shows (Do the math)
I done spend a half a million for my family though
I think it's time to take my homies and ride on a boat
Show them a good time 'cause I know they'll do that for me, oh
Ah-ah-ah, work
Tonight baby got to work, work, work
Work, work, work
You gotta work, work, work, work, you gotta work
If you want it bae you gotta earn it
You gotta earn-earn-earn it
If you wanna earn it
You gotta earn-earn-earn it
Build a bridge, you better not burn it, aye
Better be the number one concern with, aye
I got big dogs and they German, aye
Aye, aye, aye, aye
"""
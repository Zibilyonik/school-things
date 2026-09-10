##Music Player Summative

playlist=[]
history=[]

while True:
    print("1. Add song")
    print("2. Play next song")
    print("3. View song year")
    print("4. Play previous song")
    print("5. View status of songs")
    print("0. Quit")
    choice=input("Choose from the above: ")

    if choice=="1":
        song=input("Which song you want to add?: ")
        year=input("Year of the song: ")
        details=[song,year]
        playlist.append(details)
        print(f"Added {song} to queue.")
        print(playlist)

    elif choice=="2":
        if len(playlist)==0:
            print("No songs in queue.")
        else:
            x=playlist[0]
            playlist.pop(0)
            history.append(x)
            song=x[0]
            print(f"Now Playing song : {song}")

    elif choice=="3":
        if len(history)==0:
            print("No songs is playing.")
        else:
            play_year=history[-1][1]
            print(f"The song was released in {play_year}")
        
    elif choice=="4":
        if len(history)==0:
            print("No History available.")
        else:
            back_song=history.pop(-1)
            playlist.insert(0,back_song)
            only_name=back_song[0]
            print(f"Rewinding to: {only_name}")

    elif choice=="5":
    
        print(f"Your history playlist looks like this:")
        if len(history)==0:
            print("No songs here")
        else:
            for x in history:
                y=history.index(x)
                xname=history[y][0]
                print(xname)
                
        print(f"Your playlist of songs looks like this:")
        if len(playlist)==0:
            print("No songs here")
        else:
            for x in playlist:
                y=playlist.index(x)
                yname=playlist[y][0]
                print(yname)

    elif choice=="0":
        print("Quitting")
        break
    
    else: 
        print("Invalid command")
        break
        








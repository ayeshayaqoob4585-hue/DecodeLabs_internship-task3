# AI Song Recommendation System

import random

songs = [
    {"name":"Perfect","artist":"Ed Sheeran","genre":"Romantic","language":"English","mood":"Relaxed","rating":5},
    {"name":"Shape of You","artist":"Ed Sheeran","genre":"Pop","language":"English","mood":"Happy","rating":5},
    {"name":"Believer","artist":"Imagine Dragons","genre":"Rock","language":"English","mood":"Energetic","rating":5},
    {"name":"Thunder","artist":"Imagine Dragons","genre":"Rock","language":"English","mood":"Energetic","rating":4},
    {"name":"Radioactive","artist":"Imagine Dragons","genre":"Rock","language":"English","mood":"Sad","rating":4},
    {"name":"Blinding Lights","artist":"The Weeknd","genre":"Pop","language":"English","mood":"Energetic","rating":5},
    {"name":"Levitating","artist":"Dua Lipa","genre":"Pop","language":"English","mood":"Happy","rating":4},
    {"name":"Calm Down","artist":"Rema","genre":"Pop","language":"English","mood":"Relaxed","rating":5},
    {"name":"Night Changes","artist":"One Direction","genre":"Pop","language":"English","mood":"Relaxed","rating":5},
    {"name":"Tum Hi Ho","artist":"Arijit Singh","genre":"Romantic","language":"Hindi","mood":"Sad","rating":5},
    {"name":"Kesariya","artist":"Arijit Singh","genre":"Romantic","language":"Hindi","mood":"Happy","rating":5},
    {"name":"Apna Bana Le","artist":"Arijit Singh","genre":"Romantic","language":"Hindi","mood":"Relaxed","rating":5},
]

while True:
    print("\n" + "="*50)
    print("AI SONG RECOMMENDATION SYSTEM")
    print("="*50)
    print("1. Recommend Songs")
    print("2. View All Songs")
    print("3. Search Song")
    print("4. Top Rated Songs")
    print("5. Filter by Artist")
    print("6. Surprise Me")
    print("7. Exit")
    choice=input("Enter choice: ").strip()

    if choice=="1":
        g=input("Genre (Pop/Rock/Romantic): ").capitalize()
        m=input("Mood (Happy/Sad/Energetic/Relaxed): ").capitalize()
        l=input("Language (English/Hindi): ").capitalize()
        found=False
        print("\nRecommendations:\n"+"-"*40)
        for s in songs:
            if s["genre"]==g and s["mood"]==m and s["language"]==l:
                print(f'{s["name"]} - {s["artist"]} ({s["rating"]}/5)')
                found=True
        if not found:
            print("No matching songs found.")

    elif choice=="2":
        for s in songs:
            print(f'{s["name"]} | {s["artist"]} | {s["genre"]} | {s["language"]} | {s["mood"]} | {s["rating"]}/5')

    elif choice=="3":
        q=input("Song name: ").lower()
        found=False
        for s in songs:
            if q in s["name"].lower():
                print(s)
                found=True
        if not found:
            print("Song not found.")

    elif choice=="4":
        for s in songs:
            if s["rating"]>=5:
                print(f'{s["name"]} - {s["artist"]}')

    elif choice=="5":
        a=input("Artist: ").lower()
        found=False
        for s in songs:
            if a==s["artist"].lower():
                print(f'{s["name"]} ({s["genre"]})')
                found=True
        if not found:
            print("No songs for this artist.")

    elif choice=="6":
        s=random.choice(songs)
        print("Today's Recommendation:")
        print(f'{s["name"]} - {s["artist"]}')

    elif choice=="7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")

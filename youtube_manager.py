import json
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
    
    
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']},
        Duration: {video['time']} ")
    print("\n")
    print("*" * 70)
        
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
def Update_video(videos):
    pass
def Delete_video(videos):
    pass
def main():
    videos = []
    while True:
        print("\n youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input(2)
        print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(video)
            case '3':
                Update_video(videos)
            case '4':
                Delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
if __name__ == "__main__":
    main()
    
    
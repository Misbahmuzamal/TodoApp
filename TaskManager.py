import json
def load_data():
    try:
       with open("youtube.txt",'r') as f:
          return json.load(f)
    except FileNotFoundError:
          return []
def List_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} and Duration {video['time']} ")
    print("\n")
    print("*" * 70)
def Save_data(videos):
    with open("youtube.txt",'w') as f:
        json.dump(videos,f)
def Add_videos(videos):
    name=input("enter video name")
    time=input("enter video time")
    videos.append({"name": name, "time": time})
    Save_data(videos)
def Update_videos(videos):
    List_videos(videos)
    index=int(input("Enter video number to update"))
    if 1<=index<=len(videos):
        name = input("enter video name")
        time = input("enter video time")
        videos[index-1]={'name':name ,"time":time}
        Save_data(videos)
    else:
        print("invalid index selected")

def Delete_videos(videos):
    List_videos(videos)
    index = int(input("Enter video number to Delete"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        Save_data(videos)
    else:
        print("invalid index selected")
def main():
    videos = load_data()
    while True:
        print("Video Manager")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit app")
        choice = input("Enter a choice: ")
        match choice:
            case '1':
                List_videos(videos)
            case '2':
                Add_videos(videos)
            case '3':
                Update_videos(videos)
            case '4':
                Delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == '__main__':
    main()







from tkinter import *
import tkinter.font as font
import youtube_dl

root = Tk()
root.title("Yt_downloader")
root.geometry("370x300")
Font1 = font.Font(size=15)
Font2 = font.Font(size=12)


def main():
    def mp4():
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download([entry.get()])

    def mp3():
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([entry.get()])

    label_1 = Label(root, text=" Welcome to Yt_downloader ")
    label_1.grid(row=0, column=0, padx=30, pady=20)
    label_1['font'] = Font1

    label_2 = Label(root, text=" Enter the url: ")
    label_2.grid(row=1, column=0, padx=20)
    label_2['font'] = Font2

    entry = Entry(root, width=40, borderwidth=2)
    entry.grid(row=2, column=0, padx=20, pady=10)

    mp4 = Button(root, text="MP4", command=mp4)
    mp4.grid(row=3, column=0, padx=10, pady=10)

    mp3 = Button(root, text="MP3", command=mp3)
    mp3.grid(row=4, column=0)

    quit = Button(root, text="Exit", command=root.quit)
    quit.grid(row=5, column=0, pady=10)


if __name__ == '__main__':
    try:
        main()
    except EXCEPTION:
        print("Something went wrong")

root.mainloop()

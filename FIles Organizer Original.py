import os

files = os.listdir()


def notExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


files = os.listdir()
files.remove("Files Organizer.py")

notExists('Docs')
notExists('Images')
notExists('Media')
notExists('Compressed')
notExists('Installers')
notExists('Others')

imgExts = [".tif", ".bmp", ".jpg", ".jpeg", ".gif", ".png", ".raw", ".eps", ".cr2", ".nef", ".orf", ".sr2", ".tiff"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".doc", ".docx", ".html", ".htm", ".odt", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

medExts = [".3g2", ".3gp", ".amv", ".asf", ".avi", ".mkv", ".mp4", ".mp3", ".m4v", ".f4v", ".f4p",
           ".f4a", ".f4b", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mpg", ".mpeg", ".m2v", ".wmv", ".viv", ".svi",
           ".roq", ".wav"]
media = [file for file in files if os.path.splitext(file)[1].lower() in medExts]

comExts = [".rar", ".zip", ".7z", ".arj", ".bz2", ".cab", ".gz", ".iso", ".jar",
           ".lz", ".lzh", ".tar", "uue", "xz", "z", "zipx", ".001"]
comp = [file for file in files if os.path.splitext(file)[1].lower() in comExts]

winExts = [".msi", ".msm", ".msp", ".mst", ".idt", ".cub", ".pcp", ".exe"]
wini = [file for file in files if os.path.splitext(file)[1].lower() in winExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in medExts) and (ext not in comExts) \
            and (ext not in winExts) and os.path.isfile(file):
        others.append(file)
move("Images", images)
move("Docs", docs)
move("Media", media)
move("Compressed", comp)
move("Installers", wini)
move("Others", others)

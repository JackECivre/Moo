import subprocess

try:
    print("MOOOOOOOOOO!!!! ")
    filename = "twitter_api.py"
    while True:
        process = subprocess.Popen("python " + filename, shell=True).wait()

        if process != 0:
            continue
        else:
            break
except Exception as Error:
    print("This Cow couldn't Moo" + str(Error))

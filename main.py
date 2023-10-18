import os
import time

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

def write_a_new_file():
    # count number of files with txt extension in tmp directory and add 1
    file_count = len([name for name in os.listdir("tmp") if name.endswith(".txt")]) + 1
    # write a new file
    with open(f"tmp/log_{file_count}.txt", mode="w") as file:
        content = f"counting files to test this API thing: {file_count}"
        file.write(content)

    # sleep for 10 seconds
    print(f"PID: {os.getpid()} -- sleeping for 10 seconds")
    time.sleep(10)

@app.post("/write-file")
async def write_file(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_a_new_file)
    return {"message": "Writing file in background"}
import whisper

file = input("enter the file name: ")

model = whisper.load_model("base")

result = model.transcribe(file)

print(result["text"])
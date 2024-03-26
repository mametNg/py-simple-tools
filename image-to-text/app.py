import easyocr

img_file = "sample.png"

reader = easyocr.Reader(['en', 'id'])
img = reader.readtext(img_file)
print(img)
print("=========================================================")

for (bbox, text, prob) in img:
    print(text)
print("=========================================================")

img = reader.readtext(img_file, detail=0)
print(img)
print("=========================================================")

img = reader.readtext(img_file, paragraph=True)
print(img)
print("=========================================================")
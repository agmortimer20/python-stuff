import requests
import PIL.Image
# !pip install face_recognition
import face_recognition
import urllib.request
from bs4 import BeautifulSoup

known_image = face_recognition.load_image_file("dwayne-the-rock-.jpg")

known_image_encoded = face_recognition.face_encodings(known_image)[0]

URL = "https://www.dmarge.com/2021/01/most-likeable-person-world-the-rock.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

images = soup.find_all("img")

# target = 0.6
# best_image = None

for image in images:
  path = image["src"]

  opener = urllib.request.build_opener()
  opener.addheaders = [('User-Agent', 'MyApp/1.0')]
  urllib.request.install_opener(opener)
  urllib.request.urlretrieve(path, "selected_image.png")

  scraped_image = face_recognition.load_image_file("selected_image.png")  
  scraped_image_encoded = face_recognition.face_encodings(scraped_image)

  result = face_recognition.compare_faces(known_face_encodings=known_image_encoded, face_encoding_to_check=scraped_image_encoded, tolerance=0.6)
  print(type(result))
  # result = face_recognition.face_distance(scraped_image_encoded, known_image_encoded)
  # print(result)

  # check=face_recognition.compare_faces([known_image_encoded], scraped_image_encoded)
  
  # if result[0] < target:
  #   best_image = scraped_image

  if result[0] == True:
    print("match")
    best_image = scraped_image
  else:
    print("nope")

print("closest match:")

pil_image = Image.fromarray(best_image)
pil_image
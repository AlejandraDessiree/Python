import random

global img_empty
img_empty = ('''  
  ------
  |    |
       |
       |
       |
       |
       |
===========''')

global img_fail_1
img_fail_1 = ('''
  ------
  |    |
  O    |
       |
       |
       |
       |
===========''')

global img_fail_2
img_fail_2 = ('''
  ------
  |    |
  O    |
  |    |
       |
       |
       |
===========''')

global img_fail_3
img_fail_3 = ('''
  ------
  |    |
  O    |
 /|    |
       |
       |
       |
===========''')

global img_fail_4
img_fail_4 = ('''
  ------
  |    |
  O    |
 /|\\   |
       |
       |
       |
===========''')

global img_fail_5
img_fail_5 = ('''
  ------
  |    |
  O    |
 /|\\   |
 /     |
       |
       |
===========''')

global img_fail_6
img_fail_6 = ('''
  ------
  |    |
  O    |
 /|\\   |
 / \\   |
       |
===========''')

def hangman():
 words_list = ["apple", "banana", "grape", "orange", "mango", "watermelon", "kiwi", "peach", "strawberry", "blueberry","cherry", "plum", "pineapple", "pear", "cantaloupe", "melon", "fig", "apricot", "lemon", "lime","sunflower", "rose", "tulip", "orchid", "daffodil", "lily", "lavender", "daisy", "violet", "lotus", "dog", "cat", "rabbit", "hamster", "turtle", "fish", "parrot", "elephant", "giraffe", "kangaroo", "zebra", "panda", "lion", "tiger", "bear", "wolf", "fox", "deer", "bison", "squirrel", "raccoon", "ball", "bat", "glove", "goal", "net", "basket", "soccer", "football", "baseball", "hockey", "tennis", "golf", "volleyball", "cricket", "rugby", "swimming", "running", "cycling", "badminton", "squash", "archery", "wrestling", "boxing", "karate", "judo", "fencing", "sailing", "surfing", "skating", "skiing", "piano", "guitar", "violin", "drums", "flute", "trumpet", "saxophone", "clarinet", "accordion", "harp", "computer", "laptop", "keyboard", "mouse", "monitor", "phone", "tablet", "camera", "printer", "scanner", "television", "radio", "speaker", "headphones", "microphone", "charger", "battery", "router", "modem", "car", "bike", "bus", "train", "plane", "boat", "helicopter", "submarine", "truck", "scooter", "bicycle", "skateboard", "rollerblades", "wagon", "hot-air balloon", "tractor", "electric scooter", "hoverboard", "mountain", "river", "ocean", "lake", "forest", "desert", "valley", "canyon", "volcano", "island", "beach", "hill", "cliff", "plateau", "prairie", "field", "meadow", "park", "garden", "backyard", "New York", "London", "Paris", "Tokyo", "Berlin", "Sydney", "Rome", "Moscow", "Beijing", "Cairo", "Bangkok", "Amsterdam", "Athens", "Los Angeles", "Madrid", "Istanbul", "Dubai", "Dubai", "Rio de Janeiro", "Mexico City", "Buenos Aires", "Toronto", "Mexico", "USA", "Canada", "Germany", "Italy", "France", "India", "Australia", "China", "Japan", "Brazil", "Argentina", "South Africa", "Egypt", "Russia", "Spain", "Greece", "Thailand", "Norway", "Sweden", "Switzerland", "Belgium", "Netherlands", "South Korea", "Vietnam", "Chile", "pizza", "burger", "fries", "pasta", "spaghetti", "sushi", "sashimi", "taco", "burrito", "falafel", "gyros", "salad", "sandwich", "bagel", "steak", "chicken", "bacon", "sausage", "tofu", "cheese", "ice cream", "cake", "pie", "cookie", "donut", "croissant", "waffles", "brownie", "pancakes", "cheesecake", "coffee", "tea", "milk", "juice", "smoothie", "soda", "beer", "wine", "whiskey", "cocktail", "water" "chair", "table", "couch", "sofa", "bed", "pillow", "blanket", "lamp", "lamp shade", "fan", "rug", "curtain", "bookshelf", "dresser", "mirror", "toaster", "microwave", "oven", "refrigerator", "dishwasher", "washing machine", "dryer", "vacuum", "clock", "painting", "picture frame", "telephone", "alarm clock", "restaurant", "store", "library", "school", "hospital", "bank", "market", "gym", "theater", "museum", "church", "mosque", "temple", "stadium", "stadium", "palace", "castle", "fortress", "skyscraper", "airport", "train station", "post office", "park", "zoo", "aquarium", "shopping mall", "hotel", "resort", "book", "pen", "notebook", "paper", "pencil", "eraser", "ruler", "scissors", "glue", "stapler", "tape", "highlighter", "marker", "file", "folder", "binder", "clipboard", "paperclip", "rubber band", "shirt", "pants", "dress", "jacket", "sweater", "hat", "scarf", "gloves", "shoes", "socks", "raincoat", "umbrella", "boots", "sandals", "belt", "tie", "bracelet", "necklace", "earrings", "watch", "wallet", "bag", "suitcase", "backpack", "briefcase", "glasses", "sunglasses", "scarf", "calendar", "clock", "time", "watch", "hour", "minute", "second", "day", "week", "month", "year", "season", "holiday", "birthday", "vacation", "trip", "journey", "adventure", "exploration", "light", "dark", "bright", "shadow", "sun", "moon", "star", "cloud", "sky", "rain", "snow", "wind", "thunder", "lightning", "fog", "storm", "earthquake", "hurricane", "tornado", "traffic", "cityscape", "street", "road", "bridge", "building", "construction", "urban", "suburb", "nature", "wildlife", "landscape", "countryside", "island", "archipelago", "desert", "beach", "python", "java", "javascript", "ruby", "swift", "go", "c", "cpp", "kotlin", "php", "perl", "rust", "typescript", "html", "css", "sql", "ruby", "matlab", "r", "scala", "haskell", "algorithm", "function", "variable", "loop", "array", "string", "integer", "boolean", "class", "object", "method", "constructor", "inheritance", "encapsulation", "polymorphism", "abstraction", "interface", "recursion", "data structure", "hashmap", "stack", "queue", "linked list", "tree", "graph", "search", "sort", "django", "flask", "react", "angular", "vue", "nodejs", "express", "bootstrap", "tailwind", "jquery", "tensorflow", "keras", "pytorch", "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", "opencv","git", "github", "gitlab", "docker", "jenkins", "aws", "azure", "google cloud", "heroku", "debugging", "compiling", "syntax", "IDE", "text editor", "CLI", "API", "framework", "repository", "branch", "commit", "pull request", "merge", "clone", "push", "version control", "package manager", "dependency", "unit test"]
 filtered_words = [word for word in words_list if " " not in word]
 word = random.choice(filtered_words).lower()
 print("Welcome to HangMan")
 word_lenght = len(word)
 placeholder = ""
 for position in range(word_lenght):
    placeholder += "_"

 print("The word you have to guess is: ", placeholder)
 
 guessed_letters = []
 game_over = False
 attempts = 6
 
 if attempts == 6:
     print(img_empty)
    

 while attempts > 0 and not game_over:
    display = ""
    placeholder = ""
    
  
    guess = input("Guess a letter: ").lower()
     
    if guess not in word:
         attempts -= 1
         print(f"You have {attempts} attempts left")     
         if attempts == 5:
          print(img_fail_1)
         elif attempts == 4:
          print(img_fail_2)
         elif attempts == 3:
          print(img_fail_3) 
         elif attempts == 2:
          print(img_fail_4)
         elif attempts == 1:
          print(img_fail_5)
        
    for letter in word:
      if letter == guess:
        display += letter
        guessed_letters.append(guess)
        print(img_empty)
      elif letter in guessed_letters:
        display += letter
        if attempts == 5:
           print(img_fail_1)
        elif attempts == 4:
           print(img_fail_2)
        elif attempts == 3:
           print(img_fail_3)
        elif attempts == 2:
           print(img_fail_4)
        elif attempts == 1:
           print(img_fail_5)
      else:
        display += "_"  
            
    print(display)
      
    if not "_" in display:
      game_over = True
      print("You Won")
      
    if attempts == 0:
      print(img_fail_6)
      game_over = True
      print("the word was: ", word)
      print("No more attempts, try again")

hangman()
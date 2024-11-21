import random

def hangman():
 words_list = ["apple", "banana", "grape", "orange", "mango", "watermelon", "kiwi", "peach", "strawberry", "blueberry","cherry", "plum", "pineapple", "pear", "cantaloupe", "melon", "fig", "apricot", "lemon", "lime","sunflower", "rose", "tulip", "orchid", "daffodil", "lily", "lavender", "daisy", "violet", "lotus", "dog", "cat", "rabbit", "hamster", "turtle", "fish", "parrot", "elephant", "giraffe", "kangaroo", "zebra", "panda", "lion", "tiger", "bear", "wolf", "fox", "deer", "bison", "squirrel", "raccoon", "ball", "bat", "glove", "goal", "net", "basket", "soccer", "football", "baseball", "hockey", "tennis", "golf", "volleyball", "cricket", "rugby", "swimming", "running", "cycling", "badminton", "squash", "archery", "wrestling", "boxing", "karate", "judo", "fencing", "sailing", "surfing", "skating", "skiing", "piano", "guitar", "violin", "drums", "flute", "trumpet", "saxophone", "clarinet", "accordion", "harp", "computer", "laptop", "keyboard", "mouse", "monitor", "phone", "tablet", "camera", "printer", "scanner", "television", "radio", "speaker", "headphones", "microphone", "charger", "battery", "router", "modem", "car", "bike", "bus", "train", "plane", "boat", "helicopter", "submarine", "truck", "scooter", "bicycle", "skateboard", "rollerblades", "wagon", "hot-air balloon", "tractor", "electric scooter", "hoverboard", "mountain", "river", "ocean", "lake", "forest", "desert", "valley", "canyon", "volcano", "island", "beach", "hill", "cliff", "plateau", "prairie", "field", "meadow", "park", "garden", "backyard", "New York", "London", "Paris", "Tokyo", "Berlin", "Sydney", "Rome", "Moscow", "Beijing", "Cairo", "Bangkok", "Amsterdam", "Athens", "Los Angeles", "Madrid", "Istanbul", "Dubai", "Dubai", "Rio de Janeiro", "Mexico City", "Buenos Aires", "Toronto", "Mexico", "USA", "Canada", "Germany", "Italy", "France", "India", "Australia", "China", "Japan", "Brazil", "Argentina", "South Africa", "Egypt", "Russia", "Spain", "Greece", "Thailand", "Norway", "Sweden", "Switzerland", "Belgium", "Netherlands", "South Korea", "Vietnam", "Chile", "pizza", "burger", "fries", "pasta", "spaghetti", "sushi", "sashimi", "taco", "burrito", "falafel", "gyros", "salad", "sandwich", "bagel", "steak", "chicken", "bacon", "sausage", "tofu", "cheese", "ice cream", "cake", "pie", "cookie", "donut", "croissant", "waffles", "brownie", "pancakes", "cheesecake", "coffee", "tea", "milk", "juice", "smoothie", "soda", "beer", "wine", "whiskey", "cocktail", "water" "chair", "table", "couch", "sofa", "bed", "pillow", "blanket", "lamp", "lamp shade", "fan", "rug", "curtain", "bookshelf", "dresser", "mirror", "toaster", "microwave", "oven", "refrigerator", "dishwasher", "washing machine", "dryer", "vacuum", "clock", "painting", "picture frame", "telephone", "alarm clock", "restaurant", "store", "library", "school", "hospital", "bank", "market", "gym", "theater", "museum", "church", "mosque", "temple", "stadium", "stadium", "palace", "castle", "fortress", "skyscraper", "airport", "train station", "post office", "park", "zoo", "aquarium", "shopping mall", "hotel", "resort", "book", "pen", "notebook", "paper", "pencil", "eraser", "ruler", "scissors", "glue", "stapler", "tape", "highlighter", "marker", "file", "folder", "binder", "clipboard", "paperclip", "rubber band", "shirt", "pants", "dress", "jacket", "sweater", "hat", "scarf", "gloves", "shoes", "socks", "raincoat", "umbrella", "boots", "sandals", "belt", "tie", "bracelet", "necklace", "earrings", "watch", "wallet", "bag", "suitcase", "backpack", "briefcase", "glasses", "sunglasses", "scarf", "calendar", "clock", "time", "watch", "hour", "minute", "second", "day", "week", "month", "year", "season", "holiday", "birthday", "vacation", "trip", "journey", "adventure", "exploration", "light", "dark", "bright", "shadow", "sun", "moon", "star", "cloud", "sky", "rain", "snow", "wind", "thunder", "lightning", "fog", "storm", "earthquake", "hurricane", "tornado", "traffic", "cityscape", "street", "road", "bridge", "building", "construction", "urban", "suburb", "nature", "wildlife", "landscape", "countryside", "island", "archipelago", "desert", "beach", "python", "java", "javascript", "ruby", "swift", "go", "c", "cpp", "kotlin", "php", "perl", "rust", "typescript", "html", "css", "sql", "ruby", "matlab", "r", "scala", "haskell", "algorithm", "function", "variable", "loop", "array", "string", "integer", "boolean", "class", "object", "method", "constructor", "inheritance", "encapsulation", "polymorphism", "abstraction", "interface", "recursion", "data structure", "hashmap", "stack", "queue", "linked list", "tree", "graph", "search", "sort", "django", "flask", "react", "angular", "vue", "nodejs", "express", "bootstrap", "tailwind", "jquery", "tensorflow", "keras", "pytorch", "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", "opencv","git", "github", "gitlab", "docker", "jenkins", "aws", "azure", "google cloud", "heroku", "debugging", "compiling", "syntax", "IDE", "text editor", "CLI", "API", "framework", "repository", "branch", "commit", "pull request", "merge", "clone", "push", "version control", "package manager", "dependency", "unit test"]
 word = random.choice(words_list)
 print(word)
 
 guessed_letters = []
 game_over = False
 attemps = 5
 word_lenght = len(word)
 
 while not game_over:
    while attemps > 0:
     display = ""
     placeholder = ""
     for position in range(word_lenght):
       placeholder += "_"
  
     guess = input("Guess a letter: ").lower()
     
     for letter in word:
      if letter == guess:
        display += letter
        guessed_letters.append(guess)
      elif letter in guessed_letters:
        display += letter
      else:
        display += "_"  
            
     print(display)
     
     if guess not in word:
         attemps -= 1
         print(f"You have {attemps} left")
      
     if not "_" in display:
      game_over = True
      print("You Won")
      
     if attemps == 0:
      game_over = True
      print("No more attemps, try again")
  
hangman()
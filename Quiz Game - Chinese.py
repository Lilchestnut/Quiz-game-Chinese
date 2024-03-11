print("Are you ready to test your Chinese?")
answer = input()
if answer.lower() != "yes":
    quit()

print("There are 4 questions \n")

print(
    "Let's start with an easy one: 你好 \n" 
    "a. Good morning! \n" 
    "b. How are you? \n" 
    "c. Hi! \n"
      )
answer = input()
while answer.lower() != "c":
    print("WRONGGGGGGGG! Take another guess!")
    answer = input()
print("You are correct! \n")
    

print("Here is the next one: 我會說一點中文 \n"
      "a. I am hungry \n"
      "b. I can speak a little Mandarine \n"
      "c. I like to read \n"
      )
answer = input()
while answer.lower() != "b":
    print("WRONGGGGGGGG! Take another guess!")
    answer = input()
print("You are correct!\n")

print("Here is the next one: 你吃飯了嗎? \n"
      "a. How was your day? \n"
      "b. Have you eaten? \n"
      "c. Going to head out! \n"
      )
answer = input()
while answer.lower() != "b":
    print("WRONGGGGGGGG! Take another guess!")
    answer = input()
print("You are correct!\n")

print("Here is the next one: 我今天過得很開心! \n"
      "a. I went to work today \n"
      "b. He is feeling down \n"
      "c. I had a great day today \n"
      )
answer = input()
while answer.lower() != "c":
    print("WRONGGGGGGGG! Take another guess!")
    answer = input()
print("You are correct!")

print(f"Thanks for playing the quiz \n")
    #   "here is your score: {score}"
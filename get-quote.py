import random


def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  

def addQuote():
    quote= input("Write the quote you want to add...\n")
    file_object = open('quotes.txt', 'a')
    file_object.write("\n"+ quote)
    file_object.close()
    


if __name__== "__main__":
    ans = input("add more quote? Yes or no?\n")
    if ans.lower() == "yes":
        addQuote()
    primary()


import random
SPACE = " "
NONWORD = chr(0)
tolstoy = "texts/warandpeace.txt"
paine = "texts/commonsense.txt"

def readwords(filename:str)-> list[str]:
    with open(filename) as f:
        lines = f.readlines()
    words = []
    for line in lines:
        words += [ word for word in line.split() if word != "" ]
    return words
    
def generate1(limit:int, filename:str, *start_words:str)-> str:
    output = [*start_words]
    predecessor = output [-1]
    print (output)
    words = readwords(filename)
    successors = build_model1(words)
    for _ in range (limit - len(start_words)):
        chosenWord = pick_word(predecessor, successors)
        output.append(chosenWord)
        predecessor = chosenWord
    return SPACE.join(output)

def build_model1(words:list[str]) -> dict [str, list[str]]:
    successors = {}
    predecessor = NONWORD
    for word in words:
        if predecessor in successors:
            successors[predecessor].append(word)
        else:
            successors[predecessor] = [word]
        predecessor = word
    return successors

def pick_word(predecessor:str, successors:dict[str, list[str]])-> str:
    return random.choice(successors[predecessor])

def build_model2(words:list[str], chain_length:int) -> dict [str, list[str]]:
    successors = {}
    predecessor = (NONWORD,) * chain_length
    for word in words:
        if predecessor in successors:
            successors[predecessor].append(word)
        else:
            successors[predecessor] = [word]
        predecessor = append_shift_left(predecessor, word)
    return successors

def append_shift_left(items: tuple[str], item: str)-> tuple[str]:
    return items[1:] + (item,)

def pick_word2(predecessor:tuple[str], successors: dict[str, list[str]])->str:
    return random.choice(successors[predecessor])

def generate2(limit:int, filename:str, *start_words:str)-> str:
    output = [*start_words]
    predecessor = (tuple(start_words))
    words = readwords(filename)
    successors = build_model2(words, len(predecessor))
    for _ in range (limit - len(start_words)):
        chosenWord = pick_word2(predecessor, successors)
        output.append(chosenWord)
        predecessor = append_shift_left(predecessor, chosenWord)
    return SPACE.join(output)

print(generate2(50, tolstoy, "to", "go", "to"))
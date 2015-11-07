
import pickle

book = open("log.txt")

expect_title = False
expect_body = False

break_in_body = 0

poems = {}
poem = []

while True:
    l = book.readline()
    rl = l
    if len(l) == 0:
        break

    l = l.strip()

    if l.find("BOOK") != -1:
        for _ in range(0, 2):
            book.readline()
        expect_title = True
    elif expect_title and len(l) > 0:
        print repr(l), len(l)
        expect_title = False
        title = l.strip('"')
        poem = []
        book.readline()
        expect_body = True
    elif expect_body:
        if len(l) == 0:
            if break_in_body > 2:
                poems[title] = poem[:-1]
                poem = []
                expect_body = False
                expect_title = True
                break_in_body = 0
            else:
                poem.append("")
                break_in_body += 1
        else:
            break_in_body = 0
            poem.append(l)
print len(poems)


pickle.dump(poems, open('log.pkl', 'w'))        
        
    
    

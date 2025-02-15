"""
a=open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/article.txt', 'r')
b=a.read()
def read_last(lines, file):
    if lines>0:
        with open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/article.txt') as text:
            file_lines=text.readlines()[-lines :]
        for line in file_lines:
            print(line.strip())
    
            
read_last(1, 'article.txt')
read_last(-5, 'read_last')

"""
"""
def longest_words(file):
    with open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/article.txt', 'r') as text:
        words=text.read().split()
    a=len(max(words,key=len))
    b=[word for word in words if len(word)==a]
    
    f='article.txt'
    i=1
    while os.path.exists(f):
        f=f"'article.{i}.txt"
        i+=1
    with open(f, 'w') as file:
        file.write(' '.join(b)+"\n")
print(a)
"""
"""
def count_statistics(file):
    with open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/file.txt', 'r') as f:
        text=f.read('file.txt')
        a=sum(c.isalpha() for s in text)
        b =text.split()
        c =len(words)
        d =text.count("\n")+1
        text=f.close()
print(c)
""""
       


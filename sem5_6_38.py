# Напишите программу, удаляющую из текста все слова содержащие "абв".


text = 'Но я должен объяснить абв, как родилась вся эта ошиабвочная идея отрицания удоабвольствия и восхваления боли, и я дам абвам полный отчет о системе и излабвгаю фактические учения абвеликого исследователя истиныабв.'
d = 'абв'

def delWorlds(text, d):
    arr = text.split()
    for i in arr:
        if i.find(d) != -1:
            arr.remove(i)
    res = " ".join(arr)
    return res

print(text)
print(delWorlds(text, d))
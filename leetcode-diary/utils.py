from pathlib import Path

def get_list(): 
    dir = Path(__file__).parent
    l = []
    for item in dir.iterdir():
        content = item.stem
        if content == 'TEMPT' or content == 'utils': continue
        if Path.is_dir(item): continue
        l.append(content)
    for i in l:
        print(i)
    print('-------------------------------')
    print(f'total number: {len(l)}')
    return l

get_list()


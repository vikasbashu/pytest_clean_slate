import json

def getLocators(filename):
    return json.load(open(f'locators/{filename}.json', 'r'))

if __name__ == '__main__':
    print(getLocators('amazon_locators.json'))
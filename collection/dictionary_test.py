# testing dictionary methods
def dictionary_test():
    person = {'name': 'Thofiq', 'age': '32'}
    person.update({'phone': '89828349383434'})
    address = person.get('address', 'no address specified')
    print(person)
    print(address)


dictionary_test()

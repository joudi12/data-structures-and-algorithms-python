from data_structures_and_algorithms.data_structures.hashtable.hashtable import HashTable

def left_join(synonym, antonyms):
    output = []
    for linkedlist in synonym.map:
        if linkedlist == None :
            continue
        else:
            current = linkedlist.head
            while current:

                if  antonyms.contains(current.data[0]):
                    output.append(current.data)
                    current.data.append(antonyms.get(current.data[0]))

                else:
                    output.append(current.data)
                    current.data.append('null')
                current = current.next


    return output
if __name__ == "__main__":
    synonym=HashTable(1024)
    antonyms=HashTable(1024)
    synonym.add('could','enamored')
    synonym.add('cloud','anger')
    antonyms.add('fond','averse')

    print(left_join(synonym, antonyms))

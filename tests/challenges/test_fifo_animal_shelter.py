from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter ,Queue,Dog,Cat

def test_enqueu_cat_dog():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    Sherry = Cat('Sherry')
    Semsem = Cat('Semsem')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(Sherry)
    animals.enqueue(Semsem)

    expected = ('alex', 'Aln', 'Sherry', 'Semsem')
    actual = alex.name ,aln.name, Sherry.name,Semsem.name
    assert expected == actual

def test_enqueu_any_value():
    animals = AnimalShelter()
    expected = 'Add Cat or Dog Only'
    actual = animals.enqueue('any')
    assert expected == actual

def test_dequeue_cat():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    Sherry = Cat('Sherry')
    Semsem = Cat('Semsem')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(Sherry)
    animals.enqueue(Semsem)

    expected = 'Sherry'
    actual = animals.dequeue('cat')
    assert expected == actual

def test_dequeue_dog():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    Sherry = Cat('Sherry')
    Semsem = Cat('Semsem')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(Sherry)
    animals.enqueue(Semsem)

    expected = 'Aln'
    actual = animals.dequeue('dog')
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_any():
    animals = AnimalShelter()
    aln = Dog('Aln')
    Sherry = Cat('Sherry')
    animals.enqueue(aln)
    animals.enqueue(Sherry)

    expected = None
    actual = animals.dequeue('any')
    assert expected == actual

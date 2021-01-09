# Hashtables
## A Hash Table is a data structure that stores data in an associative manner. It is made up of two parts: an array, where the data is stored, and a Hash Function which is a mapping function. Basically, a Hash Function is a function that takes things from one space and maps them to a space for indexing.

## Challenge
### dealing with it using linkedlist

## Implementation
### The Hashtable is implemented with the following methods:
- hash: takes in an arbitrary key and returns an index in the collection.
- add: takes in both the key and value. This method hashes the key, and adds the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
- contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
## Testing
### The Hashtable implementation passes the following tests:

- Adding a key/value to your hashtable results in the value being in the data structure
- Retrieving based on a key returns the value stored
- Successfully returns null for a key that does not exist in the hashtable
- Successfully handle a collision within the hashtable
- Successfully retrieve a value from a bucket within the hashtable that has a collision
- Successfully hash a key to an in-range value

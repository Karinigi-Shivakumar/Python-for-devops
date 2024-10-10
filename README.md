# Python-for-devops

| Feature          | List                        | Tuple                      | Set                         | Dictionary                              |
|------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------------------|
| **Definition**    | Ordered, mutable collection | Ordered, immutable collection | Unordered, mutable collection with no duplicates | Unordered, mutable collection of key-value pairs |
| **Syntax**        | `[1, 2, 3]`                | `(1, 2, 3)`                 | `{1, 2, 3}`                 | `{'key1': 'value1', 'key2': 'value2'}`  |
| **Order**         | Ordered                     | Ordered                     | Unordered                   | Unordered (Python 3.7+ maintains insertion order) |
| **Mutability**    | Mutable (can be changed)    | Immutable (cannot be changed) | Mutable (can be changed)    | Keys are immutable, values are mutable  |
| **Duplicates**    | Allows duplicates           | Allows duplicates           | Does not allow duplicates   | Keys must be unique, values can be duplicated |
| **Indexing**      | Supports indexing and slicing | Supports indexing and slicing | Does not support indexing   | Can access values using keys            |
| **Use Case**      | Collection of ordered items | Fixed ordered collection    | Unique items, unordered set operations | Key-value pairs, for mapping or lookup  |
| **Methods**       | `.append()`, `.remove()`, `.pop()`, etc. | `.count()`, `.index()`     | `.add()`, `.remove()`, `.union()`, etc. | `.keys()`, `.values()`, `.items()`, `.get()` |


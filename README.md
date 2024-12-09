# Remote Procedure Call

RPC is an API architecture that allows a function or procedure to be executed on a remote machine within a network. It's commonly used when tasks need to be distributed across multiple machines or when making requests more efficiently.

## Built with

Client and server can operate on different computers and can be written in different programming languages.   
The implementation was carried out in the following programming languages:

| Client-Server | Programming Language |
|---------------|----------------------|
| Client        | JavaScript (Node.js) |
| Server        | Python               |

## Demo

[![asciicast](https://asciinema.org/a/P71AG0MTjQ3LIj7oJfv55jJvq.svg)](https://asciinema.org/a/P71AG0MTjQ3LIj7oJfv55jJvq)

## Server Functions

The server provides the following functions as RPC to the client:

- `floor`: Returns the nearest integer by rounding down.
  - **Params**: `double x`
  - **Return**: `int`

- `nroot`: Computes the value of `r` in the equation `x = r^n`.
  - **Params**: `int n, int x`
  - **Return**: `int`

- `reverse`: Returns a new string that is the reverse of the input string.
  - **Params**: `string s`
  - **Return**: `string`

- `isAnagram`: Checks if two strings are anagrams of each other.
  - **Params**: `string s1, string s2`
  - **Return**: `bool`

## Implementation

- On the server side, a hash map of <string, callable> pairs is created to store the keys and values.
- When a request arrives at the server, it refers to this table to find the function associated with the specified key, and passes the parameters received from the request to the function.
- Parameter validation is performed before executing the function to ensure parameters are sent in the correct format and data type.
- Multiple clients are supported using Python's threading and multiprocessing modules, assigning a unique ID to each request (process) to track which request comes from which client.

If an error occurs, the server returns a response to the client containing an error message like the following:

```json
{
    "id": 1,
    "error": "Invalid parameter"
}
```
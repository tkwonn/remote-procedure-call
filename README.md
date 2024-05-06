# Remote Procedure Call (RPC)

RPC is an API architecture that allows a function or procedure to be executed on a remote machine within a network. It's commonly used when tasks need to be distributed across multiple machines or when making requests more efficiently.

### Reasons for Using Remote Machines

Some of the reasons to use remote machines include:

- **Accessing a company's confidential database** for security reasons.
- **Performing computationally intensive functions** that require more resources.

RPC ensures that the client and server can operate on different computers and can be written in different programming languages. This time, the implementation was carried out in the following programming languages:

| Client-Server | Programming Language |
|---------------|----------------------|
| Client        | JavaScript (Node.js) |
| Server        | Python               |

### Demo

![RPC Demo Output](https://github.com/tkwonn/socket/assets/66197642/8730c610-c884-4627-b710-834864d37134)

### Server Functions

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

### Request and Response Format

```json
// Request
{
    "id": 1,
    "method": "nroot",
    "params": [3, 8]
}

// Response
{
    "id": 1,
    "results": "2",
    "result_type": "int"
}
```

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
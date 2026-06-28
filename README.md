# Multi-Service Converter Server

## Team

- Student Name: Gurnoor Pannu |  Student ID: 169104346
- Student Name: Gurbeer Pannu |  Student ID: 169104705

## Programming language used

- Python 3 
- only the standard library like socket and threading.

## Files

| File             | Purpose                                         |
|------------------|-------------------------------------------------|
| `server.py`      | TCP server — accept loop + one thread per client + does the conversion|
| `client.py`      | Interactive TCP client                          |
| `protocol_design.md`    | Wire protocol specification              |
| `README.md`      | Design explanation                              |

## How to compile

None needed — Python is interpreted. Just make sure Python 3 is installed:

```
python3 --version
```

## How to run server

```
python3 server.py
```

- Since the instructions jsut say specified port, we decided to use port 9000.
- The server runs until you stop it with `Ctrl+C`.
- It prints a line each time a client connects/disconnects.

Example:
```
$ python3 server.py 9000
Multi-Service Converter Server listening on port 9000...
Press Ctrl+C to stop.
```

## How to run client

In a separate terminal (can be on the same machine or a different one
on the network):

```
python3 client.py
```

- `host` defaults to `127.0.0.1` (localhost)
- `port` defaults to `9000`

Example session:
```
$ python3 client.py
Connected to 127.0.0.1:9000. Type HELP for commands, QUIT to exit.
> CONVERT TEMP C F 25
RESULT 77.00 F
> CONVERT CURRENCY USD CAD 100
RESULT 137.00 CAD
> QUIT
```

You can run multiple `client.py` instances at once (in different
terminals) to demonstrate the server handling concurrent connections.

## Supported commands

```
CONVERT TEMP C F <value>        CONVERT TEMP F C <value>
CONVERT LENGTH KM MI <value>    CONVERT LENGTH MI KM <value>
CONVERT WEIGHT KG LB <value>    CONVERT WEIGHT LB KG <value>
CONVERT CURRENCY <FROM> <TO> <value>     (FROM/TO ∈ USD, CAD, EUR, GBP)
HELP                              (client-side only — shows this list)
QUIT  /  EXIT                     (closes the connection)
```

Full protocol details, including all error responses, are in `protocol.md`.

## Known limitations

- Currency conversion uses **fixed, hardcoded exchange rates, not live rates from an API**
- No authentication/encryption — this
  is a plaintext protocol intended
  for a local/trusted network, not production use.
- Negative or zero values are accepted and converted without a
  physical-plausibility check.
- The server does not persist logs to disk beyond stdout.
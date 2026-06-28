# Protocol Specification — Multi-Service Converter

Plain-text line-based protocol over TCP. Every message ends with `\n`.
The connection stays open across multiple requests until the client
sends `QUIT` or disconnects.

## Request (client → server)

```
CONVERT <CATEGORY> <FROM_UNIT> <TO_UNIT> <VALUE>
```

- `<CATEGORY>`: Can only be either `TEMP`, `LENGTH`, `WEIGHT`, `CURRENCY`
- `<FROM_UNIT>` / `<TO_UNIT>`: must both belong to the same category
- `<VALUE>`: a number (int or float), e.g. `25` or `98.6`
- Tokens are case-insensitive (`convert temp c f 25` works)

| Category | Valid units      |
|----------|-------------------|
| TEMP     | C, F              |
| LENGTH   | KM, MI            |
| WEIGHT   | KG, LB            |
| CURRENCY | USD, CAD, EUR, GBP|

Other supported lines:

- `QUIT` / `EXIT` — close the connection (handled by both sides)

## Response (server → client)

Success:
```
RESULT <VALUE> <UNIT>
```
`<VALUE>` is always formatted to 2 decimal places.

Error (exactly one line per request, request is otherwise ignored):
```
ERROR <message>
```

| Condition                                   | Response                   |
|----------------------------------------------|-----------------------------|
| Unknown category                              | `ERROR Invalid category`   |
| Unit not valid for that category              | `ERROR Invalid unit`       |
| Value isn't a parseable number                | `ERROR Invalid numeric value` |
| Wrong number of tokens / unknown command       | `ERROR Malformed request`  |

## Examples

```
> CONVERT TEMP C F 25
< RESULT 77.00 F

> CONVERT CURRENCY USD CAD 100
< RESULT 137.00 CAD

> CONVERT TEMP C K 25
< ERROR Invalid unit

> CONVERT TEMP C F abc
< ERROR Invalid numeric value
```
# The Emoji Code JSON API

The URI format is `/api/{code}.json`.

??? example "Fetch a 200 Emoji Code"

    For example, fetching `/api/200.json` returns:
    
    ```javascript
    {
      "code": 200,
      "name": "OK",
      "description": "Request fulfilled, document follows",
      "emoji": ":thumbsup:",
      "category": "success"
    }
    ```

You may fetch all of the Emoji Codes @ `/api/codes.json`.

[Try it today!](codes.json){target=_blank}

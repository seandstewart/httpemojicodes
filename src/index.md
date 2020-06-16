# HTTP Emoji Codes :globe_with_meridians:

HTTP Emoji Codes are *HTTP Status Codes for Humans™*. Start sending Emoji Codes and
make the web a more human place, one response at a time!

This lexicon was inspired by a twitter thread started by user `@francesc`, linked below,
and is entirely in the public domain. Contributions are always welcome!

## JSON API

This site has a simple JSON API for fetching Emoji Codes by their legacy integer Status
Codes.

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

[Try it today!](/api/codes.json){target=_blank}

## Path to Success :white_check_mark:

- [ ] Connect with our API or download the source JSON.
- [ ] Update your server to send your Status Emoji with the `X-Status-Emoji` header.
- [ ] Profit :money_mouth_face:

## Sources

- [Twitter Thread started by @francesc](https://twitter.com/francesc/status/1271200986447482880){target=_blank}
- [MDN: HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status){target=_blank}
- [Twemoji 13.0](https://emojipedia.org/twitter/){target=_blank}

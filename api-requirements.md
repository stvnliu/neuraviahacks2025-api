# My API requirements :))))

- `GET /` should serve a web page (implement later)
- `GET /data?type=[type]&span=[timespan]`
  - returns JSON
  - an array of `{time: string, y: number}` for the data type `type` parameter that is recorded in the database
  - span of `"daily"/"weekly"/"monthly"`, produces 30, 7, or 30/31 values

```js
{
    'data': [
        {'x': "Monday", 'y': 67.0},
        {'x': "Tuesday", 'y': 78.0},
        // etc..
    ]
}
```
- `POST /data`
  - POST body JSON of following schema:
  ```js
  {
    fname: string,
    lname: string,
    age: number,
    heightMetre: number,
    weightKg: number,
  }
  ```

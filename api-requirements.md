# My API requirements :))))

- `GET /` should serve a web page (implement later)
- `GET /data?type=[type]&span=[timespan]`
  - GET DATA FOR EACH USER so put something in the header
  - returns JSON
  - an array of `{time: string, y: number}` for the data type `type` parameter that is recorded in the database
  - span of `"daily"/"weekly"/"monthly"`, produces 30, 7, or 30/31 values
- `GET /data/bmi?height=[float]&weight=[float]&sex=[bool]`
  - 0 - female 1 male
- this should giin form:
- `GET /data/bmi?user=[username]` etc.

```js
  [
    {'timestamp': 123456789, 'bmi': 1.0},
    {'timestamp': 123456789, 'bmi': 1.0},
    {'timestamp': 123456789, 'bmi': 1.0},
    {'timestamp': 123456789, 'bmi': 1.0},
    etc.// etc...
  ]
```

# ODOT

```js
{
    'data': [
        {'x': "Monday", 'y': 7.0},
        {'x': "Tuesday", 'y':78.0},
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

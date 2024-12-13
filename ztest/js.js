
fetch('https://h15g52u2y5.execute-api.eu-north-1.amazonaws.com/prod/empl?id=3ebcd909-7480-42c6-bb01-78e55fcb62f8', {
    method: 'GET'
}).then(res => res.json())
    .then(res => {
        console.log(res)
    })
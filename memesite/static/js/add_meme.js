document.getElementById(add_meme).addEventListener("click", add_meme)

class Meme {
    constructor(image, name, description, year, source){
        this.image = image
        this.name = name
        this.description = description
        this.year = year
        this.source = source
    }

    time_since_added() {
        const date = new Date();
        return date.getFullYear() - this.year;
    }
}

function add_meme(){
    // POST
    fetch('/', {

        headers: {
        'Content-Type': 'application/json'
        },
        method: 'POST',

        body: JSON.stringify({
            "greeting": "Hello from the browser!"
        })
    }).then(function (response) { // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {

        console.log('POST response: ');

        // Should be 'OK' if everything was successful
        console.log(text);
    });
}
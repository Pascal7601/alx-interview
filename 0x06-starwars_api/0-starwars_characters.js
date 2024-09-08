#!/usr/bin/node
/**
 * working with star wars api
 */

const request = require('request');

// Get the argument from the command line
const arg1 = process.argv[2];

// Form the URL for the film
const url = `https://swapi-api.alx-tools.com/api/films/${arg1}`;

// First request: Get the film data
request(url, (err, res, body) => {
    if (err) {
        console.error('Error:', err);
        return;
    }

    // Parse the response body into a JavaScript object
    const film = JSON.parse(body);
    
    // Extract the characters array (contains URLs)
    const characters = film.characters;

    // Loop over the characters and make a request for each one
    characters.forEach((characterUrl) => {
        request(characterUrl, (err, res, body) => {
            if (err) {
                console.error('Error fetching character:', err);
                return;
            }

            // Parse and log each character's data
            const character = JSON.parse(body);
            console.log(character.name);
        });
    });
});

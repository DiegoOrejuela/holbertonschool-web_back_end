module.exports = function displayMessage(message) {
  process.stdout.write(message  + '\n');
}
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

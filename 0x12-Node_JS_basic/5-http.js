const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise(((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, paramsStudents) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      let students = paramsStudents;
      students = students.split('\n');
      const headers = students.shift().split(',');

      const groupingStudentsField = {};
      const studentsObjects = [];

      students.forEach((student) => {
        if (student) {
          const studentInfo = student.split(',');
          const studentObject = {};

          headers.forEach((header, index) => {
            studentObject[header] = studentInfo[index];
            if (header === 'field') {
              if (groupingStudentsField[studentInfo[index]]) {
                groupingStudentsField[studentInfo[index]].push(studentObject.firstname);
              } else {
                groupingStudentsField[studentInfo[index]] = [studentObject.firstname];
              }
            }
          });
          studentsObjects.push(studentObject);
        }
      });
      const numberStudents = `Number of students: ${studentsObjects.length}`;

      let response = `${numberStudents}\n`;
      console.log(numberStudents);

      for (const groupStudent in groupingStudentsField) {
        if (groupingStudentsField[groupStudent]) {
          const listStudents = groupingStudentsField[groupStudent];
          const responseGroupStudents = `Number of students in ${groupStudent}: ${listStudents.length}. List: ${listStudents.join(', ')}`;
          response += `${responseGroupStudents}\n`;
          console.log(responseGroupStudents);
        }
      }
      resolve(response.substring(0, response.length - 1));
    });
  }));
}

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  switch (req.url) {
    case '/':
      res.writeHead(200);
      res.end('Hello Holberton School!');
      break;
    case '/students':
      res.writeHead(200);
      countStudents(process.argv[2])
        .then((data) => {
          res.end(`This is the list of our students\n${data}`);
        })
        .catch((error) => {
          res.end(error.message);
        });
      break;
    default:
      res.writeHead(404);
      res.end(JSON.stringify({ error: 'Resource not found' }));
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;

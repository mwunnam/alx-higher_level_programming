#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response !== 200) {
    console.error('Unable to get get data');
  }
  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
  const formattedJson = JSON.stringify(completedTasks, null, 2).replace(/"/g, "'").replace(/\n\s*}/g, ' }');
  console.log(formattedJson);
});

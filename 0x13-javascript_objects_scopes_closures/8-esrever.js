#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  const newList = [];

  for (let i = len; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};

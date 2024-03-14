#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      if (base > 10 && num > 9) {
        return String.fromCharCode(65 + num - 10);
      } else {
        return '' + num;
      }
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base);
    }
  };
};

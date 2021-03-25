#!/usr/bin/node
/* https://developer.mozilla.org/es/docs/Web/JavaScript/Closures */

/* Closure */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

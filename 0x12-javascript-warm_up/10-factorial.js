#!/usr/bin/node
/*Declare the function*/
function factorial (number) {
    if (isNaN(number) || number <= 1) {
	return 1;
    } else {
	/*Use recursion*/
	return number * factorial(number - 1);
    }
}
/*Declare arguments*/
const number = parseInt(process.argv[2]);
/*Call the function*/
console.log(factorial(number));

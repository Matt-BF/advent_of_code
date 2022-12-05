"use strict";
const { readFileSync } = require("fs");
const file = readFileSync("./input.txt", "utf-8");
const fileArray = file.split(/\n/);
const caloriesPerElf = [];
let caloriesCurrentElf = 0;
fileArray.forEach((line) => {
    if (line != "") {
        caloriesCurrentElf += parseInt(line);
    }
    else {
        caloriesPerElf.push(caloriesCurrentElf);
        caloriesCurrentElf = 0;
    }
});
console.log(Math.max(...caloriesPerElf));
const sortedCaloriesPerElf = caloriesPerElf
    .sort((a, b) => a - b)
    .reverse();
console.log(sortedCaloriesPerElf.slice(0, 3).reduce((a, b) => a + b));

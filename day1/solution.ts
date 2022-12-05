const { readFileSync } = require("fs");

const file = readFileSync("./input.txt", "utf-8");

const fileArray = file.split(/\n/);
const caloriesPerElf: number[] = [];
let caloriesCurrentElf: number = 0;

fileArray.forEach((line: string) => {
  if (line != "") {
    caloriesCurrentElf += parseInt(line);
  } else {
    caloriesPerElf.push(caloriesCurrentElf);
    caloriesCurrentElf = 0;
  }
});
console.log(Math.max(...caloriesPerElf));

const sortedCaloriesPerElf: number[] = caloriesPerElf
  .sort((a, b) => a - b)
  .reverse();
console.log(sortedCaloriesPerElf.slice(0, 3).reduce((a, b) => a + b));

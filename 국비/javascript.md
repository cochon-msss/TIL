# JavaScript

부트캠프 JavaScript 학습노트. 기초 문법부터 드림코딩 강의 실습 코드까지 정리.

## 자바스크립트 초급

### 변수, 자료형, 기본 문법

```javascript
let, const // 변수 타입
alert()        // 대화창 출력
console.log()  // 콘솔에 출력
typeof()       // 타입 확인
prompt()       // 사용자에게 값을 입력받을 때 사용
confirm()      // 사용자에게 확인을 받을 때 사용

String()   // 문자형으로 변환
Number()   // 숫자형으로 변환
Boolean()  // 불린형으로 변환

if문        // (자바와 동일)
for문       // (자바와 동일)
while문     // (자바와 동일)
do-while문  // (자바와 동일)
break, continue // (자바와 동일)
switch문    // (자바와 동일)

function() {} // 자바의 메소드와 동일

// 객체 만들기
const superman = {
  name: 'clark',
  age: 33,
}; // name:name 이면 name 으로 축약 가능

// 접근 방법
superman.name
superman['age']

// 추가
superman.gender = 'male'; // [] 표기법으로도 됨

// 삭제
delete superman.name;

// in 연산자
'age' in superman; // 프로퍼티 존재 확인
```

### 반복문, 메소드, 배열, 생성자 함수

```javascript
// for in 반복문
for (let key in superman) {
  console.log(key);
  console.log(superman[key]);
  console.log(Mike[x]);  // Mike['age'], Mike['name'] 값을 불러옴
  console.log(Mike);     // Mike의 이름만 불러옴
} // 객체를 순회하면서 값을 얻음
// key 는 변수 역할

// 메소드
sayhello: function () {
  console.log(`hello, i'm ${this.name}`);
}

// 배열
let students = ['철수', '영희', '영수'];
students[0] = '민정'; // 수정 가능
// 배열은 문자 뿐만 아니라, 숫자, 객체, 함수 등도 포함할 수 있음
let arr = [
  '민수',
  3,
  false,
  {
    name: 'Mike',
    age: 30,
  },
  function () {
    console.log('TEST');
  }
];

length      // 배열 길이
push()      // 배열 끝에 추가
pop()       // 배열 끝 요소 제거 (stack 메서드와 동일)
unshift(), shift() // 배열 앞에서 추가/제거

// for of 반복문
for (let day of days) {
  console.log(day);
} // 배열에는 for of 권장, 향상된 for문 느낌

function User(name, age) {
  this.name = name;
  this.age = age;
  this.sayName = function () {
    console.log(this.name);
  }
}
let user5 = new User('Han', 40);
user5.sayName(); // 'Han'
// 자바스크립트에서 this 는 user5를 의미
```

## 자바스크립트 중급

### 객체 메소드, 숫자/문자/배열 API

```javascript
// var 는 잘 사용하지 않음

// Object.assign() : 객체 복제
const newUser = Object.assign({ /* 초기값 */ }, user); // user값이 {} 으로 들어감
// { } + { name: 'Mike', age: 30 } 형태

// Object.keys() : 키 배열 반환
const user = {
  name: 'Mike',
  age: 30,
  gender: 'male',
};
Object.keys(user); // ["name", "age", "gender"]

// Object.values() : 값 배열 반환 (값만 배열로 반환)

// Object.entries() : 키/값 배열 반환 (키와 값을 쌍으로 묶어서 줌)
// [ ["name", "Mike"], ... ]

// Object.fromEntries() : 키/값 배열을 객체로

Symbol       // new를 붙이지 않는다. 유일한 식별자를 만들 때 사용
Symbol.for() // 전역 심볼
// 숨겨진 Symbol key 보는 법
Object.getOwnPropertySymbols(user);

// toString() : 10진수를 2진수/16진수로 바꿔줌
let num = 10;
num.toString(2); // "1010"

// Math
Math.ceil()    // 올림
Math.floor()   // 내림
Math.round()   // 반올림
Math.random()  // 무작위 수
Math.max()     // 괄호 안에서 가장 큰 숫자
Math.min()     // 괄호 안에서 가장 작은 숫자
Math.abs()     // 절대값
Math.pow(n, m) // 제곱
Math.sqrt()    // 제곱근

toFixed(2); // 소수점 둘째 자리까지 표현(셋째 자리에서 반올림)
            // 문자형으로 반환하기 때문에 Number()로 숫자로 변환
isNaN()     // NaN인지 아닌지 판단
parseInt()  // 문자열을 숫자로 바꿔준다.
parseFloat()// 소수점을 반환

// 문자열 메소드
toUpperCase() / toLowerCase() // 영어 대소문자 바꾸기
str.indexOf()    // 인덱스 위치 반환
str.slice(n, m)  // substring from to
str.substring(n, m) // slice와 다른 점은 n과 m을 바꿔도 동작, 음수 허용 x
str.substr(n, m) // n은 시작, m은 몇 개를 가져올 것인지
str.trim()       // 앞뒤 공백 제거
str.repeat(n)    // 문자열을 n번 반복

// 배열 메소드
arr.splice(n, m)    // 특정 요소 지움
arr.splice(n, m, x) // 특정 요소 지우고 추가
arr.splice()        // 삭제된 요소를 반환함
arr.slice(n, m)     // n부터 m까지 반환
arr.concat(arr2, arr3...) // 합쳐서 반환, 추가 느낌
arr.forEach(fn, name, index) // 배열 반복, fn은 함수
arr.indexOf / lastIndexOf // 위치 반환
arr.includes()  // 포함하는지 확인
arr.find(fn)    // 첫 번째 true 값만 반환하고 끝, 없으면 undefined 반환
arr.filter(fn)  // 조건에 맞는 것을 전부 찾는다
arr.reverse()   // 역순으로 재정렬
arr.map(fn)     // 함수를 받아 특정 기능을 실행하고 새로운 배열을 반환

arr.sort()      // 배열 재정렬
// Lodash 라이브러리
arr.reduce(fn)  // (prev, cur) 누적 계산값, 현재값
```

### 구조 분해 할당

```javascript
// 구조 분해 할당 - 배열이나 객체의 속성을 분리해서
// 그 값을 변수에 담을 수 있게 하는 표현식

// 배열 구조 분해, 객체 구조 분해 같음
let [x, y] = [1, 2];

let [user1, user2, user3] = users;
let [user1, , user2] = [1, 2, 3, 4]; // 두 번째 값 2는 공백으로 건너뜀
```

## 데이터 타입, let vs var, hoisting

```javascript
//1. Use strict
//added in ES 5
//use this for Vanilla Javascript

'use strict';

//2. Variable, rw(read/write)
//let (added in ES6)
{
  let name = 'ellie';
  console.log(name);
  name = 'hello';
  console.log(name);
}

// var (don`t ever use this!)
// var hoisting (move, declaration from bottom to top)

//3. Constant, r(read only)
//favor immutable data type always for a few reasons
// - security
// - thread safety
// - reduce human mistakes
const daysInWeek = 7;
const maxNumber = 5;

//4. Variable types
//primitive, single item: number, string, boolean, null, undefined, symbol
//object, box container
//function, first-class function

const count = 17; //integer
const size = 17.1; //decimal number
console.log(`value: ${count}, type: ${typeof count}`);
console.log(`value: ${size}, type: ${typeof size}`);

//string
const char = 'c';
const brendan = 'brendan';
const greeting = 'hello ' + brendan;
console.log(`value: ${greeting}, type: ${typeof greeting}`);
const helloBob = `h1 ${brendan}!`; //template literals (string)
console.log(`value: ${helloBob}, type: ${typeof helloBob}`);

//boolean
//false: 0, null, undefined, NaN, ''
//true: any other value
const canRead = true;
const test = 3 < 1; //false
console.log(`value: ${canRead}, type: ${typeof canRead}`);
console.log(`value: ${test}, type: ${typeof test}`);

//null
let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);

//undefined
let x;
console.log(`value: ${x}, type: ${typeof x}`);

//symbol, create unique identifiers for objects
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2);
const gsymbol1 = Symbol.for('id');
const gsymbol2 = Symbol.for('id');
console.log(gsymbol1 === gsymbol2); //true
// console.log(`value: ${symbol1}, type: ${typeof symbol1}`); //에러
console.log(`value: ${symbol1.description}, type: ${typeof symbol1}`);

//5. Dynamic typing: dynamically typed language
let text = 'hello';
console.log(`value: ${text}, type: ${typeof text}`);
text = 1;
console.log(`value: ${text}, type: ${typeof text}`);
text = '7' + 5;
console.log(`value: ${text}, type: ${typeof text}`);
text = '8' / '2';
console.log(`value: ${text}, type: ${typeof text}`);
```

## 연산자, if, for loop

```javascript
'use strict';

//1. String concatenation
console.log('my' + 'cat');
console.log('1' + 2);
console.log(`string literals:

'''''
1+2=${1 + 2}`);

console.log("elli\'s book");

//2. Numeric operators
console.log(1 + 1); //add
console.log(1 - 1); //substract
console.log(1 / 1); //divide
console.log(1 * 1); //multiply
console.log(5 % 2); //remainder
console.log(2 ** 3); //exponentiation

//3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;
//counter = counter +1;
//preIncrement = counter;
const postIncrement = counter++;
//preIncrement = counter;
//counter = counter +1;

//4. Assignment operators
let x = 3;
let y = 6;
x += y; //x = x + y;
x -= y;
x *= y;
x /= y;

//5. Comparison operators
console.log(10 < 6);
console.log(10 <= 6);
console.log(10 > 6);
console.log(10 >= 6);

//6. Logical operators: || (or), && (and), ! (not)
const value1 = false;
const value2 = 4 < 2;

//7. Equality
const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);

// === strict equality, no type conversion
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

// object equality by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;
console.log(ellie1 == ellie2);
console.log(ellie1 === ellie2);
console.log(ellie1 === ellie3);

//8. Conditional operators: if
// if else if, else
const name = 'ellie';
if (name === 'ellie') {
  console.log('Welcome, Ellie');
} else if (name === 'coder') {
  console.log('You are amazing coder');
} else {
  console.log('unknown');
}

//9. Ternary operator: ?
//condition ? value1 : value2
console.log(name === 'ellie' ? 'yes' : 'no');

//10. Switch statement
//use for multiple if checks
//use for enum-like value check
//use for multiple type checks in TS
const browser = 'IE';
switch (browser) {
  case 'IE':
    console.log('go away');
    break;
  case 'Chrome':
    console.log('love you');
    break;
  case 'Firefox':
    console.log('love you');
    break;
  default:
    console.log('same all');
    break;
}

//11. Loops
//while loop, while the condition is truthy,
//body code is executed.
let i = 3;
while (i > 0) {
  console.log(`while: ${i}`);
  i--;
}

// do while loop, body code is executed first,
//then check the condition.
do {
  console.log(`do while: ${i}`);
  i--;
} while (i > 0);

//for loop, for(begin; condition; step)
for (i = 3; i > 0; i--) {
  console.log(`for: ${i}`);
}

for (let i = 3; i > 0; i = i - 2) {
  //inline variable declaration
  console.log(`inline variable for: ${i}`);
}

//nested loops
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    console.log(`i: ${i}, j:${j}`);
  }
}
```

## 함수의 선언과 표현

```javascript
'use strict';

//Function
//- fundamental building block in the program
//- subprogram can be used multiple times
//- performs a task or calculates a value

//1. Function declaration
//function name(param1, param2) {body... return;}
//one function === one thing
//naming: doSomething, command, verb
//e.g. createCardAndPoint -> createCard, createPoint
//function is object in JS
function printHello() {
  console.log('Hello');
}
printHello();

function log(message) {
  console.log(message);
}
log('Hello@');

//2. Parameters
//primitive parameters : passed by value
//object parameters: passed by reference
function changeName(obj) {
  obj.name = 'coder';
}
const ellie = { name: 'ellie' };
changeName(ellie);
console.log(ellie);

//3. Default parameters (added in ES6)
function showMessage(message, from = 'unknown') {
  console.log(`${message} by ${from}`);
}
showMessage('Hi!');

//4. Rest parameters (added in ES6)
function printAll(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
  for (const arg of args) {
    console.log(arg);
  }
}
printAll('dream', 'coding', 'ellie');

//5. Local scope
let globalMessage = 'global'; //global variable
function printMessage() {
  let message = 'hello';
  console.log(message); //local variable
  console.log(globalMessage);
}
printMessage();

//6. Return a value
function sum(a, b) {
  return a + b;
}
const result = sum(1, 2); //3
console.log(`sum: ${sum(1, 2)}`);

//7. Early return, early exit
//bad
function upgradeUser(user) {
  if (user.point > 10) {
    //long upgrade logic...
  }
}

//1. Function expression
const print = function () { //anonymous function
  console.log('print');
};
print();
const printAgain = print;
printAgain();
const sumAgain = sum;
console.log(sumAgain(1, 3));

//2. Callback function using function expression
function randomQuiz(answer, printYes, printNo) {
  if (answer === 'love you') {
    printYes();
  } else {
    printNo();
  }
}
//anonymous function
const printYes = function () {
  console.log('yes!');
}
//named function
const printNo = function print() {
  console.log('no!');
}
randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);

//Arrow function
//always anonymous function
const simplePrint = function () {
  console.log('simplePrint');
}
const simplePrint2 = () => console.log('simplePrint');
// const add = (a,b) => a+b;
const add = function (a, b) {
  return a + b;
}

//IIFE: Immediately Invoked Function Expression
(function hello() {
  console.log("IIFE");
})();
```

## 객체지향 언어 클래스 정리

```javascript
'use strict';
//class: template

//1. Class declarations
class Person {
  // constructor
  constructor(name, age) {
    //fields
    this.name = name;
    this.age = age;
  }
  //methods
  speak() {
    console.log(`${this.name}: hello!`);
  }
}
const ellie = new Person('ellie', 20);
console.log(ellie.name);
console.log(ellie.age);
ellie.speak();

//2. Getter and setters
class User {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  get age() {
    return this._age;
  }
  set age(value) {
    this._age = value;
  }
}
const user1 = new User('steve', 'job', -1);
console.log(user1.age);

//3. Fields (public, private)
class Experiment {
  publicField = 2;
  #privateField = 0;
}
const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

//4. Static properties and methods
class Article {
  static publisher = 'Dream Coding';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }
  static printPublisher() {
    console.log(Article.publisher);
  }
}

//5. Inheritance
//a way for one class to extend another class.
class Shape {
  constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
  }
  draw() {
    console.log(`drawing ${this.color} color of`);
  }
  getArea() {
    return width * this.height;
  }
}
class Rectangle extends Shape {}

//6. Class checking: instanceOf
```

## 오브젝트

```javascript
'use strict';

//Objects
// one of the JavaScript`s data types.
// a collection of related data and/or functionality.
// Nearly all objects in JavaScript are instances of Object
// object = {key : value};

//1. Literals and properties
const obj1 = {}; //'object literal' syntax
const obj2 = new Object(); //'object constructor' syntax

function print(person) {
  console.log(person.name);
  console.log(person.age);
}

const ellie = { name: 'ellie', age: 4 };
print(ellie);

// with JavaScript magic (dynamically typed language)
// can add properties later
ellie.hasJob = true;
console.log(ellie.hasJob);

// can delete properties later
delete ellie.hasJob;
console.log(ellie.hasJob);

//2. Computed properties
// key should be always string
console.log(ellie.name);
console.log(ellie['name']);
ellie['hasJob'] = true;
console.log(ellie.hasJob);

function printValue(obj, key) {
  console.log(obj[key]);
}
printValue(ellie, 'name');
printValue(ellie, 'age');

//3. Property value shorthand
const person1 = { name: 'bab', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };
const person4 = new Person();
console.log(person4);

//4. Constructor Function
function Person(name, age) {
  //this = {};
  this.name = name;
  this.age = age;
  //return this;
}

//5. in operator: property existence check (key in obj)
console.log('name' in ellie);
console.log('age' in ellie);
console.log('random' in ellie);
console.log(ellie.random);

// 6. for..in vs for..of
// for (key in obj)
console.clear();
for (key in ellie) {
  console.log(key);
}

//for(value of iterable)
const array = [1, 2, 3, 4, 5];
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}

for (value of array) {
  console.log(value);
}

//7. Fun cloning
//Object.assign(dest, [obj1, obj2, obj3...])
const user = { name: 'ellie', age: '20' };
const user2 = user;
user2.name = 'coder';
console.log(user);

//old way
const user3 = {};
for (key in user) {
  user3[key] = user[key];
}
console.clear();
console.log(user3);

const user4 = Object.assign({}, user);
console.log(user4);

//another example
const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2);
console.log(mixed.color);
console.log(mixed.size);
```

## 배열 개념과 API 총정리

```javascript
'use strict';

// Array

//1. Declaration
const arr1 = new Array();
const arr2 = [1, 2];

//2. Index position
const fruits = ['apple', 'banana'];
console.log(fruits);
console.log(fruits.length);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
console.log(fruits[fruits.length - 1]);

console.clear();
//3. Looping over an array
//print all fruits
//a. for
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

//b. for of
for (let fruit of fruits) {
  console.log(fruit);
}

//c. forEach
fruits.forEach(function (fruit, index) {
  console.log(fruit, index);
});
fruits.forEach((fruit, index) => console.log(fruit, index));

//4. Addition, deletion, copy
//push: add an item to the end
fruits.push('strawberry', 'peach');
console.log(fruits);

//pop: remove an item from the end
fruits.pop();
fruits.pop();
console.log(fruits);

//unshift: add an item to the beginning
fruits.unshift('strawberry', 'peach');
console.log(fruits);
//shift: remove an item from the beginning
fruits.shift();
fruits.shift();
console.log(fruits);

//note! shift, unshift are slower than pop, push
//splice: remove an item by index position
fruits.push('strawberry', 'peach', 'lemon');
console.log(fruits);
fruits.splice(1, 1);
console.log(fruits);
fruits.splice(1, 1, 'green apple', 'watermelon');
console.log(fruits);

//combine two arrays
const fruits2 = ['pear', 'coconut'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);

//5. Searching
//indexOf: find the index
console.clear();
console.log(fruits);
console.log(fruits.indexOf('apple'));
console.log(fruits.indexOf('watermelon'));
console.log(fruits.indexOf('pepper'));

//includes
console.log(fruits.includes('watermelon'));
console.log(fruits.includes('pepper'));

//lastIndexOf
console.clear();
fruits.push('apple');
console.log(fruits);
console.log(fruits.indexOf('apple'));
console.log(fruits.lastIndexOf('apple'));
```

## 유용한 10가지 배열 함수

```javascript
// Q1. make a string out of an array
{
  const fruits = ['apple', 'banana', 'orange'];
  const result = fruits.join();
  console.log(result);
}

// Q2. make an array out of a string
{
  const fruits = 'apple, kiwi, banana, cherry';
  const result1 = fruits.split(',', 2);
  console.log(result1);
}

// Q3. make this array look like this: [5, 4, 3, 2, 1]
{
  const array = [1, 2, 3, 4, 5];
  const result = array.reverse();
  console.log(result);
}

// Q4. make new array without the first two elements
{
  const array = [1, 2, 3, 4, 5];
  const result = array.slice(2, 5);
  console.log(result);
  console.log(array);
}

class Student {
  constructor(name, age, enrolled, score) {
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student('A', 29, true, 45),
  new Student('B', 28, false, 80),
  new Student('C', 30, true, 90),
  new Student('D', 40, false, 66),
  new Student('E', 18, true, 88),
];

// Q5. find a student with the score 90
{
  const result = students.find(function (student, index) {
    return student.score === 90;
  });
  console.log(result);
}

// Q6. make an array of enrolled students
{
  const result = students.filter((student) => student.enrolled);
  console.log(result);
}

// Q7. make an array containing only the students' scores
// result should be: [45, 80, 90, 66, 88]
{
  const result = students.map((student) => student.score);
  console.log(result);
}

// Q8. check if there is a student with the score lower than 50
{
  const result = students.some((student) => student.score < 50);
  console.log(result);

  const result2 = !students.every((student) => student.score < 50);
  console.log(result2);
}

// Q9. compute students' average score
{
  const result = students.reduce((prev, curr) => {
    console.log(prev);
    console.log(curr);
    return prev + curr.score;
  }, 0);
  console.log(result);
}

// Q10. make a string containing all the scores
// result should be: '45, 80, 90, 66, 88'
{
  const result = students
    .map((student) => student.score)
    .filter((score) => score >= 50)
    .join();
  console.log(result);
}

// Bonus! do Q10 sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
  const result = students
    .map((student) => student.score)
    .sort((a, b) => a - b)
    .join();
  console.log(result);
}
```

## JSON 개념 정리 및 활용

```javascript
//JSON
//JavaScript Object Notation

//1. Object to JSON
//stringify(obj)
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const rabbit = {
  name: 'tori',
  color: 'white',
  size: null,
  birthDate: new Date(),
  jump: () => {
    console.log(`${name} can jump!`);
  },
};

json = JSON.stringify(rabbit);
console.log(json);

json = JSON.stringify(rabbit, ["name", "color"]);
console.log(json);

//2. JSON to Object
//parse(JSON)
console.clear();
json = JSON.stringify(rabbit);
const obj = JSON.parse(json);
console.log(obj);
rabbit.jump();
// obj.jump();

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());
```

## 콜백 (Callback)

```javascript
'use strict';

// JavaScript is synchronous.
// Execute the code block by order after hoisting.
//hoisting: var, function declaration
console.log('1');
setTimeout(function () { console.log('2'); }, 1000);
console.log('3');

//synchronous callback
function printImmediately(print) {
  print();
}
printImmediately(() => console.log('hello'));

//Asynchronous callback
function printWithDelay(print, timeout) {
  setTimeout(print, timeout);
}
printWithDelay(() => console.log('async call back'), 2000);

//Callback Hell example
class UserStorage {
  loginUser(id, password, onSuccess, onError) {
    setTimeout(() => {
      if (
        (id === 'ellie' && password === 'dream') ||
        (id === 'coder' && password === 'academy')
      ) {
        onSuccess(id);
      } else {
        onError(new Error('not found'));
      }
    }, 2000);
  }
  getRoles(user, onSuccess, onError) {
    setTimeout(() => {
      if (user === 'ellie') {
        onSuccess({ name: 'ellie', role: 'admin' });
      } else {
        onError(new Error('no access'));
      }
    }, 1000);
  }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
  id,
  password,
  user => {
    userStorage.getRoles(
      user,
      userWithRole => {
        alert(`Hello ${userWithRole.name}, you have a ${userWithRole.role} role`);
      },
      error => {
        console.log(error);
      }
    );
  },
  error => { console.log(error); }
);
```

## 알아두면 좋은 코드

```html
<script type="text/javascript">
  function del() {
    ans = confirm("정말 삭제하시겠습니까?");
    if (ans == true) {
      document.form.action.value = "delete";
      document.form.submit();
    } else {
      return;
    }
  }
</script>
```

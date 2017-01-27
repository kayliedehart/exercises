'use strict'

let animals = [
  { name: 'Luna', species: 'cat'},
  { name: 'Fifi', species: 'dog'},
  { name: 'Bob', species: 'fish'},
  { name: 'Pidgey', species: 'bird'},
  { name: 'Munk', species: 'chipmunk'},
  { name: 'Lulu', species: 'cat'},
]
let isCat = animal => (animal.species === 'cat')

let cats = animals.filter(animal => animal.species === 'cat') //smaller array
let add_animals = animals.map((animal) => animal.name) //a mutated array

let total_cats = animals.reduce((cat_count, animal) => cat_count += (isCat(animal) ? 1 : 0), 0) //an object


// console.log(cats);
// console.log(add_animals);
// console.log(total_cats);

//currying example
let curry_recipe = base => protein => sauce => ('This is a ' + sauce + ' curry with ' + protein + ' on ' + base)
//console.log(curry_recipe('rice')('tofu')('masala'));

let tree = [
  {id: 'animal', 'parent' : null},
  {id: 'mammal', 'parent' : 'animal'},
  {id: 'cat', 'parent' : 'mammal'},
  {id: 'dog', 'parent' : 'mammal'},
  {id: 'fish', 'parent' : 'animal'},
  {id: 'husky', 'parent' : 'dog'},
  {id: 'lion', 'parent' : 'cat'},
  {id: 'leopard', 'parent' : 'cat'},
  {id: 'clown fish', 'parent' : 'fish'},
  {id: 'nemo', 'parent' : 'clown fish'},
  {id: 'fluffy', 'parent' : 'husky'},
]

let makeTree = (categories, parent) => {
  let node = {}
  categories
    .filter(c => c.parent === parent)
    .forEach(c => node[c.id] = makeTree(categories, c.id))
  return node
}

console.log(JSON.stringify(makeTree(tree, null), null, 2));

// Promises
function loadImage(url) {
  return new Promise((resolve, reject) => {
    let image = new Image()

    image.onload = function() {
      resolve(image)
    }

    image.onerror = function() {
      let message =
        'Could not load image at ' + url
      reject(new Error(msg))
    }

    image.src = url

  })
}

let addImg = (src) => {
  let imgElement =
    document.createElement("img")
  imgElement.src = src
  document.body.appendChild(imgElement)
}

Promise.all([
  loadImage('https://unsplash.it/200/300/?random'),
  loadImage('https://unsplash.it/200/300/?random'),
  loadImage('https://unsplash.it/200/300/?random'),
  loadImage('https://unsplash.it/200/300/?random')
]).then((images) => {
  images.forEach(img => addImg(img.src))
}).catch((error) => {
  // handle error later
})

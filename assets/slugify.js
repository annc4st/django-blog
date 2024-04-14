const titleInput = document.querySelector('input[name="title"]');
const slugInput = document.querySelector('input[name="slug"]');
 


const slugFunc = (val) => {
    let result = val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')
    .replace(/[\s\W]+/g, '-');
    return result
}


titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugFunc(titleInput.value))

})
function createCupcake(cupcake) {
    return `
        <div data-cupcake-id=${cupcake.id}>
            <li>
            ${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating} 
            </li>
            <img src="${cupcake.image}" alt="cupcake">
        </div>
    `
}

async function displayCupcakes() {
    const response = await axios.get('http://127.0.0.1:5000//api/cupcakes')
    for (let details of response.data.cupcakes) {
        let newCupcake = $(createCupcake(details))
        $('.cupcakes-list').append(newCupcake)
    }
}

// form to add cupcakes 
$('.cupcake-form').on('submit', async function(evt) {
    evt.preventDefault(); 

    let flavor = $('#flavor').val()
    let rating = $('#rating').val() 
    let size = $('#size').val() 
    let image = $('#image').val() 

    const cupcakeAxios = await axios.post('http://127.0.0.1:5000/api/cupcakes', {
        flavor, rating, size, image 
    }); 

    let newCupcake = $(createCupcake(cupcakeAxios.data.cupcake))
    $('.cupcakes-list').append(newCupcake)
    $('.cupcake-form').trigger('reset')
})

$(displayCupcakes); 
const serverPath = 'http://127.0.0.1:8000'

window.addEventListener('DOMContentLoaded', () => {
    const url = serverPath + '/get_location_names';
    fetch(url).then(response => {
        return response.json();
    }).then(data => {
        const uiLocations = document.getElementById('uiLocations');
        data.locations.forEach(loc => {
            const el = document.createElement('option');
            el.innerHTML = loc;
            el.onclick = () => el.setAttribute('selected', 'selected');
            uiLocations.appendChild(el)
        });
    });

    const locationsEl = document.getElementById('uiLocations');
    locationsEl.addEventListener('click', () => {
        if (locationsEl.classList.contains('show-menu')) {
            locationsEl.classList.remove('show-menu');
        } else {
            locationsEl.classList.add('show-menu');
            locationsEl.querySelectorAll('[selected]').forEach(el => {
                el.removeAttribute('selected');
            });
        }
    });
});

const onClickSubmit = () => {
    const bedrooms = document.querySelector('.switch-field.bedrooms input[checked]')?.value
    const bathrooms = document.querySelector('.switch-field.bathrooms input[checked]')?.value
    const location = document.querySelector('#uiLocations [selected]')?.value
    const square_feet = document.getElementById('uiSqft')?.value
    const url = serverPath + '/predict_home_price';
    fetch(url, {
        type: 'POST',
        contentType: 'application/json',
        datatype: 'json',
        data: { bedrooms, bathrooms, location, square_feet}
    }).then(response => {
        const resultEl = document.querySelector('#uiEstimatedPrice h2');
        resultEl.innerHTML = 'Estimated Price (Lakh): ' + response.data.price_prediction;
    });
}
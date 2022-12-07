const api = "http://localhost:8888"

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST', 
      mode: 'cors', 
      cache: 'no-cache', 
      credentials: 'same-origin', 
      headers: {
        'Content-Type': 'application/json',
        'Content-Type':'application/x-www-form-urlencoded'
      },
      redirect: 'follow', 
      referrerPolicy: 'no-referrer', 
      body: JSON.stringify(data) 
    });
    return response.json();
}
  

document.querySelector("#btn-send").addEventListener('click', function(event) {
    const object = {
        lname : document.querySelector("#lname").value,
        fname : document.querySelector("#fname").value,
        pname : document.querySelector("#patronymic-name").value,
        phone : document.querySelector("#phone").value,
        message : document.querySelector("#message").value
    };
    console.log(JSON.stringify(object));
    postData(api, object)
    .then((data) => {
        console.log(data);
    });

});
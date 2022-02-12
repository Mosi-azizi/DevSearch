
    let form = document.getElementById('login-form')

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        // console.log('From was submitted')


        let formData = {
            'username' : form.username.value,
            'password' : form.password.value
        }

        fetch('http://127.0.0.1:8000/api/users/token/',{
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                console.log('DATA',data.accessToken)
                if(data.access){
                    localStorage.setItem('token',data.access)
                    window.location = 'http://localhost:63342/DevSearch/FRONTEND/projects-list.html?_ijt=54t7n7ho69slmt44a2pdafm9m8'
                }else {
                    alert('Username OR password dose not work')
                }
            })
    })
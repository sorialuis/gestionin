<script>
    let DNI= '';
    let password = '';
    let data = {};
    
    var formData = new FormData();
    const API = "http://192.168.100.6:8000/users/login/";
	
	async function handleClick () {
        formData.append( 'dni' , `${DNI}` );
        formData.append( 'password' , `${password}` );
		const res = await fetch(API, {
            mode:'no-cors',
			method: 'POST',
			body: formData,
		})
		
		const json = await res.json()
		data = JSON.stringify(json)
	}
   

 
/*    async function handleClick() {
        formData.append( 'dni' , `${DNI}` );
        formData.append( 'password' , `${password}` );
		const response = await fetch( API , {
        mode:'no-cors',
        method:'POST',
        body:formData,
        });
        data = await response.json();
    

   // console.log(data);
    console.log("hola");
    alert( ` ${DNI}  ${password}`  );
    };

*/
</script>


<style>
.Login-container {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    background-color: yellowgreen;
    padding-bottom: 2rem;
    margin: auto;
    margin-top: 5rem;
    width: 20%;
    text-align: center;
    border:0.2rem solid black;
    border-radius: 1rem;
}

.Login-header{
    position: relative;
    bottom: 2.5em;
    text-align: center;
}

.Login-dni {
    padding-bottom: 1rem;
}

.Login-password {
    padding-bottom: 1rem;
}

.dni {
    text-align: center;
    border-radius: 2rem;
}



.password {
    text-align: center;
    border-radius: 2rem;
}

.dni:hover {
    font-size: 95%;
}


.password:hover {
    font-size: 95%;
}

.Login-in {
    padding-bottom: 1rem;
}

.Login-Titulo {
    box-sizing: border-box;
    width: 15%;
    margin: auto;
    margin-top: 0;
    text-align: center;
    font-family: "Pacifico", cursive;
    border-color: red blue green yellow;
    border-width: 1rem;
    border-style: solid;
    background-color: #fafafa;
    color: black;
}

i{
    color: black;
}

.Login-Titulo:hover {
    animation: random 5s infinite;
}

h2 {
    box-sizing: content-box;
    padding: 0;
    margin: 0;
}

button {
    border-radius: 1rem;
    background-color: #80ACF0;
}

img{
    width: 75%;
    border:0.2rem solid black;
    border-radius: 2rem;
}

.in:hover{
    width: 30%; 
}

.checkins:hover{
    width: 40%;
}

@keyframes  random {
    0% { border-color:red blue green yellow; } 
    33% { border-color: yellow red blue green; } 
    66% { border-color: green yellow red blue; } 
    99% { border-color: blue green yellow red; } 
}

</style>
<div class="Login">
    <div class="Login-Titulo" >
        <h2>Gestionin</h2>
    </div>
    <div class="Login-container">
        <div class="Login-header">
            <img src="https://iwcoweb.blob.core.windows.net/imagenes/Blog%20IW/Roles%20de%20usuario/Encabezado.png"  alt="">
            <h2>Iniciar Sesion</h2>
        </div>
        <div class="Login-input">
            <div class="Login-dni">
                <i class="fas fa-user"></i>
                <input  bind:value={DNI}  type="text" class="dni" placeholder="DNI" id="dni">
            </div>
            <div class="Login-password">
                <i class="fas fa-unlock"></i>
                <input bind:value={password} type="text" class="password" placeholder="Contraseña" id="password">
            </div>
        </div>
        <div class="Login-Buttons">
            <div class="Login-in">
                <button type="button" class="in" on:click={handleClick}>Ingresar</button>
            </div>
            <div class="Login-checkin">
                <button  class="checkins">Registrarse</button>
            </div>
        </div>
    </div>
</div>